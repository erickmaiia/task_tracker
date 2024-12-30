from task_repository import TaskRepository

class TaskCLI:
    def __init__(self):
        self.repo = TaskRepository()

    def add_task(self, description):
        task = self.repo.add_task(description)
        print(f"Task added successfully (ID: {task.id})")

    def update_task(self, task_id, description):
        task = self.repo.update_task(task_id, description)
        if task:
            print(f"Task {task_id} updated successfully")
        else:
            print(f"Task {task_id} not found")

    def delete_task(self, task_id):
        task = self.repo.delete_task(task_id)
        if task:
            print(f"Task {task_id} deleted successfully")
        else:
            print(f"Task {task_id} not found")

    def mark_in_progress(self, task_id):
        task = self.repo.get_task(task_id)
        if task:
            task.mark_in_progress()
            self.repo.save_tasks()
            print(f"Task {task_id} marked as in-progress")
        else:
            print(f"Task {task_id} not found")

    def mark_done(self, task_id):
        task = self.repo.get_task(task_id)
        if task:
            task.mark_done()
            self.repo.save_tasks()
            print(f"Task {task_id} marked as done")
        else:
            print(f"Task {task_id} not found")

    def list_tasks(self, status=None):
        tasks = self.repo.list_tasks(status)
        if tasks:
            for task in tasks:
                print(f"ID: {task.id}, Description: {task.description}, Status: {task.status}, CreatedAt: {task.createdAt}, UpdatedAt: {task.updatedAt}")
        else:
            print("No tasks found")
