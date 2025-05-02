import asyncio
from typing import Callable, Generic, Self

from bot.cache.base import CACHE_TYPE, DATA_TYPE
from bot.core.enums import CacheLoadModules


class FindMixin:
    def find(self, key: str) -> str | int | None:
        for attr in self.__dict__.values():
            data = getattr(attr, "_data", None)
            if isinstance(data, dict) and key in data:
                return data.get(key)
        return None


class LoadMixin:
    async def load(self, load_modules: list[CacheLoadModules] | None = None) -> Self:
        if load_modules is None:
            load_modules = list(CacheLoadModules)
        tasks = [getattr(self, module).load() for module in load_modules]
        await asyncio.gather(*tasks)
        return self


class CacheMixin(FindMixin, LoadMixin):
    pass


class ModuleMixin(Generic[CACHE_TYPE]):
    _parent: CACHE_TYPE
    _data: DATA_TYPE
    _make_redis_key: Callable[[], str]
    ex_time: int | None

    async def load(self) -> None:
        redis_key = self._make_redis_key()
        raw_data = await self._parent.redis.hgetall(redis_key)

        self._data = {k: int(v) if v.isdigit() else v for k, v in raw_data.items()}

    async def _save_field(self, field_name: str, value: str | int | None) -> None:
        if value is None:
            value = ""
        redis_key = self._make_redis_key()
        await self._parent.redis.hset(redis_key, field_name, value)
        if self.ex_time is not None:
            await self._parent.redis.expire(redis_key, self.ex_time)
        elif self._parent.ex_time:
            await self._parent.redis.expire(redis_key, self._parent.ex_time)

    async def delete(self, game_id: str | None = None) -> None:
        if game_id is None:
            redis_key = self._make_redis_key()
            await self._parent.redis.delete(redis_key)
        else:
            redis_key = self._make_redis_key()
            await self._parent.redis.delete(redis_key)

    @property
    def data(self) -> DATA_TYPE:
        return self._data
