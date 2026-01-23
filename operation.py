from tkinter import messagebox
from Data import Task, SubTask


class AddTask:
    def execute(self, tasks, name, due, priority):
        if name == "":
            messagebox.showerror("Error", "Enter task name")
            return
        tasks.append(Task(name, due, priority))


class AddSubTask:
    def execute(self, tasks, tree, name, due, priority):
        selected = tree.selection()
        if not selected or "_" in selected[0]:
            messagebox.showwarning("Error", "Select MAIN task")
            return
        index = int(selected[0]) - 1
        tasks[index].subtasks.append(SubTask(name, due, priority))


class MarkComplete:
    def execute(self, tasks, tree):
        selected = tree.selection()
        if not selected:
            return
        item = selected[0]
        if "_" in item:
            t, s = map(int, item.split("_"))
            tasks[t - 1].subtasks[s].status = "Completed"
        else:
            tasks[int(item) - 1].status = "Completed"


class DeleteItem:
    def execute(self, tasks, tree):
        selected = tree.selection()
        if not selected:
            return
        item = selected[0]
        if "_" in item:
            t, s = map(int, item.split("_"))
            tasks[t - 1].subtasks.pop(s)
        else:
            tasks.pop(int(item) - 1)
