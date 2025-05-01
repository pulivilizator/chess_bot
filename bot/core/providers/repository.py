from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from bot.core import dto
from bot.repository import UserRepository, UserSettingsRepository
from bot.repository.impl.game import GameRepository
from database.models import User, UserSettings
from database.models.games import Game


class RepositoryProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_user_repository(self, session: AsyncSession) -> UserRepository:
        return UserRepository(
            session=session,
            model=User,
            dto_model=dto.UserWithSettingsDTO,
            lookup_field="telegram_id",
        )

    @provide(scope=Scope.REQUEST)
    def get_user_settings_repository(
        self,
        session: AsyncSession,
    ) -> UserSettingsRepository:
        return UserSettingsRepository(
            session=session,
            model=UserSettings,
            dto_model=dto.UserSettingsDTO,
            lookup_field="id",
        )

    @provide(scope=Scope.REQUEST)
    def get_game_repository(self, session: AsyncSession) -> GameRepository:
        return GameRepository(
            session=session,
            model=Game,
            dto_model=dto.GameDTO,
            lookup_field="id",
        )
