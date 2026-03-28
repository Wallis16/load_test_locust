# ---------- BUILD STAGE ----------
FROM python:3.13-slim AS builder

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    build-essential

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY pyproject.toml uv.lock* ./

RUN uv sync --frozen --no-dev

# ---------- RUNTIME STAGE ----------
FROM python:3.13-slim

WORKDIR /app

# só runtime, sem gcc/build tools
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/.venv /app/.venv

ENV PATH="/app/.venv/bin:$PATH"

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]