user_prompt = "Enter ToDo list:"
to_dos = []

while True:
    to_do = input(user_prompt)
    todo_title = to_do.title()
    to_dos.append(todo_title)
    print("Next...")
    print(to_dos)