from dishka import Provider, Scope, provide

from bot.cache.cache import GameCache
from bot.interactors.game import (
    AbandonStaleGamesInteractor,
    CreateGameInteractor,
    DeleteGameInteractor,
    GetGameInteractor,
    UpdateGameStatusInteractor,
)
from bot.interactors.user import (
    CreateUserInteractor,
    GetUserInteractor,
    UpdateUserSettingsInteractor,
)
from bot.repository import GameRepository, UserRepository, UserSettingsRepository


class InteractorProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def create_user(
        self,
        user_repo: UserRepository,
        settings_repo: UserSettingsRepository,
    ) -> CreateUserInteractor:
        return CreateUserInteractor(
            user_repo=user_repo,
            user_settings_repo=settings_repo,
        )

    @provide(scope=Scope.REQUEST)
    def get_user(
        self,
        user_repo: UserRepository,
        settings_repo: UserSettingsRepository,
    ) -> GetUserInteractor:
        return GetUserInteractor(user_repo=user_repo, user_settings_repo=settings_repo)

    @provide(scope=Scope.REQUEST)
    def update_user_settings(
        self,
        settings_repo: UserSettingsRepository,
    ) -> UpdateUserSettingsInteractor:
        return UpdateUserSettingsInteractor(user_settings_repo=settings_repo)

    @provide(scope=Scope.REQUEST)
    def create_game(
        self,
        game_repo: GameRepository,
    ) -> CreateGameInteractor:
        return CreateGameInteractor(game_repo=game_repo)

    @provide(scope=Scope.REQUEST)
    def get_game(
        self,
        game_repo: GameRepository,
    ) -> GetGameInteractor:
        return GetGameInteractor(game_repo=game_repo)

    @provide(scope=Scope.REQUEST)
    def update_game_status(
        self,
        game_repo: GameRepository,
    ) -> UpdateGameStatusInteractor:
        return UpdateGameStatusInteractor(game_repo=game_repo)

    @provide(scope=Scope.REQUEST)
    def delete_game(
        self,
        game_repo: GameRepository,
    ) -> DeleteGameInteractor:
        return DeleteGameInteractor(game_repo=game_repo)

    @provide(scope=Scope.REQUEST)
    def abandon_stale_games(
        self,
        game_repo: GameRepository,
        game_cache: GameCache,
    ) -> AbandonStaleGamesInteractor:
        return AbandonStaleGamesInteractor(game_repo=game_repo, game_cache=game_cache)
