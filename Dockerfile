FROM ghcr.io/astral-sh/uv:debian-slim

COPY pyproject.toml uv.lock /opt/a11ytagger/

WORKDIR /opt/a11ytagger/

RUN uv sync --no-dev --locked

COPY . .

EXPOSE 80

CMD ["uv", "run", "gunicorn", "server:app", "-b [::]:80"]
