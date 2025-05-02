from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from bot.cache.cache import GameCache


@inject
async def start_game(
    message: Message,
    widget: Button,
    dialog_manager: DialogManager,
    game: FromDishka[GameCache],
) -> None: ...
