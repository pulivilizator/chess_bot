from collections.abc import Awaitable
from typing import Any, Callable

import structlog
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from dishka.integrations.aiogram import FromDishka

from bot.cache import UserCache
from bot.cache.cache import GameCache

from .inject import aiogram_middleware_inject


class CacheMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.logger = structlog.get_logger(self.__class__.__name__)

    @aiogram_middleware_inject
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
        game_cache: FromDishka[GameCache],
        user_cache: FromDishka[UserCache],
    ) -> Any:
        if user_cache.game.id.get_value() and not game_cache:
            game_cache.game_id = str(user_cache.game.id.get_value())
            await game_cache.load()

        return await handler(event, data)
