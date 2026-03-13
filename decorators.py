from functools import wraps
import logging
from stats import stats

logger = logging.getLogger(__name__)


def get_user_id_from_context(ctx):
    """Универсальная функция для получения user_id из разных типов контекста"""
    try:
        # Пробуем разные варианты получения user_id
        if hasattr(ctx, 'from_user') and hasattr(ctx.from_user, 'id'):
            return ctx.from_user.id
        elif hasattr(ctx, 'user_id'):
            return ctx.user_id
        elif hasattr(ctx, 'message') and hasattr(ctx.message, 'from_user'):
            return ctx.message.from_user.id
        elif hasattr(ctx, 'callback') and hasattr(ctx.callback, 'from_user'):
            return ctx.callback.from_user.id
        elif hasattr(ctx, 'effective_user') and hasattr(ctx.effective_user, 'id'):
            return ctx.effective_user.id
    except Exception as e:
        logger.error(f"Ошибка получения user_id: {e}")

    logger.warning("⚠️ Не удалось получить user_id из контекста")
    return None


def track_activity(func):
    """Декоратор для отслеживания активности пользователя с защитой от дублирования"""

    @wraps(func)
    async def wrapper(ctx, *args, **kwargs):
        # Получаем user_id из контекста
        user_id = get_user_id_from_context(ctx)

        if user_id:
            # Регистрируем активность и получаем статистику
            activity_info = stats.register_user_activity(user_id)

            # Логируем для отладки (можно убрать в продакшене)
            func_name = func.__name__
            if activity_info['is_new_daily']:
                logger.info(f"🎯 {func_name}: Новый пользователь {user_id} за сегодня")
            if activity_info['is_new_monthly']:
                logger.info(f"🎯 {func_name}: Новый пользователь {user_id} за месяц")
        else:
            logger.warning(f"⚠️ {func.__name__}: Не удалось определить пользователя")

        # Вызываем оригинальную функцию
        return await func(ctx, *args, **kwargs)

    return wrapper