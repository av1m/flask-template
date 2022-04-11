# Flask template

This repository is a template for a simple flask project.
It does not use much blueprint by default because it wants to be light and fast.

This project allows you to deploy the application directly to a WSGI server (for example)
The [main.py](./main.py) file allows you to deploy on a serverless service such as Google Cloud Functions, Azure Functions or Amazon Lambda.

## Get started 🎉

Clone this project

```bash
git clone https://github.com/av1m/flask-template.git
```

Install the dependencies

```bash
make install
```

Run the app

```bash
make run
```

To begin, edit the file [main.py](./app/main.py)

## Test

You can write tests in the directory [tests](./tests)

In order to test your code, you can run the following command

```bash
make test
```

## Format

The code is formatted using [black](https://black.readthedocs.io/en/stable/) and [isort](https://isort.readthedocs.io/en/stable/).

To format the code, run the following command

```bash
make format
```
