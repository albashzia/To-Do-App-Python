# creating 3 main lists to hold parallel data
tasks = [] 
descriptions = []
statuses = []
# creating a function to add data to the lists 
def add_task(title, description, status):
    global tasks, descriptions, statuses
    tasks.append(title)
    descriptions.append(description)
    statuses.append(status)
# creating a function to view all incomplete tasks
def view_incomplete_task():
    global tasks, statuses
    for i in range(len(tasks)):
        if statuses[i] == "incomplete":
            print(tasks[i])
        print()
# creating a function to delete a task having a certain keyword
def delete_task(keyword):
    # declaring new lists for updated data 
    new_tasks = []
    new_descriptions = []
    new_statuses = []
    global tasks, descriptions, statuses
    # looping over the entries of tasks list and description lists 
    for i in range(len(tasks)):
        # checking for presence of keyword in tasks or descriptions list
        if keyword not in tasks[i] or keyword not in descriptions[i]: 
            new_tasks.append(tasks[i])
            new_descriptions.append(descriptions[i])
            new_statuses.append(statuses[i])       
    # updating original lists with new lists
    tasks = new_tasks
    descriptions = new_descriptions
    statuses = new_statuses
    
# main entry point
print("Welcome to To-Do App")
choice = 0
while choice != 4:
    # displaying a menu
    print("1. Add a task.")
    print("2. View Incomplete Tasks.")
    print("3. Delete a task.")
    print("4. Exit the program.")
    # taking user's choice
    choice = int(input("Enter your choice: "))
    # proceeding for choice = 1
    if choice == 1:
        title = input("Enter the title of the task: ")
        desc = input("Enter task's description: ")
        status = input("Enter the status of the task: ").lower().strip()
        add_task(title, desc, status) # call to add_task function
    # proceeding for choice = 2
    elif choice == 2:
        view_incomplete_task() # call to view_incomplete_task function
    # proceeding for choice = 3
    elif choice == 3:
        word = input("Enter the keyword to remove the task using it: ")
        delete_task(word) # call to delete_task function 
        print("Action Complete")
    # proceeding for choice = 4
    elif choice == 4:
        break # exiting the program 
