from aiogram_dialog import Dialog

from .game import dialog as game_dialog
from .main_menu import dialog as menu_dialog


def get_dialogs() -> list[Dialog]:
    return [
        menu_dialog,
        game_dialog,
    ]


__all__ = ["get_dialogs"]
