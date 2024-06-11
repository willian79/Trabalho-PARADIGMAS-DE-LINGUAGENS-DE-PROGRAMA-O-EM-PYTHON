import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Lista de Tarefas")
        
        self.tasks = []

        self.create_widgets()
    
    def create_widgets(self):
        # Rótulo para a entrada de tarefa
        self.task_label = tk.Label(self.window, text="Digite uma tarefa:")
        self.task_label.grid(row=0, column=0, padx=10, pady=10)

        # Entrada para a tarefa
        self.task_entry = tk.Entry(self.window, width=50)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)

        # Botão para adicionar tarefa
        self.add_task_button = tk.Button(self.window, text="Adicionar Tarefa", command=self.add_task)
        self.add_task_button.grid(row=0, column=2, padx=10, pady=10)

        # Lista de tarefas
        self.tasks_listbox = tk.Listbox(self.window, width=50, height=15)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botão para remover tarefa
        self.remove_task_button = tk.Button(self.window, text="Remover Tarefa", command=self.remove_task)
        self.remove_task_button.grid(row=1, column=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Você deve digitar uma tarefa.")

    def remove_task(self):
        try:
            task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[task_index]
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Aviso", "Você deve selecionar uma tarefa para remover.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ToDoListApp()
    app.run()
