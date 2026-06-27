install:
	poetry install

run:
	poetry run uvicorn app.main:app --reload --port 8000

shell:
	poetry shell

activate:
	poetry env activate

makemigrations:
	poetry run alembic revision --autogenerate -m "$(msg)"

upgrade:
	poetry run alembic upgrade head

downgrade:
	poetry run alembic downgrade -1

db-init:
	poetry run alembic upgrade head

db-reset:
	poetry run alembic downgrade base
	poetry run alembic upgrade head

import-csv:
	poetry run python -m scripts.import_csv
default-admin:
	poetry run python -m scripts.seed_admin
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +