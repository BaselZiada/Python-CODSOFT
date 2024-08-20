import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description, due_date, subject, priority):
        self.description = description
        self.due_date = due_date
        self.subject = subject
        self.priority = priority
        self.completed = False

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{self.subject}] {self.description} - Due: {self.due_date} - Priority: {self.priority} - Status: {status}"

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-do list at University")

        self.tasks = []

        # UI setup with frames and widgets
        self.frame = tk.Frame(root, bg="#8B0000")
        self.frame.pack(padx=10, pady=10)

        self.task_label = tk.Label(self.frame, text="Task Description(Name):", bg="lightblue")
        self.task_label.grid(row=0, column=0)

        self.task_entry = tk.Entry(self.frame, width=60)
        self.task_entry.grid(row=0, column=1)

        self.date_label = tk.Label(self.frame, text="Due Date (YYYY-MM-DD):", bg="lightblue")
        self.date_label.grid(row=1, column=0)

        self.date_entry = tk.Entry(self.frame, width=60)
        self.date_entry.grid(row=1, column=1)

        self.subject_label = tk.Label(self.frame, text="Subject:", bg="lightblue")
        self.subject_label.grid(row=2, column=0)

        self.subject_entry = tk.Entry(self.frame, width=60)
        self.subject_entry.grid(row=2, column=1)

        self.priority_label = tk.Label(self.frame, text="Priority (High, Medium, Low):", bg="lightblue")
        self.priority_label.grid(row=3, column=0)

        self.priority_entry = tk.Entry(self.frame, width=60)
        self.priority_entry.grid(row=3, column=1)

        self.add_button = tk.Button(self.frame, text="Add Tasks", command=self.add_task, bg="blue", fg="white")
        self.add_button.grid(row=4, columnspan=2, pady=5)

        self.listbox = tk.Listbox(self.frame, width=100, height=15)
        self.listbox.grid(row=5, columnspan=2, pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task, bg="red", fg="white")
        self.delete_button.grid(row=6, column=0)

        self.complete_button = tk.Button(self.frame, text="Mark as Completed", command=self.mark_as_completed, bg="blue", fg="white")
        self.complete_button.grid(row=6, column=1)

        self.sort_date_button = tk.Button(self.frame, text="Sort by Date", command=self.sort_by_date, bg="orange", fg="white")
        self.sort_date_button.grid(row=7, column=0)

        self.sort_priority_button = tk.Button(self.frame, text="Sort by Priority", command=self.sort_by_priority, bg="purple", fg="white")
        self.sort_priority_button.grid(row=7, column=1)

    def add_task(self):
        description = self.task_entry.get()
        due_date = self.date_entry.get()
        subject = self.subject_entry.get()
        priority = self.priority_entry.get()

        if description and due_date and subject and priority:
            task = Task(description, due_date, subject, priority)
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.subject_entry.delete(0, tk.END)
            self.priority_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_as_completed(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]].completed = True
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = str(task)
            self.listbox.insert(tk.END, display_text)
            if task.completed:
                self.listbox.itemconfig(tk.END, {'bg': 'lightgreen'})
            elif task.priority.lower() == 'high':
                self.listbox.itemconfig(tk.END, {'bg': 'salmon'})
            elif task.priority.lower() == 'medium':
                self.listbox.itemconfig(tk.END, {'bg': 'lightyellow'})
            else:
                self.listbox.itemconfig(tk.END, {'bg': 'lightgrey'})

    def sort_by_date(self):
        self.tasks.sort(key=lambda task: task.due_date)
        self.update_listbox()

    def sort_by_priority(self):
        priority_order = {'high': 1, 'medium': 2, 'low': 3}
        self.tasks.sort(key=lambda task: priority_order.get(task.priority.lower(), 4))
        self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
