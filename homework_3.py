from decimal import Decimal
# task 1

def get_unique_tags(ids):
    return {tag for tags in ids.values() for tag in tags}

# task 2

def get_word_stats(queries):
    total_len = len(queries)
    stats = dict()
    for i in range(total_len):
        current_length = len(queries[i].split())
        stats[current_length] = stats.get(current_length, 0) + 1
    result = []
    for amount, frequence in stats.items():
        pr_frequence = frequence/total_len * 100
        result.append(f'Поисковых запросов, содержащих {amount} слов(а): {pr_frequence:.2f}%')
    result = sorted(result)
    return '\n'.join(result)

# task 3

def get_roi(results):
    for organisation in results.keys():
        results[organisation].update({'roi' : round(((results[organisation]['revenue']/results[organisation]['cost'])-1)*100, 2)})

    return results

# task 4

def get_max_sales(stats):
    max_sales = 0
    winner = ''
    for organisation, sales in stats.items():
        if sales > max_sales:
            max_sales = sales
            winner = organisation
    return f'Максимальный объем продаж на рекламном канале: {winner}'


# task 5

def get_nested(data):
    if len(data) == 1:
        return data[0]
    else:
        return {data[0]: get_nested(data[1:])}

# task 6

def get_ingridient_list(data):
    portions = int(input('Введите количество порций:'))
    ingredient_dict = dict()
    for dish in data:
        for ingredient in data[dish]:
            current_item = (ingredient['ingridient_name'], ingredient['measure'])
            ingredient_dict[current_item] = ingredient_dict.get(current_item, 0) + (ingredient['quantity'] * portions)
    result = []
    for item, quantity in ingredient_dict.items():
        name, measure = item
        name = name.title()
        result.append(f'{name}: {quantity} {measure}')
    return '\n'.join(result)