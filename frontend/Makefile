.PHONY: help install dev build docker-build docker-run clean lint

# Default target - show help
help:
	@echo "Available targets:"
	@echo "  install       - Install dependencies with yarn"
	@echo "  dev           - Run Vite development server"
	@echo "  build         - Build production bundle"
	@echo "  lint          - Run ESLint"
	@echo "  docker-build  - Build Docker image"
	@echo "  docker-run    - Run Docker container"
	@echo "  clean         - Clean up build files and cache"

# Install dependencies with yarn
install:
	yarn install --frozen-lockfile

# Run Vite development server
dev:
	yarn dev

# Build production bundle
build:
	yarn build

# Run ESLint
lint:
	yarn lint

# Build Docker image
docker-build:
	docker build -t a11ytagger-frontend .

# Run Docker container
docker-run: docker-build
	docker run --rm -it -p 8080:80 a11ytagger-frontend

# Clean up build files and cache
clean:
	rm -rf dist
	rm -rf node_modules/.vite
	rm -rf node_modules/.tmp
	find . -type f -name ".DS_Store" -delete 2>/dev/null || true
