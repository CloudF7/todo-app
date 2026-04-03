from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is: ", now)

# # pip install astropy
# from astropy.time import Time
# t = Time.now()
# print(t)

while True:
    user_action = input('Type add, show, edit, complete, or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos, start=1):
            item = item.title().strip('\n')
            print(index, item)

    elif user_action.startswith('edit'):
        try:        
            number = int(user_action[5:])
            print(number)

            todos = get_todos()

            if 0 < number <= len(todos):
                edited_todo = input('Enter new todo: ')
                todos[number-1] = edited_todo + '\n'
                write_todos(todos)
            else:
                print('Invalid number')
        except ValueError:
            print("Your command is not valid!")

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            if 0 < number < len(todos):
                completed_todo = todos[number-1].strip('\n')
                todos.pop(number-1)

                write_todos(todos)

                message = f'Todo {completed_todo} was removed from the list.'
                print(message)
            else:
                print("Invalid number")
        except ValueError:
            print("Your command is not valid!")

    elif user_action.startswith('exit'):
        break
    else:
        exit('Unknown command, exiting program!')

    

        