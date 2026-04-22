import FreeSimpleGUI as sg

first_label = sg.Text("Enter feet:")
first_input = sg.InputText(tooltip="Enter feet", key='feet')

second_label = sg.Text("Enter inches:")
second_input = sg.InputText(tooltip="Enter inches", key='inches')

convert_button = sg.Button("Convert")
result = sg.Text(key="result")

window = sg.Window("Convertor", layout=[
    [first_label, first_input],
    [second_label, second_input],
    [convert_button, result]
])

while True:
    event, values = window.read()
    match event:
        case "Convert":
            feet = float(values['feet'])
            inches = float(values['inches'])
            total_inches = feet * 12 + inches
            meters = total_inches * 0.0254

            window['result'].update(f"{meters:.3f} meters")
        case sg.WIN_CLOSED:
            break

window.close()