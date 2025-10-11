import os

file_name = "task.txt"

#load tasks from file
def load_tasks():
    tasks={}
    if os.path.exists(file_name):
        with open(file_name,'r') as file:
            for line in file:
                task_id, title, status = line.strip().split("|")
                tasks[int(task_id)]={"title":title,"status":status}
    return tasks

#save task to file
def save_tasks(tasks):
    with open(file_name,"w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']} \n")


#add new task
def add_task(tasks):
    title = input("enter task title: ")
    task_id = max(tasks.keys(),default=0) +1
    tasks[task_id] = {"title":title, "status":"incomplete"}
    print(f"task '{title}' added.")
    

#view all tasks
def view_tasks(tasks):
    if not tasks:
        print("no tasks available")
    else:
        for task_id,task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']}")

#mark task as complete
def mark_task_complete ( tasks):
    task_id = int(input("Enter task ID to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"tasks '{tasks[task_id]['title']}' marked as complete.")
    else:
        print("task id not found.")

#delete task
def delete_task ( tasks):
    task_id = int(input("Enter task ID to delete: "))
    if task_id in tasks:
        delete_task = tasks.pop(task_id)
        print(f"tasks '{delete_task['title']}' deleted.")
    else:
        print("task id not found.")

#main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n task manager menu: ")
        print("1- Add Task")
        print("2. View Tasks") 
        print("3. Mark as Complete") 
        print("4. Delete task") 
        print("5. Exit")  
        choice = input("enter your choice: ")
        if choice=='1':
            add_task(tasks)
        elif choice=='2':
            view_tasks(tasks)   
        elif choice=="3":
            mark_task_complete(tasks)
        elif choice=='4':
            delete_task(tasks)
        elif choice=='5':
            save_tasks(tasks)
            print("GoodBye, Do your best")
            break
        else:
            print("Invalid choice please try again")

if __name__ == "__main__":
    main()
    
    
            
    
               