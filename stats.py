import json
import os
from datetime import datetime, date, timedelta
from typing import Dict
import asyncio
import logging

# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class UserStats:
    def __init__(self, stats_file: str = "user_stats.json"):
        self.stats_file = stats_file
        self.stats_dir = "/home/user/otcheti/"
        self.ensure_directories()
        self.stats = self.load_stats()
        logger.info(f"📊 Статистика инициализирована. Файл: {self.stats_file}")

    def ensure_directories(self):
        """Создает необходимые директории"""
        os.makedirs(self.stats_dir, exist_ok=True)
        logger.debug(f"✅ Директория создана/проверена: {self.stats_dir}")

    def load_stats(self) -> Dict:
        """Загружает статистику из JSON файла"""
        if os.path.exists(self.stats_file):
            try:
                with open(self.stats_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    logger.info(f"✅ Статистика загружена из {self.stats_file}")
                    logger.debug(f"   Дней в статистике: {len(data.get('daily_stats', {}))}")
                    logger.debug(f"   Месяцев в статистике: {len(data.get('monthly_stats', {}))}")
                    return data
            except Exception as e:
                logger.error(f"❌ Ошибка загрузки статистики: {e}")
                return self.get_empty_stats()
        logger.info("🆕 Файл статистики не найден, создаем новый")
        return self.get_empty_stats()

    def get_empty_stats(self) -> Dict:
        """Возвращает пустую структуру статистики"""
        return {
            "users": {},  # user_id: последняя активность (timestamp)
            "daily_stats": {},  # YYYY-MM-DD: список user_id
            "monthly_stats": {}  # YYYY-MM: список user_id
        }

    def save_stats(self):
        """Сохраняет статистику в JSON файл"""
        try:
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(self.stats, f, ensure_ascii=False, indent=2)
            logger.debug(f"💾 Статистика сохранена в {self.stats_file}")
        except Exception as e:
            logger.error(f"❌ Ошибка сохранения статистики: {e}")

    def register_user_activity(self, user_id: int):
        """Регистрирует активность пользователя с защитой от дублирования"""
        today = date.today().isoformat()  # YYYY-MM-DD
        current_month = today[:7]  # YYYY-MM
        user_id_str = str(user_id)

        # Проверяем, был ли пользователь уже сегодня
        is_new_daily = False
        is_new_monthly = False

        # Обновляем общую статистику пользователей
        self.stats["users"][user_id_str] = datetime.now().timestamp()

        # Обновляем дневную статистику с проверкой на дубликаты
        if today not in self.stats["daily_stats"]:
            self.stats["daily_stats"][today] = []
            logger.info(f"📅 Начат новый день: {today}")

        if user_id_str not in self.stats["daily_stats"][today]:
            self.stats["daily_stats"][today].append(user_id_str)
            is_new_daily = True
            logger.info(f"✨ Новый пользователь {user_id_str} за день {today}")
        else:
            logger.debug(f"👤 Пользователь {user_id_str} уже был сегодня")

        # Обновляем месячную статистику с проверкой на дубликаты
        if current_month not in self.stats["monthly_stats"]:
            self.stats["monthly_stats"][current_month] = []
            logger.info(f"📆 Начат новый месяц: {current_month}")

        if user_id_str not in self.stats["monthly_stats"][current_month]:
            self.stats["monthly_stats"][current_month].append(user_id_str)
            is_new_monthly = True
            logger.info(f"✨ Новый пользователь {user_id_str} за месяц {current_month}")
        else:
            logger.debug(f"👤 Пользователь {user_id_str} уже был в этом месяце")

        self.save_stats()

        # Возвращаем информацию о том, был ли пользователь новым
        return {
            "is_new_daily": is_new_daily,
            "is_new_monthly": is_new_monthly,
            "daily_count": len(self.stats["daily_stats"][today]),
            "monthly_count": len(self.stats["monthly_stats"][current_month])
        }

    def get_daily_users(self, target_date: date = None) -> int:
        """Возвращает количество уникальных пользователей за указанный день"""
        if target_date is None:
            target_date = date.today()
        date_str = target_date.isoformat()

        if date_str in self.stats["daily_stats"]:
            count = len(self.stats["daily_stats"][date_str])
            logger.debug(f"📊 За {date_str} уникальных пользователей: {count}")
            return count
        logger.debug(f"📊 За {date_str} нет данных")
        return 0

    def get_monthly_users(self, target_date: date = None) -> int:
        """Возвращает количество уникальных пользователей за указанный месяц"""
        if target_date is None:
            target_date = date.today()
        month_str = target_date.isoformat()[:7]

        if month_str in self.stats["monthly_stats"]:
            count = len(self.stats["monthly_stats"][month_str])
            logger.debug(f"📊 За {month_str} уникальных пользователей: {count}")
            return count
        logger.debug(f"📊 За {month_str} нет данных")
        return 0

    def generate_daily_report(self, report_date: date = None):
        """Генерирует отчет за указанный день"""
        if report_date is None:
            report_date = date.today()

        daily_users = self.get_daily_users(report_date)
        monthly_users = self.get_monthly_users(report_date)

        # Формируем имя файла: otchet_dd_mm
        filename = f"otchet_{report_date.strftime('%d_%m')}"
        filepath = os.path.join(self.stats_dir, filename)

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"Пользователей за день: {daily_users}\n")
                f.write(f"Пользователей за месяц: {monthly_users}\n")

            logger.info("=" * 50)
            logger.info(f"✅ ОТЧЕТ СОХРАНЕН: {filepath}")
            logger.info(f"   📅 Дата: {report_date.strftime('%d.%m.%Y')}")
            logger.info(f"   👥 Пользователей за день: {daily_users}")
            logger.info(f"   📊 Пользователей за месяц: {monthly_users}")
            logger.info("=" * 50)

            return filepath
        except Exception as e:
            logger.error(f"❌ Ошибка сохранения отчета: {e}")
            return None

    def get_today_stats(self):
        """Возвращает статистику за сегодня"""
        today = date.today()
        daily = self.get_daily_users(today)
        monthly = self.get_monthly_users(today)
        return {
            "daily": daily,
            "monthly": monthly,
            "date": today.isoformat()
        }


# Глобальный экземпляр статистики
stats = UserStats()


async def scheduled_report():
    """Планировщик для ежедневного формирования отчетов"""
    logger.info("⏰ Планировщик отчетов запущен")

    while True:
        now = datetime.now()
        # Вычисляем время до следующего дня (00:05)
        next_run = datetime(now.year, now.month, now.day) + timedelta(days=1, minutes=5)
        sleep_seconds = (next_run - now).total_seconds()

        logger.info(
            f"⏰ Следующий отчет будет сформирован через {sleep_seconds / 3600:.1f} часов (в {next_run.strftime('%H:%M %d.%m')})")
        await asyncio.sleep(sleep_seconds)

        # Формируем отчет за вчерашний день
        yesterday = date.today() - timedelta(days=1)
        logger.info(f"📝 Формирование отчета за {yesterday.strftime('%d.%m.%Y')}")
        stats.generate_daily_report(yesterday)

        # Показываем статистику за сегодня
        today_stats = stats.get_today_stats()
        logger.info(f"📊 Текущая статистика за сегодня: {today_stats['daily']} пользователей")