import PySimpleGUI as sg

sg.theme("Black")

def to_meter(inch,feet):
    meter = feet * 0.3048 + inch * 0.0254
    return meter


lable1 = sg.Text("Enter Feet:")
input1 = sg.Input(key="feet")
button1 = sg.Button("Convert", key="Convert")

lable2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inch")
button2 = sg.Button("Exit", key="Exit")

output1 = sg.Text(key="output", text_color="Red")

window = sg.Window("Convertor",
                   layout=[[lable1,input1],
                           [lable2,input2],
                           [button1,button2,output1]
                           ]
                   )
event, values = window.read()

while True:
    try:

        if event == "Convert":
            event, values = window.read()
            print(event,values)
            feet = float(values["feet"])
            inch = float(values["inch"])
            result = to_meter(inch,feet)
            window["output"].update(value=f"{result} m", text_color="white")
        if event == "Exit":
            break
    except ValueError:
        sg.popup("Please Enter Values")

window.close()


