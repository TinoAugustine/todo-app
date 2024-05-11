def get_todos(filepath='todos.txt'):
    """Read the Text file and returns the
    To-Dos Items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath='todos.txt'):
    """Write the  To-Dos Items
    To the Text files.
    """
    with open (filepath, 'w') as file:
        file.writelines(todos_arg)