import datetime

while True:
    print("1. Создать новую заметку")
    print("2. Прочитать список заметок")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выход")
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
