from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Back, Button, Cancel, Row, SwitchTo
from aiogram_dialog.widgets.text import Format

from bot.handling.dialogs.game.getters import (
    bot_game_side_getter,
    choose_mode_getter,
    game_common_getter,
)
from bot.handling.states import GameSG

dialog = Dialog(
    Window(
        Format("{game_choose_mode_message}"),
        SwitchTo(text=Format("{game_with_bot}"), id="bot_game", state=GameSG.bot_game_side),
        SwitchTo(text=Format("{game_with_player}"), id="player_game", state=GameSG.player_game),
        Cancel(text=Format("{back_message}"), id="cancel"),
        getter=choose_mode_getter,
        state=GameSG.choose_mode,
    ),
    Window(
        Format("{game_bot_choose_side}"),
        Row(
            Button(text=Format("{game_bot_choose_white}"), id="white"),
            Button(text=Format("{game_bot_choose_black}"), id="black"),
        ),
        Button(text=Format("{game_bot_choose_random}"), id="random"),
        Back(text=Format("{back_message}")),
        getter=bot_game_side_getter,
        state=GameSG.bot_game_side,
    ),
    getter=game_common_getter,
)
