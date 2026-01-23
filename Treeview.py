from imports import ttk


def create_treeview(root):
    tree = ttk.Treeview(
        root, columns=("Due", "Priority", "Status"), show="tree headings"
    )
    tree.heading("#0", text="Task / SubTask")
    tree.heading("Due", text="Due Date")
    tree.heading("Priority", text="Priority")
    tree.heading("Status", text="Status")
    tree.pack(fill="both", expand=True, pady=10)
    return tree
