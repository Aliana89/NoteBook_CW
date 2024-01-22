import json
import datetime

def create_note():
    note_id = input("Введите id заметки: ")
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    
    return note

def save_note(note, notebook):
    notes = []
    try:
        with open(notebook, 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        pass
    notes.append(note)
    with open(notebook, 'w') as file:
        json.dump(notes, file)


def read_notes(notebook):
    notes = []
    
    try:
        with open(notebook, 'r') as file:
            notes = json.load(file)
            
        for note in notes:
            print("ID: ", note["id"])
            print("Заголовок: ", note["title"])
            print("Текст: ", note["body"])
            print("Дата/Время: ", note["timestamp"])
            print("-----")
    except FileNotFoundError:
        print("Файл с заметками не найден.")

def show_note(notebook, note_id):
    try:
        with open(notebook, 'r') as file:
            notes = json.load(file)
        
        for note in notes:
            if note["id"] == note_id:
                print("id: ", note["id"])
                print("заголовок: ", note["title"])
                print("текст: ", note["body"])
                print("дата/время: ", note["timestamp"])
                print("-----")
                break
        else:
            print("Заметка с таким id не найдена.")
    except FileNotFoundError:
        print("Файл с заметками не найден.")

def select_notes_by_date(notebook, date):
    notes = []
    
    try:
        with open(notebook, 'r') as file:
            notes = json.load(file)
        
        selected_notes = [note for note in notes if note["timestamp"].startswith(date)]
        
        if len(selected_notes) == 0:
            print("Заметки с такой датой не найдены.")
        else:
            for note in selected_notes:
                print("id: ", note["id"])
                print("заголовок: ", note["title"])
                print("текст: ", note["body"])
                print("дата/время: ", note["timestamp"])
                print("-----")
    except FileNotFoundError:
        print("Файл с заметками не найден.")        


def edit_note(notebook):
    note_id = input("Введите идентификатор заметки для редактирования: ")
    
    try:
        with open(notebook, 'r') as file:
            notes = json.load(file)
            
        for note in notes:
            if note["id"] == note_id:
                print("Редактирование заметки с ID ", note_id)
                new_title = input("Введите новый заголовок: ")
                new_body = input("Введите новый текст: ")
                note["title"] = new_title
                note["body"] = new_body
                note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break
        else:
            print("Заметка с таким ID не найдена.")
            return
        
        with open(notebook, 'w') as file:
            json.dump(notes, file)
            
        print("Заметка успешно отредактирована.")
    except FileNotFoundError:
        print("Файл с заметками не найден.")


def delete_note(notebook):
    note_id = input("Введите идентификатор заметки для удаления: ")
    
    try:
        with open(notebook, 'r') as file:
            notes = json.load(file)
            
        for note in notes:
            if note["id"] == note_id:
                notes.remove(note)
                break
        else:
            print("Заметка с таким ID не найдена.")
            return
        
        with open(notebook, 'w') as file:
            json.dump(notes, file)
            
        print("Заметка успешно удалена.")
    except FileNotFoundError:
        print("Файл с заметками не найден.")


def main():
    notebook = "notes.json"  # имя файла для сохранения заметок
    
    while True:
        print("1. Создать новую заметку")
        print("2. Показать список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выбрать заметки по дате")
        print("6. Показать выбранную запись")
        print("7. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            note = create_note()
            save_note(note, notebook)
            print("Заметка успешно создана и сохранена.")
        elif choice == "2":
            read_notes(notebook)
        elif choice == "3":
            edit_note(notebook)
        elif choice == "4":
            delete_note(notebook)
        elif choice == "5":
            date = input("Введите дату (в формате %y-%m-%d): ")
            select_notes_by_date(notebook, date)
        elif choice == "6":
            note_id = input("Введите идентификатор записи: ")
            show_note(notebook, note_id)
        elif choice == "7":
            break
        else:
            print("Неверный выбор. попробуйте еще раз.")



if __name__ == "__main__":
    main() #Вызов
