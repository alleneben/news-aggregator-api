import requests

class DataSource:
    def __init__(self, config, sources):
        self.sources = sources
        self.data = []
        self.response = {"data": self.data, "errors": ""}
        self.NEWSAPI_API_KEY = config['NEWSAPI_API_KEY']

    
    def fetch_data(self, query_string):
        try:
            # Loop through all sources or apis
            for source in self.sources:
                # Check if source or api is reddit or newsapi
                if source["name"] == "reddit":
                    request =  requests.get(f"{source['url']}?q={query_string}",headers=source["headers"])
                    response_data = request.json()
                    self.transform_reddit_data(response_data["data"]["children"],source["name"])

                elif source["name"] == "newsapi":
                    request =  requests.get(f"{source['url']}?q={query_string}&apiKey={self.NEWSAPI_API_KEY}",headers=source["headers"])
                    response_data = request.json()
                    if response_data["status"] == "ok":
                        self.transform_newsapi_data(response_data["articles"],source["name"])

                else:
                    # If source or api does not exist
                    self.response["errors"]  = f"The source { source['name'] } is not defined! Please use newsapi or reddit."

            return self.response
        except Exception as e:
            return { "error": str(e) }

    
    # The method transforms reddit response data
    def transform_reddit_data(self, data, source):
        for response in data:
            self.data.append({ "headline": response["data"]["title"], "link": response["data"]["url"], "source": source })

    # The method transforms newsapi response data
    def transform_newsapi_data(self, data, source):
        for response in data:
            self.data.append({ "headline": response["title"], "link": response["url"], "source": source })

