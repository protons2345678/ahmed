# Todo List Application 

tasks = []

def add_task(task_description):
    tasks.append({'task': task_description, 'completed':False})
    print(f'Task "{task_description}" added.')

def view_tasks():
    if not tasks:
        print("No tasks.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = 'done' if task ['completed'] else 'not done'
            print(f"{index}. [{status}] {task['task']}")

def mark_task_completed(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['completed'] = True
        print(f"Task {task_index} marked as completed.")
    else:
        print("Invalid task index.")

def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        print(f"Task {task_index} deleted.")
    else:
        print("Invalid task index.")
    
# Example usage 
add_task("Study math")
add_task("Finish report")
view_tasks()

mark_task_completed(1)
view_tasks()

delete_task(2)
view_tasks()