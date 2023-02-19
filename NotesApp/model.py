from tabulate import tabulate
import csv
import time
from datetime import datetime

def open_all_notes():
    notes = []
    with open('notes.csv', 'r', encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            try:
                title = row[1][:30] + '\n' + \
                    row[1][30:] if len(row[1]) > 30 else row[1]
                body = row[2][:30] + '\n' + \
                    row[2][30:] if len(row[2]) > 30 else row[2]
                creation_time = row[3] if row[3] else ''
                change_time = row[4] if row[4] else ''
                notes.append([row[0], title, body, creation_time, change_time])
            except IndexError:
                notes.append(['', '', '', '', ''])
    print(tabulate(notes, headers=['ID', 'Заголовок', 'Описание заметки',
          'Дата/время создания', 'Дата/время изменения'], tablefmt="fancy_grid", stralign="center"))

def get_next_id():
    with open("notes.csv", "r", encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=';')
        ids = [int(row[0].replace('.', '')) for row in reader if row]
        return max(ids) + 1 if ids else 1

def adding_notes(title, body):
    id = get_next_id()
    creation_time = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
    with open("notes.csv", "a", encoding='UTF-8', newline='') as file:
        saving_data = csv.writer(file, delimiter=';')
        saving_data.writerow([id, title, body, creation_time, ''])

def editing_notes(id, title, body):
    notes = []
    with open("notes.csv", "r", encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if int(row[0]) == id:
              if title is not None:
                row[1] = title
              if body is not None:
                row[2] = body
              row[4] = time.ctime()
            notes.append(row)
    
    with open("notes.csv", "w", encoding='UTF-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(notes)

def delete_note(id_to_delete):
    notes = []
    with open("notes.csv", "r", encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if int(row[0]) != id_to_delete:
                notes.append(row)
    with open("notes.csv", "w", encoding='UTF-8', newline='') as file:
        saving_data = csv.writer(file, delimiter=";")
        saving_data.writerows(notes)

def selection_of_notes_by_date(date):
  result = []
  with open("notes.csv", "r", encoding='UTF-8') as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
      add_date = datetime.strptime(row[3], '%a %b %d %H:%M:%S %Y')
      if add_date.strftime("%d.%m.%Y") == date:
        result.append(row)
  return result

def handle_main_menu_choice(choice):
    if choice == 2:
        print("Вы завершили работу в приложении!")
        exit()