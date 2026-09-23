FILPATH = "todos.txt"


def get_todos(filepathe=FILPATH):
    """ Read a text file and return a list of todos """
    with open(filepathe, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepathe=FILPATH):
    """ Write a list of todos"""
    with open(filepathe, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print(get_todos())
    print('hello')
