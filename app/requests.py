# from unicodedata import category
# from app.main import app
# import urllib.request,json
# from .models import news
# News=news.News

# # News = news.News
# # Getting api key
# api_key = app.config['NEWS_API_KEY']
# base_url=app.config['BASE_URL']

# # Getting the news base url

# def get_news(category):
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_news_url = base_url.format(category,api_key)

#     with urllib.request.urlopen(get_news_url) as url:
#         get_news_data = url.read()
#         get_news_response = json.loads(get_news_data)

#         news_results = None

#         if get_news_response['sources']:
#             news_results_list = get_news_response['sources']
#             news_results = process_results(news_results_list)


#     return news_results
# def process_results(news_list):
#     '''
#      Function  that processes the news result and transform them to a list of Objects

#     Args:
#         news_list: A list of dictionaries that contain movie details

#      Returns     Function  that processes the news result and transform them to a list of Objects

#     Args:
#         news_list: A list of dictionaries that contain movie details

#      Returns :
#        news_results: A list of news objects
#      '''
#     news_results = []
#     for news_item in news_list:
     

#           id=news_item.get('id')
#           description=news_item.get('description')
#           url=news_item.get('url')
#           name=news_item.get('name')
#           category=news_item.get('category')
#           news_object=News(id,description,url,name,category)
#           news_results.append(news_object)
#     return news_results



# def get_articles(id):
#     get_news_details_url = base_url.format(id,api_key)

#     with urllib.request.urlopen(get_news_details_url) as url:
#         news_details_data = url.read()
#         news_details_response = json.loads(news_details_data)

#         news_object = None
#         if news_details_response:
        
          
#             id=news_details_response.get('id')
#             description=news_details_response.get('description')
#             url=news_details_response.get('url')
#             name=news_details_response.get('name')
#             category=news_details_response.get('category')
        
#             news_object =News(id,description,url,name,category)

#     return news_object
# 

import urllib.request,json
from .models import Article, Category, Source , Headlines
# Getting api key
api_key =None
# Getting source url
source_url=None
# Getting source url
cat_url= None
def configure_request(app):
    global api_key, source_url, cat_url
    api_key =app.config['NEWS_API_KEY']
    source_url=app.config['NEWS_SOURCE_URL']
    cat_url=app.config['CAT_API_URL']
def get_source(category):
    '''
    Function that gets the json response to url request
    '''
    get_source_url= source_url.format(category, api_key)
    # print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        source_results = None
        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)
    return source_results
def process_results(source_list):
    '''
    function to process results and transform them to a list of objects
    Args:
        source_list:dictionary cotaining source details
    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        if id:
            source_object = Source(id,name,description,url)
            source_results.append(source_object)
    return source_results
def article_source(id):
    article_source_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(id,api_key)
    print(article_source_url)
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)
        article_source_results = None
        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_articles_results(article_source_list)
    return article_source_results
def process_articles_results(news):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results = []
    for article in news:
        author = article.get('author')
        description = article.get('description')
        time = article.get('publishedAt')
        url = article.get('urlToImage')
        image = article.get('url')
        title = article.get ('title')
        if url:
            article_objects = Article(author,description,time,image,url,title)
            article_source_results.append(article_objects)
    return article_source_results
def get_category(cat_name):
    '''
    function that gets the response to the category json
    '''
    get_category_url = cat_url.format(cat_name,api_key)
    print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_cartegory_response = json.loads(get_category_data)
        get_cartegory_results = None
        if get_cartegory_response['articles']:
            get_cartegory_list = get_cartegory_response['articles']
            get_cartegory_results = process_articles_results(get_cartegory_list)
    return get_cartegory_results
def get_headlines():
    '''
    function that gets the response to the category json
    '''
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    print(get_headlines_url)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)
        get_headlines_results = None
        if get_headlines_response['articles']:
            get_headlines_list = get_headlines_response['articles']
            get_headlines_results = process_articles_results(get_headlines_list)
    return get_headlines_results