FROM ghcr.io/astral-sh/uv:python3.13-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY uv.lock pyproject.toml ./

RUN uv sync --no-cache

COPY . .
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]