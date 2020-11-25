from backend.common_level import read, write, articles_id_price, output_process

data = read('data.json')
articles = data['articles']
carts = data['carts']

dict_articles_price = articles_id_price(articles)

result = output_process(carts, dict_articles_price)

write('output_result.json', result)

assert read('output_result.json') == read('output.json')
