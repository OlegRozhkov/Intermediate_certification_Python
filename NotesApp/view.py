import csv
from tabulate import tabulate

def open_main_menu():
  print('Приложение заметки')
  print("Открыть меню?")
  menu_list = [
    "1. Да",
    "2. Нет"
    ]
  for item in menu_list:
    print(item)

def get_user_choice():
    while True:
        try:
            choice = int(
                input("Сделайте свой выбор: "))
            if choice > 0 and choice < 3:
                return choice
            else:
                print("Неверный ввод. Пожалуйста, введите число от 1 до 2!")
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число от 1 до 2!")

def display_notes_menu():
  print("Основное меню пользователя: ")
  menu_list = [
    "1. Посмотреть все заметки",
    "2. Добавить заметку",
    "3. Редактировать заметку",
    "4. Удалить заметку",
    "5. Сделать выборку заметок по дате добавления",
    "6. Выход"
    ]
  for item in menu_list:
    print(item)

def user_choice_menu_item():
    while True:
        try:
            choice = int(
                input("Выберите действие: "))
            if choice > 0 and choice < 7:
                return choice
            else:
                print("Неверный ввод. Пожалуйста, введите число от 1 до 6!")
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число от 1 до 6!")

# Функция вывода заголовка перед открывшемся списком всех заявок
def notes_list():
  print("Список всех заметок: ")

#Функция добавления заметки
def adding_notes():
    print("Добавить заметку: ")
    header = input("Введите заголовок заметки: ")
    description = input("Введите описание заметки: ")
    print("Заметка добавлена в приложение!")
    return header, description

def edit_note(file):
    print("Редактировать заметку: ")
    try:
        id = int(input("Введите ID заметки, которую вы хотите изменить: "))
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число!")
        return None
    
    notes = []
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        notes.append(row)
      
    title = None
    body = None
    if id not in [int(note[0]) for note in notes]:
        print("Неверный ID. Такая заметка отсутствует в списке!")
        return None
    else:
        notes = [note for note in notes if int(note[0]) != id]
        title = input("Введите новый заголовок заметки (можно оставить незаполненным): ") or None
        body = input("Введите новое описание заметки (можно оставить незаполненным): ") or None
        print("Заметка отредактирована!")
    return id, title, body

def ask_delete_note(file):
    print("Удалить заметку: ")
    try:
        id_to_delete = int(input("Введите ID заметки, которую вы хотите удалить: "))
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число!!!\033[0")
        return None

    notes = []
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        notes.append(row)

    if id_to_delete not in [int(note[0]) for note in notes]:
        print("Неверный ID. Такая заметка отсутствует в списке!")
    else:
        notes = [note for note in notes if int(note[0]) != id_to_delete]
        print("Заметка успешно удалена!")
    return id_to_delete
  
def addition_date_selection():
    print("Выборка заметок по дате добавления: ")
    date_selection = input("Введите дату для поиска, формат ввода (дд.мм.гггг): ")
    return date_selection

def display_notes(result):
  print("Результат поиска: ")
  print(tabulate(result, headers=['Заголовок', 'Описание заметки',
                                  'Дата/время создания', 
                                  'Дата/время изменения'], tablefmt="fancy_grid", stralign="center"))

def application_closing():
    print("Вы завершили работу в приложении!")