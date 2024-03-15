import fileinput
# application to enter a todo list and archive it #

import functions
import time

print(time.strftime("Current Date and Time is = " "%A %D %T"))
user_prompt = "Type add or show or edit or complete or exit:"

while True:
    # Get user input and Strip any unwanted space from it
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]
        #convert the input to Title Case
        todo_title = todo.title() + '\n'

        todos = functions.get_todos()
        todos.append(todo_title)

        functions.write_todos(todos)

    elif user_action.startswith('show') or user_action.startswith('display'):

        todos = functions.get_todos()
        for index, item in enumerate(todos):

# To Strip the extra page Break from items Another method is below
# new_todos= [item.strip('\n') for items in todos]
            item = item.strip('\n')
            row= f"{index +1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            # number = int(input("Number of the item to edit:"))
            number = number -1
            todos = functions.get_todos()

            new_todo = input("Enter new todo:")
            todo_update = todos[number].strip('\n')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

            print(f'Todo {todo_update} was updated to', new_todo)
        except  ValueError:
            print("You have entered a wrong command!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number -1

            todos = functions.get_todos()

            todos_to_remove = todos[index].strip('\n')
            todos.pop(number -1)

            functions.write_todos(todos)

            message = f"Todos '{todos_to_remove}' has been marked as completed"
            print(message)
        except ValueError:
            print("You have entered a wrong command!")
        except IndexError:
            print("There is no Item with that Value!")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Enter a valid command!")

print("Bye...")