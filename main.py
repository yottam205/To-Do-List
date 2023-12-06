import tabulate
import sys


def main():
    tasks = []
    count = 0
    running = True

    while running:
        menu_options = [{"No.": "1.", "action": "Add Tasks"},
                    {"No.": "2.", "action": "View Tasks"},
                    {"No.": "3.", "action": "Edit Tasks"},
                    {"No.": "4.", "action": "Done Tasks"},
                    {"No.": "5.", "action": "Exit"}]

        print(tabulate.tabulate(menu_options, headers="keys", tablefmt="pretty"))
        try:
            choice = input("Enter choice: ").title()
            if choice == "1" or choice == "Add Tasks":
                tasks, count = add_task(tasks, count)
            elif choice == "2" or choice == "View Tasks":
                view_tasks(tasks, count)
            elif choice == "3" or choice == "Edit Tasks":
                edit_tasks(tasks, count)
            elif choice == "4" or choice == "Done Tasks":
                tasks, count = done_tasks(tasks, count)
            elif choice == "5" or choice == "Exit":
                sys.exit("Thanks a lot, Byeeeeeeeee")
            else:
                print("Please choose one option from main menu")
        except ValueError:
            "Please choose one option from main menu"



def add_task(tasks, count):

    task = input("Task: ")
    count += 1
    tasks.append({"No.": count, "Task": task, "Status": "Not Done"})
    return tasks, count


def view_tasks(tasks, count):
    if count == 0:
        print("Task list is empty")
        main()
    else:
        task_data = [{"No.": task["No."], "Task": task["Task"], "Status": task["Status"]} for task in tasks]
        print(tabulate.tabulate(tabular_data=task_data, headers="keys", tablefmt="pretty"))
    end_or_menu()

def edit_tasks(tasks, count):
    if count == 0:
        print("Task list is empty")
        main()
    elif count >= 1:
        print(tabulate.tabulate(tasks, headers="keys", tablefmt="pretty"))

    choose_task = int(input("Enter the task number to edit: "))
    if 1 <= choose_task <= len(tasks):
        new_task = input("Pleas enter your new task: ")
        tasks[choose_task - 1]["Task"] = new_task
        tasks[choose_task - 1]["Status"] = "Not Done"
        print(f"Task {choose_task} has been updated")
        new_edit = input("Do you want to edit another task? (y/n) ").lower()
        if new_edit == "y":
            edit_tasks()
        else:
            end_or_menu()
    else:
        print("Invalid task number")
        edit_tasks()


def done_tasks(tasks, count):
    if count == 0:
        print("Task list is empty")
        main()
    else:
        print(tabulate.tabulate(tabular_data=tasks, headers="keys", tablefmt="pretty"))
        choose_task = int(input("Enter the task number to mark as Done (Or press 9 to go back): "))
        if choose_task == 0:
            end_or_menu()
        elif choose_task == 9:
            main()
        if 1 <= choose_task <= len(tasks):
            tasks[choose_task - 1]["Status"] = "Done"
            print("Task marked as 'Done'")
            view_tasks(tasks, count)
            return tasks, count
        else:
            print("Invalid task number")
            done_tasks(tasks, count)


def end_or_menu():
    while True:
        print("\nTo go back to main menu, press 9 or write 'Back'")
        print("If you wish to exit, press 5 or write 'Exit'")
        choose = input("").title()
        if choose == "9" or choose == "Back":
            break
        elif choose == "5" or choose == "Exit":
            sys.exit("Thanks a lot, Byeeeeeeeee")
        else:
            print("Invalid choice, please choose again")


if __name__ == "__main__":
    main()