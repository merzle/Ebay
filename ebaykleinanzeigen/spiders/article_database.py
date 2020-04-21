import json
from os import path

articles_database_file_name = "articles.txt"


def create_article_json(article_number):
    my_article = {
        'number': article_number
    }
    return my_article


def check_article_number(article_number):
    if path.exists(articles_database_file_name):
        with open(articles_database_file_name) as json_file:
            articles = json.load(json_file)
            for number_of_article in articles['articles']:
                if number_of_article["number"] == article_number:
                    return True
    return False


def save_article(new_article):
    if path.exists(articles_database_file_name):
        with open(articles_database_file_name) as json_file:
            articles = json.load(json_file)
            articles["articles"].append(new_article)
            with open(articles_database_file_name, 'w') as outfile:
                json.dump(articles, outfile)

    else:
        with open(articles_database_file_name, 'w') as outfile:
            articles = {'articles': []}
            articles['articles'].append(new_article)
            json.dump(articles, outfile)
