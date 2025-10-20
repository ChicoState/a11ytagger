.PHONY: help install sync run migrate makemigrations shell build docker-build docker-run clean

# Default target - show help
help:
	@echo "Available targets:"
	@echo "  install       - Sync dependencies with uv"
	@echo "  run           - Run Django development server"
	@echo "  migrate       - Run Django migrations"
	@echo "  makemigrations - Create new migrations"
	@echo "  shell         - Open Django shell"
	@echo "  build         - Build Docker image"
	@echo "  docker-run    - Run Docker container"
	@echo "  clean         - Clean up cache files"

# Install dependencies with uv
install:
	uv sync --frozen

# Run Django development server
run:
	uv run python manage.py runserver 8080

# Run Django migrations
migrate:
	uv run python manage.py migrate

# Create new migrations
makemigrations:
	uv run python manage.py makemigrations

# Open Django shell
shell:
	uv run python manage.py shell

# Build Docker image
build: docker-build

docker-build:
	docker build -t a11ytagger .

# Run Docker container
docker-run: docker-build
	docker run --rm -it -p 8080:8080 a11ytagger

# Clean up cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name ".DS_Store" -delete 2>/dev/null || true
