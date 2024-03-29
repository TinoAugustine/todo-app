import functions
import PySimpleGUI as sg

lable = sg.Text("Type in Too Do")
input_box = sg.InputText(tooltip="Enter Your Todo")
add_button = sg.Button("Add")

window = sg.Window('My To Do App', [[lable], [input_box], [add_button]])
window.read()
print("Hello World")
window.close()
