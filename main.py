"""Wrap the application"""

from functions_wrapper import entrypoint  # type: ignore

from app import create_app

app_wrap = lambda request: entrypoint(create_app(), request)
