todos = []

def add_todo(todo):
    todos.append(todo)

def remove_todo(todo):
    if(todo not in todos):
        print(f"Todo '{todo} is not in the list")
    else:    
        todos.remove(todo)
        print(f"Removed '{todo}' successfully")

def change_todo(todo, newTodo):
    if(todo not in todos):
        print(f"Todo '{todo} is not in the list")
    else:    
        i = todos.index(todo)
        todos[i] = newTodo
        print(f"Changed todo '{todo}' to {newTodo}")


while True:
    choice = input("Enter your command. 'add', 'remove', 'change', 'show': ")
    if choice == 'add':
        todo = input("Enter the title of the todo: ")
        add_todo(todo)
        
    elif(choice == 'remove'):
        todo = input("Enter the title of the todo: ")
        remove_todo(todo)
    elif(choice == 'change'):
        todo = input("Enter the title of the todo you want to change: ")
        new_todo = input("Enter the new title of the todo: ")
        change_todo(todo, new_todo)
        
        continue
    elif(choice == "show"):
        print("")
        print("---------------------TODOLIST--------------------")
        for todo in todos:
            print(f"{todo}")
        print("----------------- END OF TODOLIST----------------")
        print("")
        
    else:
        print("Unknown command")