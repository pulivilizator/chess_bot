import asyncio
from datetime import datetime, timedelta
from uuid import UUID

from pydantic import BaseModel

from bot.cache.cache import GameCache
from bot.core import dto
from bot.core.enums import GameResult, GameStatus
from bot.interactors.base import BaseInteractor
from bot.repository import GameRepository


class CreateGameInteractor(BaseInteractor):
    def __init__(self, game_repo: GameRepository) -> None:
        self._game_repo = game_repo

    async def execute(self, data: dto.CreateGameDTO) -> dto.GameDTO:
        return await self._game_repo.create(data)


class GetGameInteractor(BaseInteractor):
    def __init__(self, game_repo: GameRepository) -> None:
        self._game_repo = game_repo

    async def execute(self, game_id: UUID) -> dto.GameDTO | None:
        return await self._game_repo.get_or_none(game_id)


class UpdateGameStatusInteractor(BaseInteractor):
    def __init__(self, game_repo: GameRepository) -> None:
        self._game_repo = game_repo

    async def execute(
        self, game_id: UUID, status: GameStatus, result: GameResult | None = None
    ) -> dto.GameDTO:
        class UpdateModel(BaseModel):
            status: GameStatus
            result: GameResult | None = None

        update_data = UpdateModel(status=status, result=result)
        return await self._game_repo.update(game_id, update_data)


class DeleteGameInteractor(BaseInteractor):
    def __init__(self, game_repo: GameRepository) -> None:
        self._game_repo = game_repo

    async def execute(self, game_id: UUID) -> None:
        await self._game_repo.destroy(game_id)


class AbandonStaleGamesInteractor(BaseInteractor):
    def __init__(self, game_repo: GameRepository, game_cache: GameCache) -> None:
        self._game_repo = game_repo
        self._game_cache = game_cache

    async def execute(self, days_threshold: int = 7) -> int:
        threshold_date = datetime.now() - timedelta(days=days_threshold)
        games = await self._game_repo.get_stale_games(threshold_date)
        ids = [str(game.id) for game in games]
        count = 0

        class UpdateModel(BaseModel):
            status: GameStatus = GameStatus.CANCELLED
            result: GameResult = GameResult.ABANDONED

        update_data = UpdateModel()

        for game in games:
            await self._game_repo.update(game.id, update_data)
            count += 1

        await asyncio.gather(*[self._game_cache.game.delete(game_id) for game_id in ids])

        return count
