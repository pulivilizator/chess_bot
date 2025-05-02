#!/bin/bash
set -e

WORKERS=${WORKERS:-2}

exec uv run -m faststream run app:app --workers "$WORKERS" 