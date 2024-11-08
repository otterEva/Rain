format:
	@echo "formatting..."
	poetry run ruff format app

types:
	@echo "checking types..."
	poetry run mypy app

migration:
	@echo "creating migration..."
	alembic revision --autogenerate -m "migration"