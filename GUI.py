from imports import tk, ttk
from Treeview import create_treeview
from Button import create_buttons
from CallClass import Actions


class ToDoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="Task Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(frame, text="Due Date").grid(row=1, column=0)
        self.due_entry = tk.Entry(frame)
        self.due_entry.grid(row=1, column=1)

        self.priority = ttk.Combobox(
            frame, values=["High", "Medium", "Low"], state="readonly"
        )
        self.priority.set("Medium")
        self.priority.grid(row=2, column=1)

        self.tree = create_treeview(root)

        self.actions = Actions(
            self.tasks,
            self.tree,
            self.name_entry,
            self.due_entry,
            self.priority
        )

        create_buttons(frame, self.actions)
