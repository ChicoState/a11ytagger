# a11ytagger

A Django application for accessibility tagging.

## Prerequisites

Before getting started, ensure you have the following tools installed:

- [uv](https://github.com/astral-sh/uv) - Python package and project manager
  - Install: https://docs.astral.sh/uv/ (or `pip install uv` for basic usage)
- [Docker](https://www.docker.com/) - For containerized deployment
- Node.js / npm (for the frontend)

## Getting Started

This project uses a Makefile to simplify common development tasks. All project interactions can be done through make targets.

### Setup

Install project dependencies:
```bash
make install
```

### Development

#### Frontend (React)

The UI is in the `frontend/` directory and runs separately during development.

```bash
cd frontend
npm install
npm run dev
```

The frontend runs on http://localhost:8080 by default.

#### Backend (Django)

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

## API Proxy Configuration (Important)

The frontend uses a Vite proxy for `/api` requests (configured in
`frontend/vite.config.ts`).

By default, the proxy target is:
```ts
target: 'http://localhost:3000'
```

If you are running the Django development server locally (default port **8000**),
you must either:

- Update the proxy target to:
  ```ts
  target: 'http://localhost:8000'
  ```
- OR run the backend on port 3000 to match the existing proxy configuration.

## Troubleshooting

- **Upload error: `Unexpected end of JSON input`**  
  This usually indicates a mismatch between the frontend `/api` proxy target
  and the backend server port, or that the backend returned a non-JSON error response.


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