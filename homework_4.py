

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def get_owner(doc_number, documents):
    return next(
         (document['name'] for document in documents if document['number'] == doc_number),
         None
    )

def get_shelf(doc_number, directories):
    return next(
            (number for number, directory in directories.items() for doc in directory if doc == doc_number),
            None
    )

def print_doc_info(documents, directories):
    for document in documents:
        shelf_number = get_shelf(document['number'], directories)
        print(f'№: {document['number']}, тип: {document['type']}, '
              f'владелец: {document['name']}, полка хранения: {shelf_number}')

def get_shelf_list(directories):
    dir_len = len(directories)
    string = ''
    for number, item in enumerate(directories.keys()):
        string += item
        if number != dir_len - 1:
            string += ', '
    return string

def add_new_shelf(new_shelf, directories):
    if new_shelf in directories:
        return 1
    else:
        directories[new_shelf] = []
        return 0
    
def delete_shelf(shelf, directories):
    if shelf in directories:
        if directories[shelf] == []:
            del directories[shelf]
            return 0
        else:
            return 1
    else:
        return -1
    
def add_new_doc(doc_number, doc_type, doc_name, shelf, documents, directories):
    if shelf not in directories:
        return 1
    else:
        new_doc = {'type': doc_type, 'number': doc_number, 'name': doc_name}
        documents.append(new_doc)
        directories[shelf].append(doc_number)
        return 0
    

def delete_doc(number, documents, directories):
    for document in documents:
        if document['number'] == number:
            documents.remove(document)
            break
    else:
        return 1
    directories[get_shelf(number, directories)].remove(number)
    return 0

def move_doc(number, shelf, directories):
        old_shelf = get_shelf(number, directories)
        if old_shelf is None:
            return 1
        if shelf not in directories:
            return -1
        directories[old_shelf].remove(number)
        directories[shelf].append(number)
        return 0
        
        
        

    


def main():
    documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
    ]

    directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
    }
    

    print('ДОБРО ПОЖАЛОВАТЬ')
    while True:
        command = input('Введите команду: ')
        match command:

            case 'p':
                doc_number = input('Введите номер документа: ')
                owner = get_owner(doc_number, documents)
                if owner is None:
                        print('Документ не найден в базе')
                else:
                    print(f'Владелец документа: {owner}')

            case 's':
                doc_number = input('Введите номер документа: ')
                shelf_number = get_shelf(doc_number, directories)
                if shelf_number is None:
                        print('Документ не найден в базе')
                else:
                    print(f'Документ хранится на полке: {shelf_number}')

            case 'l':
                print_doc_info(documents, directories)

            case 'as':
                new_shelf = input('Введите номер полки: ')
                is_added = add_new_shelf(new_shelf, directories)
                if is_added == 0:
                    print(f'Полка добавлена. Текущий перечень полок: {get_shelf_list(directories)}')
                else:
                    print(f'Такая полка уже существует. Текущий перечень полок: {get_shelf_list(directories)}')

            case 'ds':
                shelf_to_delte = input('Введите номер полки: ')
                is_deleted = delete_shelf(shelf_to_delte, directories)
                if is_deleted == 0:
                    print(f'Полка удалена. Текущий перечень полок: {get_shelf_list(directories)}')
                elif is_deleted == 1:
                    print(f'на полке есть документа, удалите их перед удалением полки. '
                          f'Текущий перечень полок: {get_shelf_list(directories)}')
                else:
                    print(f'Такой полки не существует. Текущий перечень полок: {get_shelf_list(directories)}')
            
            case 'ad':
                doc_number = input('Введите номер документа:')
                doc_type = input('Введите тип документа:')
                doc_name = input('Введите владельца документа:')
                doc_shelf = input('Введите полку для хранения:')
                is_added = add_new_doc(doc_number, doc_type, doc_name, doc_shelf, documents, directories)
                if is_added == 0:
                    print('Документ добавлен.')
                else:
                    print('Такой полки не существует. Добавьте полку командой as')
                print('Текущий список документов: ')
                print_doc_info(documents, directories)
            
            case 'd':
                doc_number = input('Введите номер документа:')
                is_deleted = delete_doc(doc_number, documents, directories)
                if is_deleted == 0:
                    print('Документ удален. ')
                else:
                    print('Документ не найден в базе. ')
                print('Текущий список документов:')
                print_doc_info(documents, directories)

            case 'm':
                doc_number = input('Введите номер документа: ')
                shelf = input('Введите номер полки: ')
                is_moved = move_doc(doc_number, shelf, directories)
                if is_moved == -1:
                    print(f'Такой полки не существует. Текущий перечень полок: {get_shelf_list(directories)}')
                elif is_moved == 1:
                    print('Документ не найден в базе.')
                    print('Текущий список документов:')
                    print_doc_info(documents, directories)
                else:
                    print('Документ перемещен.')
                    print('Текущий список документов:')
                    print_doc_info(documents, directories)
            case 'q':
                break

        print('ЗАВЕШЕНИЕ РАБОТЫ')

        print('-'*30)


                

            

if __name__ == '__main__':
    main()


                  

            


