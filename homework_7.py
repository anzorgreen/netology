from datetime import datetime, timedelta


# task 1

def datetime_from_newsletter(str: str) -> datetime:
    string = str.strip().split(' — ')
    newsletter = string[0]
    date = string[1]
    match newsletter:
        case 'The Moscow Times':
            return datetime.strptime(date, '%A, %B %d, %Y')
        case 'The Guardian':
            return datetime.strptime(date, '%A, %d.%m.%y')
        case 'Daily News':
            return datetime.strptime(date, '%A, %d %B %Y')
        

# task 2

def check_date(dates: list) -> bool:
    result = []
    for date in dates:
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError as e:
            result.append(False)
        else:
            result.append(True)
    return result

# task 3

def date_range(start_date: str, end_date: str) -> list[str]:
    result = []
    try:
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        print(start, end)
        while start <= end:
            result.append(start.strftime('%Y-%m-%d'))
            start += timedelta(days=1)
    except ValueError:
        return []

    else:
        return result
    
# task 4

#  Index out of range  означает, что мы пытаемся обратиться к коллекции по индексу,
# которого нет в коллекции. Например, my_list[3], если в списке  три элемента


DEFAULT_USER_COUNT = 3

def delete_and_return_last_user(default_list=['A100', 'A101', 'A102']):
    element_to_delete = default_list[-1]
    default_list.remove(element_to_delete)

    return default_list[DEFAULT_USER_COUNT-2]

delete_and_return_last_user(1) # удаляется последний элемент и возвращается предыдущий
# при этом len(default_list) = 2
# delete_and_return_last_user(1) # удаляется последний элемент ( теперь в списке всего один)
# И функция пытается сослаться на предыдущий. Тут возникает ошибка. 
