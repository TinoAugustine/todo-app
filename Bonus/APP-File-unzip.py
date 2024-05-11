import PySimpleGUI as sg

from fununzip import extract_archive



sg.theme("BlueMono")

lable1 = sg.Text("Select the Archive:")
input1 = sg.Input()
button1 = sg.FileBrowse("Choose", key="archive")

lable2 = sg.Text("Select Destination:")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose", key="destination")

button3 = sg.Button("UnZip")
output_lable = sg.Text(key="output", text_color="Red")

window = sg.Window("Unzip Boy",
                   layout = [[lable1,input1,button1],
                             [lable2,input2,button2],
                             [button3, output_lable ]
                             ]
                    )

while True:
    event, values = window.read()
    print(event,values)
    archivepath = values["archive"]
    dest_dir = values["destination"]
    extract_archive(archivepath,dest_dir)
    window["output"].update(value="Extraction Completed!")

window.close()





