help: ## Display callable targets.
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install the environment
	python3 -m venv .venv
	.venv/bin/python3 -m pip install --upgrade pip wheel setuptools
	.venv/bin/python3 -m pip install --upgrade -r requirements.txt

format:  ## Format the code source
	isort --profile=black .
	black .

test:  ## Test the applicaion
	isort --profile=black --check .
	black --check .
	pytest .
	mypy .

run:  ## Run the server in dev mode
	FLASK_APP=main TYPE_ENV=development FLASK_ENV=development flask run -p 5000

run-functions-framework: ## Serve a dev server with the functions framework
	TYPE_ENV=development FLASK_ENV=development functions-framework --target=app_wrap --debug --port 5000

gunicorn: ## Run a gunicorn server in development mode
	TYPE_ENV=development FLASK_ENV=development gunicorn -b :5000 wsgi:app_wrap
