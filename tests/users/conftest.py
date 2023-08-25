import pytest
from time import time
from uuid import uuid4


@pytest.fixture
def generate_user():
    return {"id": str(uuid4()), "login": f"user_{time()}@reuters.com", "password": "2343f43r3"}


@pytest.fixture
def add_user(generate_user):
    print("\nadd user to system under test")
    yield generate_user
    print("\nremove user from system under test")


@pytest.fixture
def db_connection(scope="session"):
    print("db_connected")
    yield "db_resource"
    print("close db connection")
