from flask import render_template,request,redirect,url_for
from . import main
from app.main.requests import get_sources,get_articles,search_article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting sources by category
    general_sources = get_sources('general')
    business_sources = get_sources('business')
    technology_sources = get_sources('technology')
  

    title = 'Home - Welcome to The best News Website Online'

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('main.search',article_name = search_article))
    else:
        return render_template('index.html', title = title, general = general_sources, technology = technology_sources)

@main.route('/articles/<source>')
def articles(source):
    '''
    View articles for a specific source page function that returns the article details page and its data
    '''
    articles = get_articles(source)

    return render_template('article.html', articles = articles)

    return render_template('index.html', name = name, sources=news_sources)
