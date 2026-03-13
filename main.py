import aiomax
import logging
import asyncio
import os
from datetime import datetime, timedelta
from threading import Thread

# Настраиваем логирование
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

from handlers import router
from stats import stats, scheduled_report


def run_scheduler():
    """Запускает планировщик в отдельном потоке"""
    logger.info(" Запуск потока планировщика")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(scheduled_report())
    except Exception as e:
        logger.error(f" Ошибка в планировщике: {e}")


def main():
    logger.info("=" * 60)
    logger.info(" ЗАПУСК БОТА")
    logger.info("=" * 60)

    bot = aiomax.Bot('_TOKEN_')

    bot.add_router(router)

    # Запускаем планировщик отчетов в отдельном потоке
    scheduler_thread = Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()

    logger.info(f"Статистика будет сохраняться в: /home/user/otcheti/")
    logger.info(f" Файл статистики: user_stats.json")

    # Формируем отчет за предыдущий день при запуске (если сегодня еще не формировали)
    yesterday = datetime.now() - timedelta(days=1)
    report_filename = f"otchet_{yesterday.strftime('%d_%m')}"
    report_path = f"/home/user/otcheti/{report_filename}"

    if not os.path.exists(report_path):
        logger.info(f" Формируем отчет за вчерашний день ({yesterday.strftime('%d.%m')})...")
        stats.generate_daily_report(yesterday.date())
    else:
        logger.info(f" Отчет за вчерашний день уже существует")

    today_stats = stats.get_today_stats()
    logger.info(f" Текущая статистика за сегодня: {today_stats['daily']} пользователей")
    logger.info(f" Статистика за месяц: {today_stats['monthly']} пользователей")

    logger.info("=" * 60)
    logger.info(" Бот готов к работе!")
    logger.info("=" * 60)

    bot.run()


if __name__ == "__main__":
    main()
