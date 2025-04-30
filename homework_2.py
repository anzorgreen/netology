import re


# Task 1

def get_middle_from_string(word):
    middle = len(word) // 2
    if len(word) % 2 == 0 and len(word) >= 2:
        print(word[middle-1] + word[middle])
    elif len(word) % 2 != 0 and len(word) >= 1:
        print(word[middle])
    else:
        print('Введите непустую строку')

# Task 2


def sum_numbers_from_input():
    counter = 0
    while True:
        number = int(input('Введите ваше число: '))
        counter += number
        if number == 0:
            print(f'Сумма всех введённых вами чисел равна: {counter}')

# Task 3


def mvp_dating_app(set_1, set_2):
    if len(set_1) != len(set_2):
        print('Внимание, кто-то может остаться без пары!')
    else:
        print('Идеальные пары:')
        for i in range(len(set_1)):
            print(f'{set_1[i]} и {set_2[i]}')


# Task 4

def get_average_temperature_in_countries(countries):
    for country in countries:
        country_name = country[0]
        average_temperature_in_F = 0
        for temperatue in country[1]:
            average_temperature_in_F += temperatue
        average_temperature_in_F /= len(country[1])
        average_temperature_in_C = (average_temperature_in_F - 32) / 1.8
        print(f'{country_name} - {average_temperature_in_C:.1f} C')

# Task 5


def check_car_ids(car_ids):
    pattern = (r"^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$")
    for car_id in car_ids:
        is_valid = re.match(pattern, car_id)
        if is_valid:
            print(f'Номер {car_id[:6]} валиден. Регион: {car_id[6:]}')
        else:
            print(f'Номер {car_id} не валиден')


# Task 5

def get_average_views(stream):
    uniqe_users = set()
    views = 0
    pattern = r'(user\d{0,})\,(\d{4}-\d{2}-\d{2});(\d{1,})'
    for item in stream:
        found = re.search(pattern, item)
        uniqe_users.add(found.group(1))
        views += int(found.group(3))
    average_vies = views / len(uniqe_users)
    print(
        'Среднее количество просмотров'
        f'на уникального пользователя: {average_vies}'
    )