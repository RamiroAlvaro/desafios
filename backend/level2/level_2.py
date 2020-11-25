from backend.common_level import read, write, articles_id_price, delivery_fees_range_prices, delivery_price, \
    output_process

data = read('data.json')
articles = data['articles']
carts = data['carts']
delivery_fees = data['delivery_fees']

dict_articles_price = articles_id_price(articles)
dict_delivery_fees_range_prices = delivery_fees_range_prices(delivery_fees)

result = output_process(carts,
                        dict_articles_price,
                        dict_delivery_fees_range_prices=dict_delivery_fees_range_prices,
                        flag=True
                        )

write('output_result.json', result)

assert read('output_result.json') == read('output.json')
