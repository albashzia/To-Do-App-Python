tasks = []
descriptions = []
statuses = []
def add_task(title, description, status):
    global tasks, descriptions, statuses
    tasks.append(title)
    descriptions.append(description)
    statuses.append(status)

def view_incomplete_task():
    global tasks, statuses
    for i in range(len(tasks)):
        if statuses[i] == "incomplete":
            print(tasks[i])
        print()

def delete_task(keyword):
    new_tasks = []
    new_descriptions = []
    new_statuses = []
    global tasks, descriptions, statuses
    for i in range(len(tasks)):
        if keyword not in tasks[i] or keyword not in descriptions[i]:
            new_tasks.append(tasks[i])
            new_descriptions.append(descriptions[i])
            new_statuses.append(statuses[i])

    tasks = new_tasks
    descriptions = new_descriptions
    statuses = new_statuses

print("Welcome to To-Do App")
choice = 0
while choice != 4:
    print("1. Add a task.")
    print("2. View Incomplete Tasks.")
    print("3. Delete a task.")
    print("4. Exit the program.")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        title = input("Enter the title of the task: ")
        desc = input("Enter task's description: ")
        status = input("Enter the status of the task: ").lower().strip()
        add_task(title, desc, status)

    elif choice == 2:
        view_incomplete_task()

    elif choice == 3:
        word = input("Enter the keyword to remove the task using it: ")
        delete_task(word)
        print("Action Complete")

    elif choice == 4:
        break
