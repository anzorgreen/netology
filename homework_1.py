# Задание 1


def compare_strings(str1, str2):
    if len(str1) == len(str2):
        print('Фразы равной длины')
    elif len(str1) > len(str2):
        print('Фраза 1 длиннее фразы 2')
    else:
        print('Фраза 2 длиннее фразы 1')

# Задание 2


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Високосный год')
    else:
        print('Обычный год')

# Задание 3


def get_zodiac_sign():
    day = int(input('Введите день'))
    month = input('Введите месяц').lower()
    if (month == 'декабрь' and day >= 22) or (month == 'январь' and day <= 19):
        zodiac_sign = 'Козерог'
    elif (month == 'январь' and day >= 20) or (month == 'февраль' and day <= 18):
        zodiac_sign = 'Водолей'
    elif (month == 'февраль' and day >= 19) or (month == 'март' and day <= 20):
        zodiac_sign = 'Рыбы'
    elif (month == 'март' and day >= 21) or (month == 'апрель' and day <= 19):
        zodiac_sign = 'Овен'
    elif (month == 'апрель' and day >= 20) or (month == 'май' and day <= 20):
        zodiac_sign = 'Телец'
    elif (month == 'май' and day >= 21) or (month == 'июнь' and day <= 20):
        zodiac_sign = 'Близнецы'
    elif (month == 'июнь' and day >= 21) or (month == 'июль' and day <= 22):
        zodiac_sign = 'Рак'
    elif (month == 'июль' and day >= 23) or (month == 'август' and day <= 22):
        zodiac_sign = 'Лев'
    elif (month == 'август' and day >= 23) or (month == 'ентябрь' and day <= 22):
        zodiac_sign = 'Дева'
    elif (month == 'сентябрь' and day >= 23) or (month == 'октябрь' and day <= 22):
        zodiac_sign = 'Весы'
    elif (month == 'октябрь' and day >= 23) or (month == 'ноябрь' and day <= 21):
        zodiac_sign = 'Скорпион'
    elif (month == 'ноябрь' and day >= 22) or (month == 'декабрь' and day <= 21):
        zodiac_sign = 'Стрелец'
    else:
        zodiac_sign = 'Дата введена некорректно'
    print(zodiac_sign)

# Задание 4


def get_package(width, length, hight):
    if width < 0 or length < 0 or hight < 0:
        print('Неправильно указан размер')
    elif width <= 15 and length <= 15 and hight <= 15:
        print('Коробка №1')
    elif width > 200 or length > 200 or hight > 200:
        print('Упаковка для лыж')
    elif (
        width > 15 and width < 50 or
        length > 15 and length < 50 or
        hight > 15 and hight < 50
    ):
        print('Коробка №2')
    else:
        print('Коробка №3')


# Задание 5


def is_lucky_ticket(number):
    if number >= 1000000 or number < 100000:
        print('Неправильный формат номера')
    else:
        first_number = number % 10
        number //= 10
        second_number = number % 10
        number //= 10
        third_number = number % 10
        number //= 10
        fourth_number = number % 10
        number //= 10
        fifth_number = number % 10
        number //= 10
        sixth_number = number % 10
        number //= 10
        if (
            first_number + second_number + third_number ==
            fourth_number + fifth_number + sixth_number
        ):
            print('Счастливый билет')
        else:
            print('Несчастливый билет')


# Задание 6


def get_area():
    from math import pi, sqrt
    shape = input('Введите тип фигуры: ').lower()

    if shape == 'круг':
        radius = int(input('Введите радиус круга: '))
        result = 2 * pi * radius
        print(f'Площадь круга: {result:.2f}')
    elif shape == 'треугольник':
        side_a = int(input('Введите длину стороны A: '))
        side_b = int(input('Введите длину стороны B: '))
        side_c = int(input('Введите длину стороны C: '))
        if(
             side_a + side_b > side_c and
             side_a + side_c > side_b and
             side_b + side_c > side_a:
        ):
            p = (side_a + side_b + side_c) / 2
            result = sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
            print(f'Площадь треугольника: {result}')
        else:
            print('Неверно указаны стороны треугольника')
    elif shape == 'прямоугольник':
        side_a = int(input('Введите длину стороны А: '))
        side_b = int(input('Введите длину стороны B: '))
        result = side_a * side_b
        print(f'Площадь прямоугольника: {result}')
    else:
        print('Неизвестная фигура')
