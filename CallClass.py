from operation import AddTask, AddSubTask, MarkComplete, DeleteItem


class Actions:
    def __init__(self, tasks, tree, name_entry, due_entry, priority):
        self.tasks = tasks
        self.tree = tree
        self.name_entry = name_entry
        self.due_entry = due_entry
        self.priority = priority

        self.add_task_op = AddTask()
        self.add_subtask_op = AddSubTask()
        self.mark_op = MarkComplete()
        self.delete_op = DeleteItem()

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        for i, t in enumerate(self.tasks, 1):
            self.tree.insert("", "end", iid=str(i), text=t.name,
                             values=(t.due, t.priority, t.status))
            for j, s in enumerate(t.subtasks):
                self.tree.insert(str(i), "end", iid=f"{i}_{j}",
                                 text=s.name,
                                 values=(s.due, s.priority, s.status))

    def add_task(self):
        self.add_task_op.execute(
            self.tasks,
            self.name_entry.get(),
            self.due_entry.get(),
            self.priority.get()
        )
        self.refresh()

    def add_subtask(self):
        self.add_subtask_op.execute(
            self.tasks,
            self.tree,
            self.name_entry.get(),
            self.due_entry.get(),
            self.priority.get()
        )
        self.refresh()

    def mark_completed(self):
        self.mark_op.execute(self.tasks, self.tree)
        self.refresh()

    def delete_item(self):
        self.delete_op.execute(self.tasks, self.tree)
        self.refresh()
