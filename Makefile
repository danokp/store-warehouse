MANAGE := poetry run python3 manage.py

runserver:
	@$(MANAGE) runserver

makemigrations:
	@$(MANAGE) makemigrations

migrate: makemigrations
	@$(MANAGE) migrate

createsuperuser:
	@$(MANAGE) createsuperuser --noinput --email admin@admin.com

lint:
	poetry run flake8 store_warehouse
