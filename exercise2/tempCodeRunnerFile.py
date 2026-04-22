from backend import extract_archive
import FreeSimpleGUI as sg

sg.theme("Black")

extract_button = sg.Button("Extract")
output_label = sg.Text(key='output', text_color='green')
          
layout = [
    [
        sg.Column([
            [sg.Text("Select Archive:")],
            [sg.Text("Select Destination Directory:")]
        ]),
        sg.Column([
            [sg.Input(key='archive')],
            [sg.Input(key='destdir')]
        ]),
        sg.Column([
            [sg.FileBrowse("Choose")],
            [sg.FolderBrowse("Choose")]
        ])
    ],
    [extract_button, output_label]
]


window = sg.Window("Archive Extractor", layout)  
while True:
    event, values = window.read()
    archive_path = values['archive']
    dest_dir = values['destdir']
    extract_archive(archive_path, dest_dir)
    window['output'].update(value="Extraction Completed!")

    if event == sg.WIN_CLOSED:
        break
window.close()