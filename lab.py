import pickle

# Функция для создания новой заметки
def create_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержание заметки: ")
    note = {"title": title, "content": content}
    return note

# Функция для сохранения заметки в файл
def save_note_as_json(note):
    with open("notes.json", "a") as file:
        json.dump(note, file)
        file.write("\n")

# Функция для сохранения заметки в файл в формате CSV
def save_note_as_csv(note):
    with open("notes.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([note["title"], note["content"]])

# Функция для чтения списка заметок из файла в формате CSV
def read_notes_from_csv():
    try:
        with open("notes.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print("Заголовок:", row[0])
                print("Содержание:", row[1])
                print("----------------------")
    except FileNotFoundError:
        print("Файл с заметками не найден.")

# Функция для редактирования заметки
def edit_note():
    note_index = input("Введите номер заметки, которую хотите изменить: ")
    try:
        note_index = int(note_index)
        with open("notes.json", "r+") as file:
            notes = []
            for line in file:
                note = json.loads(line)
                notes.append(note)
            if note_index >= 1 and note_index <= len(notes):
                new_title = input("Введите новый заголовок заметки: ")
                new_content = input("Введите новое содержание заметки: ")
                notes[note_index - 1]["title"] = new_title
                notes[note_index - 1]["content"] = new_content
                file.seek(0)
                file.truncate()
                for note in notes:
                    file.write(json.dumps(note) + "\n")
                print("Заметка успешно отредактирована.")
            else:
                print("Недопустимый номер заметки.")
    except ValueError:
        print("Недопустимый номер заметки.")

# Функция для удаления заметки
def delete_note():
    note_index = input("Введите номер заметки, которую хотите удалить: ")
    try:
        note_index = int(note_index)
        with open("notes.json", "r+") as file:
            notes = []
            for line in file:
                note = json.loads(line)
                notes.append(note)
            if note_index >= 1 and note_index <= len(notes):
                del notes[note_index - 1]
                file.seek(0)
                file.truncate()
                for note in notes:
                    file.write(json.dumps(note) + "\n")
                print("Заметка успешно удалена.")
            else:
                print("Недопустимый номер заметки.")
    except ValueError:
        print("Недопустимый номер заметки.")

# Главная функция программы
def main():
    while True:
        print("1. Создать новую заметку")
        print("2. Показать список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            note = create_note()
            # Выберите один из вариантов сохранения заметки
            save_note_as_json(note)
            # save_note_as_csv(note)
            print("Заметка успешно сохранена.")
        elif choice == "2":
            # Выберите один из вариантов чтения заметок
            read_notes_from_json()
            # read_notes_from_csv()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Недопустимый выбор. Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()