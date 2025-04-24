from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    main_menu: Main_menu
    lang: Lang
    common: Common
    game: Game


class Main_menu:
    @staticmethod
    def start_message() -> Literal["""&lt;b&gt;The main menu of the bot.&lt;/b&gt;"""]: ...

    @staticmethod
    def start_game_message() -> Literal["""Play"""]: ...


class Lang:
    @staticmethod
    def ru() -> Literal["""🇷🇺 Русский"""]: ...

    @staticmethod
    def en() -> Literal["""🇬🇧 English"""]: ...


class Common:
    @staticmethod
    def back_message() -> Literal["""Back"""]: ...


class Game:
    @staticmethod
    def choose_mode_message() -> Literal["""&lt;b&gt;Choose game mode:&lt;/b&gt;"""]: ...

    @staticmethod
    def with_bot_message() -> Literal["""🤖 Play with bot"""]: ...

    @staticmethod
    def with_player_message() -> Literal["""👤 Play with another player"""]: ...

    @staticmethod
    def bot_choose_side_message() -> Literal["""&lt;b&gt;Choose your side:&lt;/b&gt;"""]: ...

    @staticmethod
    def bot_choose_white_message() -> Literal["""⚪ White"""]: ...

    @staticmethod
    def bot_choose_black_message() -> Literal["""⚫ Black"""]: ...

    @staticmethod
    def bot_choose_random_message() -> Literal["""🎲 Random"""]: ...

