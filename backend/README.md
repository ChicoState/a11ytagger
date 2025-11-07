# a11ytagger

A Django application for accessibility tagging.

## Prerequisites

Before getting started, ensure you have the following tools installed:

- [uv](https://github.com/astral-sh/uv) - Python package and project manager
- [Docker](https://www.docker.com/) - For containerized deployment

## Getting Started

This project uses a Makefile to simplify common development tasks. All project interactions can be done through make targets.

### Setup

Install project dependencies:
```bash
make install
```

### Development

Run the Django development server:
```bash
make run
```

Run database migrations:
```bash
make migrate
```

Create new migrations after model changes:
```bash
make makemigrations
```

Access the Django shell:
```bash
make shell
```

### Docker

Build the Docker image:
```bash
make build
```

Run the application in a Docker container:
```bash
make docker-run
```

### Other Commands

View all available make targets:
```bash
make help
```

Clean up cache files:
```bash
make clean
```