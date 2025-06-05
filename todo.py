"""
  Консольное приложение ToDo-лист
    Функционал:
    - Добавление задач
    - Удаление задач
    - Пометка задач выполненными
    - Просмотр списка задач
    Пользовательский интерфейс:
             _______  _______  ______   _______         ___      ___   _______  _______
            |       ||       ||      | |       |       |   |    |   | |       ||       |
            |_     _||   _   ||  _    ||   _   |       |   |    |   | |  _____||_     _|
              |   |  |  | |  || | |   ||  | |  |       |   |    |   | | |_____   |   |
              |   |  |  |_|  || |_|   ||  |_|  |       |   |___ |   | |_____  |  |   |
              |   |  |       ||       ||       |       |       ||   |  _____| |  |   |
              |___|  |_______||______| |_______|       |_______||___| |_______|  |___|

                          Добро пожаловать в консольный ToDo-лист v0.0.1

    Доступные команды:
    [1] Показать задачи
    [2] Добавить задачу
    [3] Удалить задачу
    [4] Выполнить задачу
    [5] Выйти из программы
    Введите команду:
"""
# | блок кода для плавного вывода текста в консоль |
import sys
import time
def type_print(text, delay=0.08):
    for word in text.split():
        sys.stdout.write(word + " ")
        sys.stdout.flush()
        time.sleep(delay)
    print()
# | блок кода для плавного вывода текста в консоль |
tasks = []

def show_tasks():
    if not tasks:
        type_print("Здесь пока нет задач.")
    else:
        for i, task in enumerate(tasks):
            complete = "[x]" if task['completed'] else "[ ]"
            type_print(f"[{i + 1}] {complete} {task['title']}")

def add_task():
    task = input("Введите задачу: ").strip()
    if task.isdigit():
        type_print("Задача не может быть числом.")
    elif not task:
        type_print("Задача не может быть пустой.")
    else:
        tasks.append({'title': task, 'completed': False})
        type_print(f"Задача [{task}] добавлена.")

def delete_task():
    show_tasks()
    task_remove_index = input("Введите номер задачи для удаления: ").strip()
    if task_remove_index and task_remove_index.isdigit():
        task_remove_index = int(task_remove_index) - 1
        if 0 <= task_remove_index < len(tasks):
            removed_task = tasks.pop(task_remove_index)
            type_print(f"Задача '{removed_task['title']}' удалена.")
        else:
            type_print("Неверный номер задачи.")
    else:
        type_print("Вы не ввели номер задачи. Пожалуйста, попробуйте снова.")

def complete_task():
    show_tasks()
    task_complete_index = input("Введите номер задачи для пометки выполненной: ").strip()
    if task_complete_index and task_complete_index.isdigit():
        task_complete_index = int(task_complete_index) - 1
        if 0 <= task_complete_index < len(tasks):
            tasks[task_complete_index]['completed'] = True
            type_print(f"Задача [{tasks[task_complete_index]['title']}] выполнена.")
        else:
            type_print("Неверный номер задачи.")
    else:
        type_print("Вы не ввели номер задачи. Пожалуйста, попробуйте снова.")

def main():
    print(
        """
             _______  _______  ______   _______         ___      ___   _______  _______
            |       ||       ||      | |       |       |   |    |   | |       ||       |
            |_     _||   _   ||  _    ||   _   |       |   |    |   | |  _____||_     _|
              |   |  |  | |  || | |   ||  | |  |       |   |    |   | | |_____   |   |
              |   |  |  |_|  || |_|   ||  |_|  |       |   |___ |   | |_____  |  |   |
              |   |  |       ||       ||       |       |       ||   |  _____| |  |   |
              |___|  |_______||______| |_______|       |_______||___| |_______|  |___|
        """
    )
    type_print("                         Добро пожаловать в консольный ToDo-лист v0.0.1")
    while True:
        type_print("\nДоступные команды:")
        type_print("[1] Показать задачи")
        type_print("[2] Добавить задачу")
        type_print("[3] Удалить задачу")
        type_print("[4] Выполнить задачу")
        type_print("[5] Выйти из программы")
        command = input("Введите команду: ").strip()
        if command == "1":
            show_tasks()
        elif command == "2":
            add_task()
        elif command == "3":
            delete_task()
        elif command == "4":
            complete_task()
        elif command == "5":
            type_print("Выход из программы.")
            break
        else:
            type_print("Неверная команда. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()