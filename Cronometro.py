import tkinter as tk

class Stopwatch:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Cronômetro")

        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.running = False

        self.time_label = tk.Label(self.window, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack()

        self.start_button = tk.Button(self.window, text="Iniciar", command=self.start)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.window, text="Parar", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(self.window, text="Resetar", command=self.reset)
        self.reset_button.pack(side=tk.LEFT)

    def update_time(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1

            time_str = f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
            self.time_label.config(text=time_str)
            self.window.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        if not self.running:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
            self.time_label.config(text="00:00:00")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.run()
