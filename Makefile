MANAGE := poetry run python3 manage.py

runserver:
	@$(MANAGE) runserver

makemigrations:
	@$(MANAGE) makemigrations

migrate: makemigrations
	@$(MANAGE) migrate

