from datetime import datetime

from sqlalchemy import select

from bot.core.dto import GameDTO
from bot.core.enums import GameStatus
from bot.repository.interfaces.sqlalchemy_repository import SQLAlchemyRepository
from database.models import Game


class GameRepository(SQLAlchemyRepository[Game, GameDTO]):
    async def get_stale_games(self, threshold_date: datetime) -> list[GameDTO]:
        query = select(Game).where(
            Game.status.in_([GameStatus.PENDING, GameStatus.ACTIVE]),
            Game.updated_at < threshold_date,
        )
        result = await self._session.execute(query)
        return [
            self._dto_model.model_validate(obj, from_attributes=True)
            for obj in result.scalars().all()
        ]
