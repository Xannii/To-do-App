import streamlit as st
import functions

todos = functions.get_todos()                   #to give a list of todos from the file

def add_todo():                                 #use a text input key to access the value
    todo = st.session_state["new_todo"] + "\n"   #to get the user input
    if todo not in todos:
        todos.append(todo)                          #update the todos list
        functions.write_todos(todos)                #write new task to the list

st.title("My Todo App")                         #returns a title instance
st.subheader("These are your tasks for the week")

for index, todo in enumerate(todos):                        #will add a new checkbox for the new task
    checkbox = st.checkbox(todo, key=f"task_{index}")                  #add todo as the label of checkbox
    if checkbox:                                #when the user is checked the checkbox
        todos.pop(index)
        functions.write_todos(todos)

        #Check if the key exists before deleting
        key = f"task_{index}"
        if key in st.session_state:
            del st.session_state[key]               #delete completed task from the session

        st.rerun()                                  #to rerun the code

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')      #create a key for that widget

