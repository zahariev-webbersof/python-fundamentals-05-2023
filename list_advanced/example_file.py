import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('SoftUni Calculator')

        self.entry = tk.Entry(self.window, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()
        self.position_buttons()

    def create_buttons(self):
        button_text = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            ">", "<", "C", "^   "

        ]

        self.buttons = []
        colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightpink']

        for index, text in enumerate(button_text):
            button = tk.Button(self.window, text=text, padx=40, pady=20, command=lambda t=text: self.button_click(t), bg=colors[index % len(colors)])
            self.buttons.append(button)

    def position_buttons(self):
        row = 1
        col = 0
        for button in self.buttons:
            button.grid(row=row, column=col)
            col += 1

            if col > 3:
                col = 0
                row += 1

    def button_click(self, text):
        current = self.entry.get()
        if text == '=':
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, 'Error')
        elif text == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, text)

    def run(self):
        self.window.mainloop()

calculator = Calculator()
calculator.run()
