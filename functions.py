import os, sys

# BASE_DIR = os.path.dirname(sys.executable) # lokasi program yang berjalan (cocok untuk exe)
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # lokasi script (untuk development)
FILEPATH = os.path.join(BASE_DIR, "todos.txt")

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())