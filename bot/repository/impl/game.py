from bot.core.dto import GameDTO
from bot.repository.interfaces.sqlalchemy_repository import SQLAlchemyRepository
from database.models import Game


class GameRepository(SQLAlchemyRepository[Game, GameDTO]):
    pass
