import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x500")
        self.root.configure(bg="#1c1c1c")
        
        self.current_value = "0"
        
        # Display Screen
        self.display = tk.Label(
            root, 
            text=self.current_value, 
            anchor="e", 
            bg="#1c1c1c", 
            fg="white", 
            font=("Arial", 40), 
            padx=20, 
            pady=20
        )
        self.display.pack(expand=True, fill="both")
        
        # Grid Container for Buttons
        self.button_frame = tk.Frame(root, bg="#1c1c1c")
        self.button_frame.pack(expand=True, fill="both")
        
        # Configure row and column weights so they resize properly
        for i in range(5):
            self.button_frame.rowconfigure(i, weight=1)
        for j in range(4):
            self.button_frame.columnconfigure(j, weight=1)
            
        # Layout Matrix matching your image
        button_values = [
            ["AC", "+/-", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "√", "="]
        ]
        
        self.create_buttons(button_values)

    def create_buttons(self, matrix):
        for row_idx, row in enumerate(matrix):
            for col_idx, char in enumerate(row):
                # Determine colors based on position/character type
                if char in ["AC", "+/-", "%"]:
                    bg_color = "#d4d4d2"
                    fg_color = "black"
                elif char in ["÷", "×", "-", "+", "="]:
                    bg_color = "#f1a33c"
                    fg_color = "white"
                else:
                    bg_color = "#505050"
                    fg_color = "white"
                
                btn = tk.Button(
                    self.button_frame, 
                    text=char, 
                    bg=bg_color, 
                    fg=fg_color, 
                    font=("Arial", 20),
                    borderwidth=1,
                    relief="groove",
                    command=lambda x=char: self.on_button_click(x)
                )
                btn.grid(row=row_idx, column=col_idx, sticky="nsew")

    def on_button_click(self, char):
        if char == "AC":
            self.current_value = "0"
            
        elif char == "+/-":
            if self.current_value != "0":
                if self.current_value.startswith("-"):
                    self.current_value = self.current_value[1:]
                else:
                    self.current_value = "-" + self.current_value
                    
        elif char == "%":
            try:
                # Converts the current view value into a percentage evaluation
                self.current_value = str(float(self.current_value) / 100)
            except ValueError:
                self.current_value = "Error"
                
        elif char == "√":
            try:
                val = float(self.current_value)
                if val >= 0:
                    self.current_value = str(math.sqrt(val))
                else:
                    self.current_value = "Error"
            except ValueError:
                self.current_value = "Error"
                
        elif char == "=":
            try:
                # Replace visual symbols with valid Python operators
                expression = self.current_value.replace("÷", "/").replace("×", "*")
                result = eval(expression)
                # Convert to integer if it's a whole number for cleaner display
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                self.current_value = str(result)
            except Exception:
                self.current_value = "Error"
                
        else: # Number or standard operator (+, -, ×, ÷, .)
            if self.current_value == "0" and char not in ["+", "-", "÷", "×", "."]:
                self.current_value = char
            else:
                # Prevent consecutive operators to avoid math errors
                if char in ["+", "-", "÷", "×"] and self.current_value[-1] in ["+", "-", "÷", "×"]:
                    self.current_value = self.current_value[:-1] + char
                else:
                    self.current_value += char
                    
        self.update_display()

    def update_display(self):
        # Truncate strings that get too long for visual neatness
        if len(self.current_value) > 12:
            self.display.config(text=self.current_value[:12])
        else:
            self.display.config(text=self.current_value)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()