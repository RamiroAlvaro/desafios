import json
import sys


def read(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        return data


def write(json_name, result):
    with open(json_name, 'w') as f:
        json.dump({'carts': result}, f)


def articles_id_price(articles):
    return {item['id']: item['price'] for item in articles}


def discounted_items(discounts, dict_articles_price):
    for discount in discounts:
        id_ = discount['article_id']
        type_ = discount['type']
        value = discount['value']
        if type_ == 'amount':
            dict_articles_price[id_] -= value
        elif type_ == 'percentage':
            dict_articles_price[id_] -= (dict_articles_price[id_] * value / 100)


def delivery_fees_range_prices(delivery_fees):
    dict_delivery_fees_range_prices = {}

    for element_dict in delivery_fees:
        max_price = element_dict['eligible_transaction_volume']['max_price']
        if not max_price:
            upper_bound = sys.maxsize ** 10
        else:
            upper_bound = max_price
        dict_delivery_fees_range_prices[upper_bound] = element_dict['price']
    return dict_delivery_fees_range_prices


def delivery_price(total_price, dict_delivery_fees_range_prices):
    for upper_bound, value in dict_delivery_fees_range_prices.items():
        if total_price < upper_bound:
            break
    return value


def output_process(carts, dict_articles_price, dict_delivery_fees_range_prices={}, flag=False):
    dict_partial_result = {}
    total = 0
    result = []

    for item in carts:
        for products in item['items']:
            article_id = products['article_id']
            total += dict_articles_price[article_id] * products['quantity']
        if flag:
            total += delivery_price(int(total), dict_delivery_fees_range_prices)
        dict_partial_result['id'] = item['id']
        dict_partial_result['total'] = int(total)
        result.append(dict_partial_result)
        total = 0
        dict_partial_result = {}
    return result
