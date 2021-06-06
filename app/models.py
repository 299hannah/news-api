class News_Article:
    '''
    defines news article objects
    '''

    def __init__(self,title,description,url,image,published_on):
        self.title =title
        self.description = description
        self.url = url
        self.image = image
        self.published_on=published_on

class News_source:
    '''
    defines news source objects
    '''
    def __init__(self,news_id,name,description):
        self.news_id = news_id
        self.name = name
        self.description = description

