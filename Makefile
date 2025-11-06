.PHONY: help install update lock run test lint format clean docker-build docker-up docker-down migrate shell

# Default target
help:
	@echo "Available commands:"
	@echo "  make install       - Install dependencies"
	@echo "  make update        - Update dependencies and rebuild Docker"
	@echo "  make lock          - Update poetry.lock file"
	@echo "  make run           - Run development server"
	@echo "  make test          - Run tests"
	@echo "  make lint          - Run linters"
	@echo "  make format        - Format code"
	@echo "  make clean         - Clean cache and temp files"
	@echo "  make docker-build  - Build Docker images"
	@echo "  make docker-up     - Start Docker containers"
	@echo "  make docker-down   - Stop Docker containers"
	@echo "  make migrate       - Run Django migrations"
	@echo "  make shell         - Open Django shell"

# Install dependencies
install:
	poetry install

# Update dependencies and rebuild Docker
update:
	./scripts/update-dependencies.sh

# Update poetry.lock
lock:
	poetry lock --no-update

# Run development server
run:
	poetry run uvicorn core.asgi:fastapp --reload --port 8000

# Run tests
test:
	poetry run pytest

# Run tests with coverage
test-cov:
	poetry run pytest --cov=apps --cov=core --cov-report=html

# Run linters
lint:
	poetry run pylint apps/ core/

# Format code
format:
	poetry run black .
	poetry run isort .

# Format and lint
check: format lint
	poetry run python manage.py check

# Clean cache and temp files
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.log" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

# Docker commands
docker-build:
	docker-compose build

docker-up:
	docker-compose up

docker-up-d:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

docker-clean:
	docker-compose down -v
	docker system prune -f

# Django commands
migrate:
	poetry run python manage.py migrate

makemigrations:
	poetry run python manage.py makemigrations

shell:
	poetry run python manage.py shell

superuser:
	poetry run python manage.py createsuperuser

collectstatic:
	poetry run python manage.py collectstatic --noinput

# Database commands
db-reset:
	rm -f db.sqlite3
	poetry run python manage.py migrate
	poetry run python manage.py createsuperuser

# Development setup
setup: install migrate
	@echo "Setup complete! Run 'make run' to start the server"

# Full reset
reset: clean docker-clean
	rm -f poetry.lock
	rm -f db.sqlite3
	@echo "Project reset complete! Run 'make setup' to start fresh"
