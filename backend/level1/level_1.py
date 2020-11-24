import json

with open('data.json', 'r') as f:
    data = json.load(f)

articles = data['articles']
carts = data['carts']

dict_articles_price = {item['id']: item['price'] for item in articles}

dict_partial_result = {}
total = 0
result = []

for item in carts:
    for products in item['items']:
        article_id = products['article_id']
        total += dict_articles_price[article_id] * products['quantity']
    dict_partial_result['id'] = item['id']
    dict_partial_result['total'] = total
    result.append(dict_partial_result)
    total = 0
    dict_partial_result = {}

with open('output_result.json', 'w') as f:
    json.dump({'carts': result}, f)
