import datetime

class Task:
    def __init__(self, id, description, status="todo"):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updatedAt = self.createdAt

    def update_description(self, description):
        self.description = description
        self.updatedAt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mark_in_progress(self):
        self.status = "in-progress"
        self.updatedAt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mark_done(self):
        self.status = "done"
        self.updatedAt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }