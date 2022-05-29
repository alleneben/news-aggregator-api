from fastapi import FastAPI
import configparser
from datasource.DataSource import DataSource

# Read environment variables from cfg file
config_parser = configparser.ConfigParser()
config_parser.read("cfg.ini")


# instantiate FastAPI
app = FastAPI()

# Sources for fetching data
sources = [
    { 
        "name":"reddit",
        "url": config_parser["configurations"]["REDDIT_URL"],
        "headers":{
            "User-Agent": "Chrome",
            "Content-Type": "application/json"
        } 
    }, 
    {
        "name":"newsapi",
        "url": config_parser["configurations"]["NEWSAPI_URL"], 
        "headers":{}
    }
]

# Instantiate DataSource class
data_source = DataSource(config_parser["configurations"], sources)


# Create a get http method with FastAPI instance
# TODO: Secure this route
@app.get("/news")
def get_news(query: str = None):
    try:
        # Call the fetch_data method passing the search word
        data = data_source.fetch_data(f"{query}")
        return data

    except Exception as e:
        return { "error": str(e) }