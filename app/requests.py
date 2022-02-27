from unicodedata import category
from app.main import app
import urllib.request,json
from .models import news
News=news.News

# News = news.News
# Getting api key
api_key = app.config['NEWS_API_KEY']
base_url=app.config['BASE_URL']

# Getting the news base url

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results
def process_results(news_list):
    '''
     Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

     Returns     Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

     Returns :
       news_results: A list of news objects
     '''
    news_results = []
    for news_item in news_list:
     

          id=news_item.get('id')
          description=news_item.get('description')
          url=news_item.get('url')
          name=news_item.get('name')
          category=news_item.get('category')
          news_object=News(id,description,url,name,category)
          news_results.append(news_object)
    return news_results



def get_articles(id):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
        
          
            id=news_details_response.get('id')
            description=news_details_response.get('description')
            url=news_details_response.get('url')
            name=news_details_response.get('name')
            category=news_details_response.get('category')
        
            news_object =News(id,description,url,name,category)

    return news_object
