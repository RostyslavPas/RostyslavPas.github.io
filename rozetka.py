import requests

headers = {
    'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    'origin': 'https://rozetka.com.ua'
}

params = {
    'front-type': 'xl',
    'country': 'UA',
    'lang': 'ru',
    'text': 'холодильник',
}
response = requests.get(
    'https://search.rozetka.com.ua/search/api/v6/autocomplete/',
    params=params, headers=headers)
assert response.status_code == 200
entity_search = response.json()
second_element = entity_search['data']['content']['records']['words_additions'][1]['href']
print(second_element)
