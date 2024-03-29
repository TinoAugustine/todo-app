import PySimpleGUI as sg
import zipfile
import os

def compress_files(file_list, destination_folder):
    zip_file_path = os.path.join(destination_folder, 'compressed_files.zip')
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for file_path in file_list:
            zipf.write(file_path, os.path.basename(file_path))
    return zip_file_path

layout = [
    [sg.Text("Select Files to compress:")],
    [sg.Input(key="-FILES-", enable_events=True, visible=False), sg.FilesBrowse("Choose", key="-BROWSE-")],
    [sg.Listbox(values=[], size=(60, 6), key="-FILELIST-")],
    [sg.Text("Select Destination Folder:")],
    [sg.Input(key="-FOLDER-"), sg.FolderBrowse("Choose")],
    [sg.Button("Compress"), sg.Button("Exit")]
]

window = sg.Window("File Compressor", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "-BROWSE-":
        selected_files = values["-BROWSE-"].split(';')
        window["-FILELIST-"].update(selected_files)
    elif event == "Compress":
        file_list = values["-FILELIST-"]
        destination_folder = values["-FOLDER-"]
        if file_list and destination_folder:
            zip_file_path = compress_files(file_list, destination_folder)
            sg.popup(f"Files compressed successfully!\nZip file saved at:\n{zip_file_path}")

window.close()
