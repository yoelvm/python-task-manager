import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def validate_due_date(due_date):
    if not due_date:
        return "Sin fecha"

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return due_date
    except ValueError:
        print("Fecha no válida. Se asignará 'Sin fecha'.")
        return "Sin fecha"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def show_menu():
    print("\n=== Python Task Manager ===")
    print("1. Ver tareas")
    print("2. Añadir tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")


def list_tasks(tasks):
    if not tasks:
        print("\nNo hay tareas guardadas.")
        return

    print("\nLista de tareas:")

    for index, task in enumerate(tasks, start=1):
        status = "Completada" if task["completed"] else "Pendiente"
        priority = task.get("priority", "media")
        due_date = task.get("due_date", "Sin fecha")
        print(
            f"{index}. {task['title']} - {status} "
            f"- Prioridad: {priority} - Fecha límite: {due_date}"
        )

def add_task(tasks):
    title = input("\nEscribe el nombre de la tarea: ").strip()

    if not title:
        print("La tarea no puede estar vacía.")
        return

    priority = input("Prioridad de la tarea (baja/media/alta): ").strip().lower()

    if priority not in ["baja", "media", "alta"]:
        print("Prioridad no válida. Se asignará prioridad media.")
        priority = "media"

    due_date = input("Fecha límite de la tarea (YYYY-MM-DD, opcional): ").strip()
    due_date = validate_due_date(due_date)

    task = {
        "title": title,
        "completed": False,
        "priority": priority,
        "due_date": due_date
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Tarea añadida correctamente.")


def complete_task(tasks):
    list_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("\nNúmero de la tarea completada: "))

        if task_number < 1 or task_number > len(tasks):
            print("Número de tarea no válido.")
            return

        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print("Tarea marcada como completada.")

    except ValueError:
        print("Debes introducir un número válido.")


def delete_task(tasks):
    list_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("\nNúmero de la tarea a eliminar: "))

        if task_number < 1 or task_number > len(tasks):
            print("Número de tarea no válido.")
            return

        deleted_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Tarea eliminada: {deleted_task['title']}")

    except ValueError:
        print("Debes introducir un número válido.")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        option = input("\nSelecciona una opción: ").strip()

        if option == "1":
            list_tasks(tasks)
        elif option == "2":
            add_task(tasks)
        elif option == "3":
            complete_task(tasks)
        elif option == "4":
            delete_task(tasks)
        elif option == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()