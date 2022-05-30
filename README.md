# News Aggregator API

### Description
This is a [**FastAPI**](https://github.com/tiangolo/fastapi) project that aggregates data from [**News API**](https://newsapi.org/ "News API") and [**Reddit**](https://www.reddit.com/dev/api/ "Reddit").

## Requirements
- python3
- pip3

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


## Running the code
