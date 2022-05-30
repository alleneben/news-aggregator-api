from fastapi import FastAPI, Depends
import configparser

from .service.service import Service
from .apisources.sources import sources
from .auth.auth_basic import get_current_username


# Read environment variables from cfg file
config_parser = configparser.ConfigParser()
config_parser.read("cfg.ini")


# instantiate FastAPI
app = FastAPI()



# Instantiate DataSource class
data_service = Service(config_parser["configurations"], sources)



# Search news
@app.get("/news", dependencies=[Depends(get_current_username)],tags=["search news"])
def get_news(query: str = None):
    try:
        # Call the fetch_data method passing the search word
        data = data_service.fetch_data(f"{query}")
        return data
    except Exception as e:
        return { "error": str(e) }