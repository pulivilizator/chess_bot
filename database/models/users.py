from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import (
    BigInteger,
    Boolean,
    ForeignKey,
    Uuid,
    text,
)
from sqlalchemy import (
    Enum as SqlAlchemyEnum,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.core.enums import Languages

from .base import Base
from .mixins import TimestampMixin

if TYPE_CHECKING:
    from .games import Game


class User(TimestampMixin, Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=True)

    settings: Mapped[UserSettings] = relationship(
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
        lazy="joined",
    )
    games: Mapped[list[Game]] = relationship(
        "Game",
        back_populates="player_1",
        foreign_keys="Game.player_1_id",
        primaryjoin="User.telegram_id == Game.player_1_id",
    )


class UserSettings(TimestampMixin, Base):
    __tablename__ = "users_settings"

    id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    language: Mapped[str] = mapped_column(
        SqlAlchemyEnum(Languages),
        nullable=False,
        default=Languages.EN,
    )
    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("users.telegram_id", ondelete="CASCADE"),
        unique=True,
    )

    user: Mapped[User] = relationship(back_populates="settings")
