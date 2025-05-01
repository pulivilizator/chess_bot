from enum import StrEnum


class Languages(StrEnum):
    RU = "ru"
    EN = "en"

    WIDGET_KEY = "language"


class CacheLoadModules(StrEnum):
    SETTINGS = "settings"
    GAME = "game"


class ChessPieces(StrEnum):
    KING = "king"
    QUEEN = "queen"
    ROOK = "rook"
    BISHOP = "bishop"
    KNIGHT = "knight"
    PAWN = "pawn"


class Side(StrEnum):
    WHITE = "white"
    BLACK = "black"


class GameStatus(StrEnum):
    PENDING = "pending"
    ACTIVE = "active"
    FINISHED = "finished"
    CANCELLED = "cancelled"


class GameResult(StrEnum):
    PLAYER1_WIN = "player1_win"
    PLAYER2_WIN = "player2_win"
    DRAW = "draw"
    ABANDONED = "abandoned"
