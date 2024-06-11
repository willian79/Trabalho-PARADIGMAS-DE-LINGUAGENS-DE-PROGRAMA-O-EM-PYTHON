import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculadora de IMC")

        self.create_widgets()
    
    def create_widgets(self):
        # Rótulo e entrada para altura
        self.height_label = tk.Label(self.window, text="Altura (m):")
        self.height_label.grid(row=0, column=0, padx=10, pady=10)
        self.height_entry = tk.Entry(self.window)
        self.height_entry.grid(row=0, column=1, padx=10, pady=10)

        # Rótulo e entrada para peso
        self.weight_label = tk.Label(self.window, text="Peso (kg):")
        self.weight_label.grid(row=1, column=0, padx=10, pady=10)
        self.weight_entry = tk.Entry(self.window)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)

        # Botão para calcular o IMC
        self.calculate_button = tk.Button(self.window, text="Calcular IMC", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, columnspan=2, pady=10)

        # Rótulo para exibir o resultado
        self.result_label = tk.Label(self.window, text="Seu IMC: ")
        self.result_label.grid(row=3, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            bmi = weight / (height ** 2)
            self.result_label.config(text=f"Seu IMC: {bmi:.2f}")
            self.show_bmi_category(bmi)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para altura e peso.")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            category = "Peso normal"
        elif 25 <= bmi < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        messagebox.showinfo("Categoria de IMC", f"Seu IMC é {bmi:.2f}, que está na categoria: {category}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = BMICalculator()
    app.run()
