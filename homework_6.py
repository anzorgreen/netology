import re

# task 1

def get_dict(file: str) -> dict:
    result = dict()
    with open(file, 'r') as file:
        next(file)
        pattern = re.compile(r'"user_id": "([\w]{10})", "category": "(\S{1,})"')
        for line in file:
            match = re.search(pattern, line)
            if match is not None:
                result[match.group(1)] = match.group(2)
    return result

# taks 2

def create_funnel_csv(visit_file: str, purchase_file: str) -> None:
    visits = open(visit_file, 'r', encoding='utf-8')
    next(visits)
    purchases_dict = get_dict(purchase_file)
    write_file = open('funnel.csv', 'w', encoding = 'utf-8' )
    write_file.write('user_id, source, category\n')
    for line in visits:
        line = line.strip()
        user = line.split(',')[0]
        print(user)
        category = purchases_dict.get(user)
        if category:
            write_file.write(f'{line},{category}\n')
    visits.close()
    write_file.close()




        
