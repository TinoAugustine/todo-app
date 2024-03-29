import functions
import PySimpleGUI as sg

lable = sg.Text("Type in To-Do")
input_box = sg.InputText(tooltip="Enter Your Todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To Do App',
                   [[lable], [input_box], [add_button]],
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
        case sg.WIN_CLOSED:
            break
window.close()
