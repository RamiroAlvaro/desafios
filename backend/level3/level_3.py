import json
import sys

with open('data.json', 'r') as f:
    data = json.load(f)

articles = data['articles']
carts = data['carts']
delivery_fees = data['delivery_fees']
discounts = data['discounts']

dict_articles_price = {item['id']: item['price'] for item in articles}

for discount in discounts:
    id_ = discount['article_id']
    type_ = discount['type']
    value = discount['value']
    if type_ == 'amount':
        dict_articles_price[id_] -= value
    elif type_ == 'percentage':
        dict_articles_price[id_] -= (dict_articles_price[id_] * value / 100)

dict_delivery_fees_range_prices = {}

for element_dict in delivery_fees:
    max_price = element_dict['eligible_transaction_volume']['max_price']
    min_price = element_dict['eligible_transaction_volume']['min_price']
    if not max_price:
        rank = range(min_price, sys.maxsize ** 10)
    else:
        rank = range(min_price, max_price)
    dict_delivery_fees_range_prices[element_dict['price']] = rank


def delivery_price(total_price):
    for key, value in dict_delivery_fees_range_prices.items():
        if total_price in value:
            return key
    return 0


dict_partial_result = {}
total = 0
result = []

for item in carts:
    for products in item['items']:
        article_id = products['article_id']
        total += dict_articles_price[article_id] * products['quantity']
    total += delivery_price(int(total))
    dict_partial_result['id'] = item['id']
    dict_partial_result['total'] = int(total)
    result.append(dict_partial_result)
    total = 0
    dict_partial_result = {}

with open('output_result.json', 'w') as f:
    json.dump({'carts': result}, f)
