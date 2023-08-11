import datetime
import time
import os
from win10toast import ToastNotifier

os.system('cls')
print("""\033[0;32m
░█▀▀▀█ ░█▀▀█ ░█─░█ ░█▀▀▀ ░█▀▀▄ ░█─░█ ░█─── ░█▀▀▀ ░█▀▀█ 
─▀▀▀▄▄ ░█─── ░█▀▀█ ░█▀▀▀ ░█─░█ ░█─░█ ░█─── ░█▀▀▀ ░█▄▄▀ 
░█▄▄▄█ ░█▄▄█ ░█─░█ ░█▄▄▄ ░█▄▄▀ ─▀▄▄▀ ░█▄▄█ ░█▄▄▄ ░█─░█
\033[0m""")


def get_task_details():
    task = input("Enter the task: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    time_str = input("Enter the time (HH:MM AM/PM): ")
    return task, date, time_str


def show_notification(message):
    toaster = ToastNotifier()
    toaster.show_toast("Scheduled Task", message, duration=10)


if __name__ == "__main__":
    num_tasks = int(input("Enter the number of tasks: "))

    tasks = []
    for _ in range(num_tasks):
        task, date, time_str = get_task_details()
        tasks.append((task, date, time_str))

    for task_info in tasks:
        task, date, time_str = task_info

        datetime_str = f"{date} {time_str}"
        task_datetime = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %I:%M %p")

        current_datetime = datetime.datetime.now()
        time_diff = (task_datetime - current_datetime).total_seconds()

        if time_diff <= 0:
            print(f"The specified time for task '{task}' has already passed.")
        else:
            time.sleep(time_diff)
            show_notification(task)
