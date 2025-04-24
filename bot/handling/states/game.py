from aiogram.fsm.state import State, StatesGroup


class GameSG(StatesGroup):
    start_game_menu = State()
    choose_mode = State()
    bot_game = State()
    bot_game_side = State()
    player_game = State()
