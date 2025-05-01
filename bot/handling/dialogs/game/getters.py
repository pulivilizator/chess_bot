from typing import TYPE_CHECKING, Any

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from i18n.stub import TranslatorRunner


async def game_common_getter(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    **kwargs: Any,
) -> dict[str, Any]:
    return {
        "back_message": i18n.common.back_message(),
    }


async def choose_mode_getter(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    **kwargs: Any,
) -> dict[str, Any]:
    return {
        "game_choose_mode_message": i18n.game.choose_mode_message(),
        "game_with_bot": i18n.game.with_bot_message(),
        "game_with_player": i18n.game.with_player_message(),
    }


async def bot_game_side_getter(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    **kwargs: Any,
) -> dict[str, Any]:
    return {
        "game_bot_choose_side": i18n.game.bot_choose_side_message(),
        "game_bot_choose_white": i18n.game.bot_choose_white_message(),
        "game_bot_choose_black": i18n.game.bot_choose_black_message(),
        "game_bot_choose_random": i18n.game.bot_choose_random_message(),
    }
