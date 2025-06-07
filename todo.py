tasks = []

def show_tasks():
    if not tasks:
        print("Здесь пока нет задач.")
    else:
        for i in range(len(tasks)):
            status = "[x]" if tasks[i]['completed'] else "[ ]"
            print(f"[{i + 1}] {status} {tasks[i]['title']}")

def add_task():
    while True:
        task = input("Введите задачу: ").strip()
        if task.isdigit():
            print("Задача не может быть числом.")
        elif not task:
            print("Задача не может быть пустой.")
        else:
            tasks.append({'title': task, 'completed': False})
            print(f"Задача [{task}] добавлена.")

def delete_task():
    while True:
        show_tasks()
        task_remove_index = input("Введите номер задачи для удаления: ").strip()
        if task_remove_index and task_remove_index.isdigit():
            task_remove_index = int(task_remove_index) - 1
            if 0 <= task_remove_index < len(tasks):
                removed_task = tasks.pop(task_remove_index)
                print(f"Задача '{removed_task['title']}' удалена.")
                break
            else:
                print("Неверный номер задачи. Попробуйте снова.")
        else:
            print("Вы не ввели номер задачи. Пожалуйста, попробуйте снова.")

def complete_task():
    while True:
        show_tasks()
        task_complete_index = input("Введите номер задачи для пометки выполненной: ").strip()
        if task_complete_index and task_complete_index.isdigit():
            task_complete_index = int(task_complete_index) - 1
            if 0 <= task_complete_index < len(tasks):
                tasks[task_complete_index]['completed'] = True
                print(f"Задача [{tasks[task_complete_index]['title']}] выполнена.")
                break
            else:
                print("Неверный номер задачи. Попробуйте снова.")
        else:
            print("Вы не ввели номер задачи. Пожалуйста, попробуйте снова.")
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
    print("                         Добро пожаловать в консольный ToDo-лист v0.0.1")
    while True:
        print("\nДоступные команды:")
        print("[1] Показать задачи")
        print("[2] Добавить задачу")
        print("[3] Удалить задачу")
        print("[4] Выполнить задачу")
        print("[5] Выйти из программы")
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
            print("Выход из программы.")
            break
        elif command == " ":
            print("Вы не ввели команду. Пожалуйста, попробуйте снова.")
        else:
            print("Неверная команда. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()