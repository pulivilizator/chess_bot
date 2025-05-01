from __future__ import annotations

from redis.asyncio import Redis

from .base import BaseGameCache, BaseUserCache
from .mixins import CacheMixin
from .models import Game, Settings, UserGame


class UserCache(CacheMixin, BaseUserCache):
    def __init__(self, user_id: int, redis: Redis[str]) -> None:
        self.user_id = user_id
        self.redis = redis
        self.settings = Settings(self)
        self.game = UserGame(self)
        self.ex_time = 60 * 60 * 6  # 6 hours


class GameCache(CacheMixin, BaseGameCache):
    def __init__(self, game_id: str, redis: Redis[str]) -> None:
        self.game_id = game_id
        self.redis = redis
        self.game = Game(self)
        self.ex_time = 60 * 60 * 24 * 7  # 7 days

    def __bool__(self) -> bool:
        return bool(self.game_id)
