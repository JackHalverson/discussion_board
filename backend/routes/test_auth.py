from fastapi.testclient import TestClient
from unittest.mock import patch
import pytest
from datetime import datetime, timedelta
from auth import router, create_access_token, get_current_user, get_user_id
import asyncio


client = TestClient(router)


@pytest.fixture
def secret_key():
    return "test_secret_key"

@pytest.fixture
def email():
    return "jackhalverson@msn.com"

@pytest.fixture
def user_id():
    return 1

#datetime that is acociated with token
"2024-05-16 20:08:37.110913"


def test_create_access_token(email, user_id):
    timeExpire = timedelta(minutes=15)
    expected_token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqYWNraGFsdmVyc29uQG1zbi5jb20iLCJ1c2VyX2lkIjoxLCJleHAiOjE3MTU4OTE5MTd9.3kdu6ksjwJtDUE0lkL1vWyf04KqnxPu6p2kEdQ0wy0s"
    token = create_access_token(email, user_id, timeExpire)
    assert token 


def test_get_current_user():
    pass

def test_get_user_id():
    pass