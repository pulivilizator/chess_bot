from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from bot.core.enums import GameResult, GameStatus, Languages


class UserDTO(BaseModel):
    telegram_id: int
    is_active: bool
    is_admin: bool


class UserSettingsDTO(BaseModel):
    id: Optional[UUID] = None
    language: Languages
    user_id: Optional[int]


class UserWithSettingsDTO(UserDTO):
    settings: UserSettingsDTO


class CreateUserDTO(BaseModel):
    user: UserDTO
    settings: UserSettingsDTO


class UpdateUserSettingsDTO(BaseModel):
    language: Languages


class CreateGameDTO(BaseModel):
    player_1_id: int
    player_2_id: int | None = None
    is_bot_opponent: bool = False
    status: GameStatus = GameStatus.PENDING


class GameDTO(BaseModel):
    id: UUID
    player_1_id: int
    player_2_id: int | None
    status: GameStatus
    result: GameResult | None
    is_bot_opponent: bool
    created_at: datetime
    updated_at: datetime
