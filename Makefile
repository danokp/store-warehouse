MANAGE := poetry run python3 manage.py

runserver:
	@$(MANAGE) runserver