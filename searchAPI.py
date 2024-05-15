import requests
import json


def auth(query):
    API_KEY = 'AIzaSyCKNfzFchCiiyYpis4DinLGgG9UU78K16c'
    SEARCH_ENGINE_ID = '4281243aff6044a03'

    # query = 'Caption by Hyatt'

    url = f'https://www.googleapis.com/customsearch/v1?key={
        API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}'
    response = requests.get(url)

    return response


brandlink = {}


def search(response):
    data = response.json()
    # print(json.dumps(data))
    brandtitle = data['items'][0]['title']
    brandurl = data['items'][0]['link']
    brandlink[brandtitle] = brandurl
    print(brandlink)
    return brandlink
