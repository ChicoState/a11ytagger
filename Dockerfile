FROM ghcr.io/astral-sh/uv:alpine

COPY pyproject.toml uv.lock /opt/a11ytagger/

WORKDIR /opt/a11ytagger

ENV DEBUG=False \
    UV_COMPILE_BYTECODE=1

RUN uv sync --no-dev --locked

COPY . .

EXPOSE 8080


HEALTHCHECK --interval=30s --start-period=30s --retries=3 \
  CMD curl -f http://localhost:8080 || exit 1

CMD ["uv", "run", "main.py"]
