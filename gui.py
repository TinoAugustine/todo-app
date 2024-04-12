import functions
import PySimpleGUI as sg

lable = sg.Text("Type in To-Do")
input_box = sg.InputText(tooltip="Enter Your Todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To Do App',
                   [[lable],
                    [input_box],
                    [add_button],
                    [list_box, edit_button, complete_button],
                    [exit_button]
                    ],
                   font=('Helvetica',20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Exit":
            break
        case 'todos':
            window['todo'].update(values['todos'][0])
        case sg.WIN_CLOSED:
            break
print("Bye")
window.close()
