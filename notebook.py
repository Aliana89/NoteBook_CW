import datetime
import csv
while True:
    print("1. Создать новую заметку")
    print("2. Прочитать список заметок")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Найти нужную заметку")
    print("6. Выход")
    choice = input("Выберите действие (введите цифру): ")
    if choice == "1":
        create_note()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        find_number()
    elif choice == "6":    
        break
    else:
        print("Некорректный выбор. пожалуйста, повторите.")

def create_note():
    id = input("Введите идентификатор заметки: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержимое заметки: ")
    created_at = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    updated_at = created_at
    note_obj = Note(id, title, content, created_at, updated_at)
    save_note(note_obj)
    print("Заметка успешно создана и сохранена.")

class Note:
    def __init__(note, id, title, content, created_at, updated_at):
        note.id = id
        note.title = title
        note.content = content
        note.created_at = created_at
        note.updated_at = updated_at
        
def save_note(note):
    with open('notes.csv', 'a', newline='',encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([note.id, note.title, note.content, note.created_at, note.updated_at])

def search_parameters(note_obj ,id, title, content, created_at, updated_at):
    print('По какому полю выполнить поиск?')
    search_field = input('1 - id\n2 - title\n3 - content\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите id для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите title для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите content для поиска: ')
        print()
    return search_field, search_value


def find_number(note_obj):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'id', '2': 'title', '3': 'content'}
    find_note = []
    for note in note_obj:
        if note[search_value_dict[search_field]] == search_value:
            find_note.append(note)
    if len(find_note) == 0:
        print('Заметка не найдена!')
    else:
        print(find_note)
    print()
