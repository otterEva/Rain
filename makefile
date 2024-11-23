format:
	@echo "formatting..."
	poetry run ruff format app

types:
	@echo "checking types..."
	poetry run mypy --explicit-package-bases app/

migration:
	@echo "creating migration..."
	alembic revision --autogenerate -m "migration"

start:
	@echo "starting app..."
	poetry run python cli.py api