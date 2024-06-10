import requests
from fastapi import HTTPException, status
from functools import wraps
import os

AUTH_SERVICE_URL = os.getenv('AUTH_SERVICE_URL', 'http://127.0.0.1:8000/auth')

def verifyauth(servico, capacidade):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = kwargs.get('request')
            header = kwargs.get('header')
            
            if not request:
                request = args[0]
            if not header:
                header = args[1]

            auth_data = {
                "username": header.security.username_token.username,
                "password": header.security.username_token.password,
                "service_name": servico,
                "capacity": capacidade
            }
            
            response = requests.post(AUTH_SERVICE_URL, json=auth_data)
            
            if response.status_code == 200:
                return await func(*args, **kwargs)
            elif response.status_code == 401:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")
            else:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Authentication Failed")

        return wrapper
    return decorator
