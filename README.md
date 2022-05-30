# News Aggregator API

### Description
This is a [**FastAPI**](https://github.com/tiangolo/fastapi) project that aggregates data from [**News API**](https://newsapi.org/ "News API") and [**Reddit**](https://www.reddit.com/dev/api/ "Reddit").

## Requirements
- [**python3**](https://www.python.org/)
- [**pip3**](https://pip.pypa.io/en/stable/)

## Installation Guidelines
1. Install python virtaul environment if you dont have by running ```sudo pip3 install virtualenv``` on a Linux or Mac
2. Clone this repository by running ```git clone https://github.com/alleneben/news-aggregator-api.git```
3. Change directory into the project using ```cd news-aggregator-api```
4. Run ```virtualenv env``` in the project root directory to create the virtaul environment
5. Activate the environment by running ```source env/bin/activate```
6. Create a ```cfg.ini``` file in the project root directory
7. Copy and paste the content of ```cfg_default.ini``` into ```cfg.ini``` and save the changes
8. Add your ```USERNAME``` and ```PASSWORD```
9. Visit [**News API**](https://newsapi.org/ "News API") and generate an API Key
10. Copy and paste the generated API Key into ```cfg.ini``` as the value for```NEWSAPI_API_KEY``` and save the changes
11. In the project root directory run ```pip3 install -r requirements.txt``` to install all dependencies for the application
12. Finally run ```python3 main.py```
13. Visit [**http://127.0.0.1:8000/docs**](http://127.0.0.1:8000/docs)


## API Usage
This api uses the [**HTTP Basic Auth**](https://www.blitter.se/utils/basic-authentication-header-generator/) i.e. a base64-encoded username:password string for authentication.

### Using CURL to test
- Without a search query

Request
```curl -X 'GET' \ 
  'http://127.0.0.1:8000/news' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic YWxsZW5lYmVuOmZhJHRAcDE='
```

Respoonse
```
{
  "data": [
    {
      "headline": "Over the 24 hours since the Uvalde massacre, Fox News has proposed at least 50 \"solutions\" and none of them are gun control.",
      "link": "https://v.redd.it/s50wxsq3cr191",
      "source": "reddit"
    },
    {
      "headline": "The Best Games Have the Smartest Learning Curves",
      "link": "https://www.wired.com/story/video-games-learning-curves/",
      "source": "newsapi"
    }
  ],
  "errors": ""
}
```

- With a search query

Request
```curl -X 'GET' \
  'http://127.0.0.1:8000/news?query=NBA' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic YWxsZW5lYmVuOmZhJHRAcDE='
```

Response
{
  "data": [
    {
      "headline": "[Charania] Sources: 76ers All-NBA star Joel Embiid suffered a right orbital fracture and mild concussion in series-clinching Game 6 win last night in Toronto. He will be listed as out and there is no timetable for his return.",
      "link": "https://twitter.com/ShamsCharania/status/1520202128253493255",
      "source": "reddit"
    },
    {
      "headline": "Former Michigan State F Adreian Payne dead at 31 - Reuters",
      "link": "https://www.reuters.com/lifestyle/sports/former-michigan-state-f-adreian-payne-dead-31-2022-05-09/",
      "source": "newsapi"
    }
  ],
  "errors": ""
}