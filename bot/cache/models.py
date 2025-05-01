from bot.cache.mixins import ModuleMixin

from .base import DATA_TYPE, BaseGameCache, BaseModule, BaseUserCache
from .wrapper import FieldWrapper


class Settings(ModuleMixin[BaseUserCache], BaseModule):
    def __init__(self, parent: BaseUserCache) -> None:
        self._parent = parent
        self._data: DATA_TYPE = {}
        self.language = FieldWrapper(self, "language")
        self.id = FieldWrapper(self, "id")
        self.ex_time = None

    def _make_redis_key(self) -> str:
        return f"user:{self._parent.user_id}:settings"


class UserGame(ModuleMixin[BaseUserCache], BaseModule):
    def __init__(self, parent: BaseUserCache) -> None:
        self._parent = parent
        self._data: DATA_TYPE = {}
        self.id = FieldWrapper(self, "id")
        self.ex_time = 60 * 60 * 24 * 7  # 7 days

    def _make_redis_key(self) -> str:
        return f"user:{self._parent.user_id}:game"


class Game(ModuleMixin[BaseGameCache], BaseModule):
    def __init__(self, parent: BaseGameCache) -> None:
        self._parent = parent
        self._data: DATA_TYPE = {}
        self.fen = FieldWrapper(self, "fen")
        self.side = FieldWrapper(self, "side")
        self.updated_at = FieldWrapper(self, "updated_at")
        self.ex_time = None

    def _make_redis_key(self) -> str:
        if self._parent.game_id is None:
            return ""
        return f"game:{self._parent.game_id}"
