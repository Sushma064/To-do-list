from imports import tk


def create_buttons(frame, actions):
    tk.Button(frame, text="Add Task",
              command=actions.add_task).grid(row=3, column=0)

    tk.Button(frame, text="Add SubTask",
              command=actions.add_subtask).grid(row=3, column=1)

    tk.Button(frame, text="Mark Completed",
              command=actions.mark_completed).grid(row=4, column=0)

    tk.Button(frame, text="Delete",
              command=actions.delete_item).grid(row=4, column=1)
