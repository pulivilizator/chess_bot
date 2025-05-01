from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import BigInteger, Boolean, ForeignKey, Uuid, text
from sqlalchemy import Enum as SqlAlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.core.enums import GameResult, GameStatus
from database.models.base import Base
from database.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from database.models.users import User


class Game(TimestampMixin, Base):
    __tablename__ = "games"

    id: Mapped[UUID] = mapped_column(
        Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    player_1_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.telegram_id", ondelete="SET NULL")
    )
    player_2_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.telegram_id", ondelete="SET NULL"), nullable=True
    )
    status: Mapped[str] = mapped_column(SqlAlchemyEnum(GameStatus), default=GameStatus.PENDING)
    result: Mapped[str | None] = mapped_column(SqlAlchemyEnum(GameResult), nullable=True)
    is_bot_opponent: Mapped[bool] = mapped_column(Boolean, default=False)

    player_1: Mapped[User] = relationship(
        "User", back_populates="games", foreign_keys=[player_1_id]
    )
    player_2: Mapped[User] = relationship(
        "User", back_populates="games", foreign_keys=[player_2_id]
    )
