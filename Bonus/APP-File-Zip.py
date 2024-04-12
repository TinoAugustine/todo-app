import PySimpleGUI as sg

lable1 = sg.Text("Select Files to Compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compres")

window = sg.Window("File Comprossor",
                   layout=[[lable1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button]
                           ]
                   )
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    print(filepaths,folder)
window.close()


