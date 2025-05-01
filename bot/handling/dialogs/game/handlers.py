from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from dishka.integrations.aiogram_dialog import inject


@inject
async def start_game(message: Message, widget: Button, dialog_manager: DialogManager) -> None: ...
