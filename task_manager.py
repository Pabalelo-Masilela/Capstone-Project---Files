print("Welcome to the task manager login page!")
# import modules
import datetime

# user login info acess and string manipulations for list formats
user_list_storage = []
password_list_storage = []
login_entry = []
with open('user.txt','r+') as users:
    for line in users:
        login_entry = line.split(',')
        login_entry[1] = login_entry[1].strip()
        user_list_storage = user_list_storage + [login_entry[0]]
        password_list_storage = password_list_storage + [login_entry[1]]
    print(user_list_storage)
    print(password_list_storage)

# Login verifications  
    while True: # while the conditions of a succesful login have not been met, loop continues.
        username = (input("Enter username: \n")).lower()
        password = (input("Enter password: \n")).lower()
        if username in user_list_storage:
            i = user_list_storage.index(username)
            if password == password_list_storage[i]:
                print("You have been succesfully authenticated.")
                break # stop the loop if all logins are correct.
            else:
                print("Incorrect password.Try again.")
        else:
            print("Incorrect username.Try again.")

# Menu selection options
while True:
    if username == "admin":
         menu = input('''Select one of the following options:
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        d - display task statistics              
        e - exit
        \n''').lower()

    else:
        menu = input('''Select one of the following options:
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit
        \n''').lower()

# New user registartion
    if menu == "r":
        if username == "admin":
        
            new_username = input("Enter new username: \n").lower()
            with open ('user.txt', 'r') as users:
                for lines in users:
                    user_list = lines.split(",")
                    if new_username == user_list[0]:
                        print("Username already exists.Try a new one")
                        break
                    else:
                        new_password = input("Enter new password: \n").lower()
                        confirm_password = input("Confirm new password: \n").lower()
                        if new_password == confirm_password:
                            print("Thank you!You have been registered.")
                            with open ('user.txt', 'a+') as users:
                                users.write(f"\n{new_username}, {new_password}")
                        else:
                            print("Password confirmation did not match new password.Register again.")
                    break
        else:
            print("Please note, only user with admin credintials is permitted to log a new user.")

# New task addition
    elif menu == "a":
        task_username = input("Enter username of person assigned to task: \n").lower()
        task_title = input("Enter task title: \n").lower()
        task_description = input("Enter task description: \n").lower()
        date_format = "%d %b %Y"
        task_completion = "No"
        task_assign_date = datetime.date.today().strftime(date_format)
        
        while True:
            task_due_date = input("Enter task due date(e.g format: 30 Oct 2019): \n")
            try:
                datetime.datetime.strptime(task_due_date,date_format)
                with open('tasks.txt', '+a') as tasks_page:
                    tasks_page.write(f"\n{task_username}, {task_title}, {task_description}, {task_assign_date}, {task_due_date}, {task_completion}")
                print("Task requirements captured.")
                break
            except:
                print("Invalid date format.Try again.")
    
# View all tasks
    elif menu == "va":
        with open('tasks.txt', 'r') as tasks_page:
            for lines in tasks_page:
                task_line = lines.split(",")
                print(f'''Task information;
Assigned user: {task_line[0]}
Task title:{task_line[1]}
Task description:{task_line[2]}
Date assigned:{task_line[3]}
Due date:{task_line[4]}
Task completed:{task_line[5]}''')

# view user tasks
    elif menu == "vm":
        with open('tasks.txt','r') as tasks_page:
            for lines in tasks_page:
                task_line = lines.split(",")
                if username == task_line[0]:
                    print(f'''Task information;
Assigned user: {task_line[0]}
Task title:{task_line[1]}
Task description:{task_line[2]}
Date assigned:{task_line[3]}
Due date:{task_line[4]}
Task completed:{task_line[5]}''')
                    break
                else:
                    print("No task information found for user.")
# Display task statistics
    elif menu == "d":
        with open('user.txt','r+') as users:
            user_list_storage = []
            for line in users:
                login_entry = line.split(',')
                login_entry[1] = login_entry[1].strip()
                user_list_storage = user_list_storage + [login_entry[0]]
            task_list_storage = [0] * len(user_list_storage)
            total_tasks = 0
            with open('tasks.txt','r') as tasks_page:
                for line in tasks_page:
                    task_string = line.split(',')  
                    user_index = user_list_storage.index(task_string[0])
                    user_tasks = task_list_storage[user_index]
                    task_list_storage[user_index] = user_tasks +1
                print(task_list_storage)  
                for i, user in enumerate(user_list_storage):
                    total_tasks += task_list_storage[i]
                    print(f"{user}: {task_list_storage[i]} task(s)")
                    print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
                print(f"Total users:{len(user_list_storage)} \nTotal tasks:{total_tasks}")
                break
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made entered an invalid input. Please try again")