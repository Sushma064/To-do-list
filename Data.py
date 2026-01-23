class SubTask:
    def __init__(self, name, due, priority):
        self.name = name
        self.due = due
        self.priority = priority
        self.status = "Pending"


class Task:
    def __init__(self, task, due, priority):
        self.task = task
        self.due = due
        self.priority = priority
        self.status = "Pending"
        self.subtasks = []