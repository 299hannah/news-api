import urllib.request,json
from .models import News_Article,News_source

News_Article = News_Article
News_source = News_source

api_key =None 
news_sources_url = None

def configure_request(app):
    global api_key,news_sources_url
    #git api key
    api_key = app.config['NEWS_API_KEY']

    news_sources_url = app.config['NEWS_API_BASE_URL']

def get_sources(category):
    '''
    gets json response to url request
    '''
    get_sources_url = news_sources_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_source_results(source_results_list)

        return source_results

def process_source_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        news_id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
      

        source_object = Source(id,name,description,category,language)
        source_results.append(source_object)

    return source_results