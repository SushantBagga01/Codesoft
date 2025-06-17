import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

class SimpleTodo:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Todo")
        self.root.geometry("600x400")
        
        self.tasks = []
        self.load_tasks()
        
        self.setup_ui()
    
    def setup_ui(self):
        # Input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Task:").pack(side=tk.LEFT)
        self.task_entry = tk.Entry(input_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=5)
        
        self.add_btn = tk.Button(input_frame, text="Add", command=self.add_task)
        self.add_btn.pack(side=tk.LEFT)
        
        # Task list
        self.listbox = tk.Listbox(self.root, width=60, height=15)
        self.listbox.pack(pady=10)
        
        # Buttons frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()
        
        self.complete_btn = tk.Button(btn_frame, text="Complete", command=self.mark_complete)
        self.complete_btn.pack(side=tk.LEFT, padx=5)
        
        self.delete_btn = tk.Button(btn_frame, text="Delete", command=self.delete_task)
        self.delete_btn.pack(side=tk.LEFT, padx=5)
        
        self.update_list()
    
    def load_tasks(self):
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as f:
                self.tasks = json.load(f)
    
    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f)
    
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            new_task = {
                'id': len(self.tasks) + 1,
                'text': task_text,
                'done': False,
                'created': datetime.now().strftime("%Y-%m-%d")
            }
            self.tasks.append(new_task)
            self.save_tasks()
            self.update_list()
            self.task_entry.delete(0, tk.END)
    
    def mark_complete(self):
        selection = self.listbox.curselection()
        if selection:
            task_id = int(self.listbox.get(selection[0]).split(":")[0])
            for task in self.tasks:
                if task['id'] == task_id:
                    task['done'] = True
                    break
            self.save_tasks()
            self.update_list()
    
    def delete_task(self):
        selection = self.listbox.curselection()
        if selection:
            task_id = int(self.listbox.get(selection[0]).split(":")[0])
            self.tasks = [task for task in self.tasks if task['id'] != task_id]
            self.save_tasks()
            self.update_list()
    
    def update_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task['done'] else " "
            self.listbox.insert(tk.END, f"{task['id']}: {task['text']} [{status}]")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleTodo(root)
    root.mainloop()