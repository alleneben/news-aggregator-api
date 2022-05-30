import configparser




# Read environment variables from cfg file
config_parser = configparser.ConfigParser()
config_parser.read("cfg.ini")


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


