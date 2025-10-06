FROM ghcr.io/astral-sh/uv:debian-slim

COPY pyproject.toml uv.lock /opt/a11ytagger/

WORKDIR /opt/a11ytagger

RUN uv sync --no-dev --locked

COPY . .

EXPOSE 8080

ENV DEBUG=False

HEALTHCHECK --interval=30s --start-period=30s --retries=3 \
  CMD curl -f http://localhost:8080 || exit 1

CMD ["uv", "run", "main.py"]
