from task import Task
import json

class TaskRepository:
    def __init__(self, filename="./data/task_data.json"):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                self.tasks = {task['id']: Task(**task) for task in json.load(f)}
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = {}

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks.values()], f, indent=4)

    def add_task(self, description):
        task_id = max(self.tasks.keys(), default=0) + 1
        task = Task(task_id, description)
        self.tasks[task.id] = task
        self.save_tasks()
        return task

    def update_task(self, task_id, description):
        task = self.tasks.get(task_id)
        if task:
            task.update_description(description)
            self.save_tasks()
            return task
        return None

    def delete_task(self, task_id):
        task = self.tasks.pop(task_id, None)
        if task:
            self.save_tasks()
        return task

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def list_tasks(self, status=None):
        if status:
            return [task for task in self.tasks.values() if task.status == status]
        return list(self.tasks.values())
