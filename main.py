import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkGrey5")

clock = sg.Text(key='time')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button("Add", size=12)
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[44, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


window = sg.Window("Task Manager App",
                   layout=[
                       [clock],
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button, complete_button],
                       [exit_button],
                       ],
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=100)
    window['time'].update(value=time.strftime("%d %B %Y, %I:%M:%S %p"))

    match event:
        case "Add":
            todos = functions.get_todos() # Mengambil isi data
            new_todo = values['todo'] + "\n"
            todos.append(new_todo) # Membuat variable baru new_todo yang mengambil values dari key todo (input_box) dan ditambahkan ke akhir list
            functions.write_todos(todos)
            window['todos'].update(values=todos) # Ambil Listbox dengan key todos, lalu update isi Listbox dengan data terbaru dari variabel todos

        case "Edit":
            try:
                todo_to_edit = values['todos'][0] # Ambil 1 todo yang dipilih user (dari list selection)
                todos = functions.get_todos()

                new_todo = values['todo'] + "\n"
                index = todos.index(todo_to_edit) # Cari index dari data yang mau diedit
                todos[index] = new_todo # Mengubah index yang dipilih menjadi new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first!", font=('Helvetica', 20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()

                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first!", font=('Helvetica', 20))

        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close() # Close di luar supaya aplikasi tetap berjalan setelah action dilakukan.

# pyinstaller --onefile --windowed app1/converter.py --distpath app1/dist