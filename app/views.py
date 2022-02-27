from flask import render_template
from app import app
from .requests import get_news,get_articles




@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    tech_news = get_news('technology')
    business_news = get_news('business')
    sports_news = get_news('sports')
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title=title,tech_news=tech_news,business_news=business_news,sports_news=sports_news)

@app.route('/news/<string:id>')
def news(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'

    return render_template('news.html',title = title,news = news)
