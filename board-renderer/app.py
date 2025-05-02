import orjson, os
import chess, chess.svg, cairosvg, uvloop
from faststream.nats import NatsBroker, NatsMessage
from faststream import FastStream

uvloop.install()
NATS_URL = os.getenv("NATS_URL", "nats://localhost:4222")

broker = NatsBroker(f"{NATS_URL}")
app = FastStream(broker)

@broker.subscriber("board.render.req", queue="board.render")
async def render_handler(msg: NatsMessage) -> None:
    try:
        data = orjson.loads(msg.body)
        fen  = data["fen"]
        size = int(data.get("size", 400))
        orientation = data.get("orientation", "white")

        board = chess.Board(fen)
        svg_bytes = chess.svg.board(
            board,
            size=size,
            orientation=orientation,
        ).encode()
        png_bytes = cairosvg.svg2png(bytestring=svg_bytes)

        if msg.reply_to:
            await broker.publish(png_bytes, subject=msg.reply_to)
    except Exception as exc:
        if msg.reply_to:
            await broker.publish(str(exc).encode(), subject=msg.reply_to)