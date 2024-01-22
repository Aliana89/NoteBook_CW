import csv
import datetime

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

def read_notes():
    try:
        with open('notes.csv', 'r',encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                note = Note(row[0], row[1], row[2], row[3], row[4])
                print("идентификатор:", note.id)
                print("заголовок:", note.title)
                print("содержимое:", note.content)
                print("дата создания:", note.created_at)
                print("дата последнего изменения:", note.updated_at)
                print("-------------------------------")
    except FileNotFoundError:
        print("файл с заметками не найден.")

def edit_note():
    id = input("введите идентификатор заметки: ")
    with open('notes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        rows = list(reader)
    index = None
    for i, row in enumerate(rows):
        if row[0] == id:
            index = i
            break
    if index is not None:
        title = input("введите новый заголовок заметки: ")
        content = input("введите новое содержимое заметки: ")
        updated_at = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        rows[index] = [id, title, content, rows[index][3], updated_at]
        with open('notes.csv', 'w',encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(rows)
        print("заметка успешно отредактирована.")
    else:
        print("заметка с таким идентификатором не найдена.")

def delete_note():
    id = input("введите идентификатор заметки: ")
    with open('notes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        rows = list(reader)
    index = None
    for i, row in enumerate(rows):
        if row[0] == id:
            index = i
            break
    if index is not None:
        del rows[index]
        with open('notes.csv', 'w',encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(rows)
        print("заметка успешно удалена.")
    else:
        print("заметка с таким идентификатором не найдена.")

def create_note():
    id = input("введите идентификатор заметки: ")
    title = input("введите заголовок заметки: ")
    content = input("введите содержимое заметки: ")
    created_at = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    updated_at = created_at
    note_obj = Note(id, title, content, created_at, updated_at)
    save_note(note_obj)
    print("заметка успешно создана и сохранена.")

# пример использования функционала работы с заметками
while True:
    print("1. создать новую заметку")
    print("2. прочитать список заметок")
    print("3. редактировать заметку")
    print("4. удалить заметку")
    print("5. выход")
    choice = input("выберите действие (введите цифру): ")
    if choice == "1":
        create_note()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
    else:
        print("некорректный выбор. пожалуйста, повторите.")
