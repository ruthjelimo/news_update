from flask import render_template
from app import app
from .requests import get_news,get_articles
from .requests import get_news,get_articles,search_news
from flask import render_template,request,redirect,url_for


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    tech_news = get_news('technology')
    business_news = get_news('business')
    sports_news = get_news('sports')
    title = 'Home - Welcome to The best News Review Website Online'
    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
       return render_template('index.html', title=title,tech_news=tech_news,business_news=business_news,sports_news=sports_news)

@app.route('/news/<string:id>')
def news(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'

    return render_template('news.html',title = title,news = news)
@app.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)