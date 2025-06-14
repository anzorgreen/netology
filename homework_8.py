import requests
from exchange import Rate
# assignment 1

def get_max_rate():
    currency_dict = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']
    max_currency = 0
    name = ''
    for value in currency_dict.values():
        if value['Value'] > max_currency:
            max_currency = value['Value']
            name = value['Name']

    return name


# assignment 2


# Только узнал, что когда мы здесь вызываем  eur(), то питон ищет сначала в дочернем класса, не находит, затем идёт к 
# родителю, находит там. Затем внутри eur() видит вызов self.make_format(), и уже его Питон опять начинает искать
# именно в дочернем классе, то есть self всегода относится к объекту ИЗ КОТОРОГО происходит поиск. Круто!
class CustomRate(Rate):
    def __init__(self, diff, format='value'):
        super().__init__(format)
        self.diff = diff

    
    def make_format(self, currency):
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                return response[currency]
            
            if self.format == 'value':
                if not self.diff:
                    return response[currency]['Value']
                else: 
                    return response[currency]['Value'] - response[currency]['Previous']
        return 'Error'


# assignment 3

class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        
        self.grade = 1
    
    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1
    
    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)
    
    def check_if_it_is_time_for_upgrade(self):
        pass

class Developer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)
    
    def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все разработчики проходят аккредитацию
        self.seniority += 1
        
        # условие повышения сотрудника из презентации
        if self.seniority % 5 == 0:
            self.grade_up()
        
        # публикация результатов
        return self.publish_grade()
    

# assignment 3

# Сори, я вообще не вкуриваю, что от меня хотят...
# Но надеюсь, хотя бы в правильном направлении...

class Designer(Employee):
    def __init__(self, name, seniority=2):
        super().__init__(name, seniority)
        self.grade = 1

    def receiving_international_reward(self):
        self.seniority += 2


    def check_if_it_is_time_for_upgrade(self):
        self.seniority += 1
        if self.seniority % 5 == 0:
            self.grade_up()
        return self.publish_grade()

    


    
