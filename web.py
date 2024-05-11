import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title(" My Todo App")
st.header("This is my Todo App")
st.write("""
This is to increase productivity
""")
st.checkbox("Can you buy grocery")
st.checkbox("Throw trash")

for todo in todos:
    st.checkbox(todo, key=todo)

st.text_input(label="", placeholder="Add new todo..",
              on_change=add_todo, key="new_todo")

print("HEllo World")

st.session_state