from backend.common_level import read, write, articles_id_price, discounted_items, delivery_price, \
    delivery_fees_range_prices

data = read('data.json')
articles = data['articles']
carts = data['carts']
delivery_fees = data['delivery_fees']
discounts = data['discounts']

dict_articles_price = articles_id_price(articles)
discounted_items(discounts, dict_articles_price)
dict_delivery_fees_range_prices = delivery_fees_range_prices(delivery_fees)

dict_partial_result = {}
total = 0
result = []

for item in carts:
    for products in item['items']:
        article_id = products['article_id']
        total += dict_articles_price[article_id] * products['quantity']
    total += delivery_price(int(total), dict_delivery_fees_range_prices)
    dict_partial_result['id'] = item['id']
    dict_partial_result['total'] = int(total)
    result.append(dict_partial_result)
    total = 0
    dict_partial_result = {}

write('output_result.json', result)

assert read('output_result.json') == read('output.json')
