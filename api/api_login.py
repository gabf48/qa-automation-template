import requests
import os

BASE_API_URL = "https://reqres.in/api"

def api_login(email: str, password: str):
    """Login via API"""
    response = requests.post(f"{BASE_API_URL}/login", json={
        "email": email,
        "password": password
    })
    return response