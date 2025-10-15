# Agent Instructions

## Commands
- Install: `uv sync --frozen`
- Run dev server: `uv run python manage.py runserver 8080`
- Run all tests: `uv run python manage.py test`
- Run single test: `uv run python manage.py test server.tests.TestClassName.test_method_name`
- Migrations: `uv run python manage.py makemigrations && uv run python manage.py migrate`
- No lint/type checking configured - add before committing

## Code Style
- Python 3.13+ Django 5.2 project using uv for package management
- Imports: Standard library first, then Django, then third-party (pikepdf), then local
- Use Django class-based views (CBVs) for views
- Use Django's cache framework for temporary storage
- No type hints currently used in codebase
- Use snake_case for functions/variables, PascalCase for classes
- Error handling: Return rendered templates with error context rather than raising exceptions
- Keep views simple, use Django shortcuts (render, redirect)
- Use f-strings for string formatting
- Two blank lines between top-level functions/classes
