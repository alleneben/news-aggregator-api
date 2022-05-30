# app/auth/auth_basic.py

from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic
import secrets
import configparser


# Read config file from environment
config_parser = configparser.ConfigParser()
config_parser.read("cfg.ini")

security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, config_parser["configurations"]['USERNAME'])
    correct_password = secrets.compare_digest(credentials.password, config_parser["configurations"]['PASSWORD'])
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username