import tkinter as tk
from sympy.logic.boolalg import sympify, to_cnf


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("SimpleLogic")

        # Center the window on the screen
        self.declare_geometry()

        self.frames = {}
        self.show_frame("main")

    def declare_geometry(self):
        window_width = self.winfo_screenwidth() - 100
        window_height = self.winfo_screenheight() - 100
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_position = (screen_width) // 2 + 200
        y_position = (screen_height) // 2 + 200
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Configure columns and rows to center the content
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def get_text(self, text_widget_name):
        content = text_widget_name.get("1.0", tk.END)
        return content
    
    def clear_text(self, text_widget_name):
        text_widget_name.delete("1.0", tk.END)

    def show_frame(self, frame_name):
        """This function raises the frame given by the frame_name passed as an argument"""
        match frame_name:
            case "main":
                main_frame = MainFrame(self, self.show_frame)
                self.frames["main"] = main_frame
            case "Visualize":
                visualize_frame = Visualize(self)
                self.frames["Visualize"] = visualize_frame
            case "Simplify":
                simplify_frame = Simplify(self)
                self.frames["Simplify"] = simplify_frame

        frame = self.frames[frame_name]
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

class MainFrame(tk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent, bg="#292929")
        
        self.label1 = tk.Label(self, text="Welcome to Simple Logic!", bg="#292929", fg="#CCCCCC",font=("Helvetica", 30))
        self.label1.grid(row=0, column=0, padx=100, pady=10, columnspan=2, sticky="nsew")

        self.b1 = tk.Button(self, text="Visualize Expressions", bg="#008080", fg="white",font=("Helvetica", 22), width=25, command=lambda: show_frame("Visualize"))
        self.b1.grid(row=1, column=0, padx=200, pady=30, sticky="nsew")

        self.b2 = tk.Button(self, text="Simplify Expressions", bg="#800080", fg="white", font=("Helvetica", 22), width=15, command=lambda: show_frame("Simplify"))
        self.b2.grid(row=2, column=0, padx=200, pady=30, sticky="nsew")

        self.b3 = tk.Button(self, text="Quit Program", bg="#800000", fg="white", font=("Helvetica", 22), width=15, command=quit)
        self.b3.grid(row=3, column=0, padx=200, pady=30, sticky="nsew")

        # Configure columns and rows to center the content
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        # Center the label in the frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
    def quit():
        app.destroy()

class Visualize(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#292929")
        msg = """Use '|' for 'or', '&' for 'and' and '~' for the complement of a variable. Ex: ~A | A&B
        Or enter the minterms as a tuple followed by the don't care terms as a tuple Ex: (1,4,5,6,7) (0,8,9) """
        
        self.text_widget = tk.Text(self, height=2, width=70, font=70, bg="#292929", fg="white")
        self.text_widget.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Initialize instruction truth
        self.instruction_truth = False
        instruction_button = tk.Button(self, text="Instructions", bg = "#555555", fg="white", font=24, height=2, command= self.on_instruction_click)
        instruction_button.grid(row=1, column=3,  padx=10, pady=10, sticky ="we")

        # Create a button to get the content of the Text widget
        evaluate_button = tk.Button(self, text="Visualize Expression", font=24, height=2, bg="#008080", fg="white", command= self.on_evaluate_click)
        evaluate_button.grid(row=1, column=0,  padx=10, pady=10, sticky ="we")

        clear_entry_button = tk.Button(self, text="Clear Entry", bg="#555555", font=24, height=2, command= self.on_clear_click)
        clear_entry_button.grid(row=1, column=1, padx=10, pady=10, sticky ="we")

        self.message_label = tk.Label(self, text="", fg="#800000", bg="#292929", font=12)
        self.message_label.grid(row=2, column=0, pady=10, columnspan=2)

        go_back_button = tk.Button(self, text="Go Back", bg="#800000", fg="white", command= self.go_back)
        go_back_button.grid(row=0, column=3, pady=40, padx=20)

        # Frame for matplot lib figure
        self.plot_frame = tk.Frame(self, bg="red")
        self.plot_frame.grid(row=3, column=0, padx=10, pady=10, columnspan=4, rowspan=2, sticky="nsew")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=6)
        self.rowconfigure(4, weight=6)


    def on_evaluate_click(self):
        content = app.get_text(self.text_widget)
        
        try:
            # Attempt to parse the input as a boolean expression
            expression = sympify(content)
            return expression
        except:
            try:
                # Attempt to parse the input as two tuples
                
                tuple_strings = content.split()

                # Convert each tuple string to an actual tuple
                tuples = [tuple(map(int, s.strip('()').split(','))) for s in tuple_strings]
                msg = f"{tuples}"
                self.message_label.config(text=msg, fg="white")
                print("Tuples:", tuples)
                
            except:
                # If both attempts fail, raise an exception
                msg = """The expression you input in invalid. Please Check your syntax. See Instruction to see use of proper syntax."""
                self.message_label.config(text=msg,fg="red")
                # raise ValueError("Input does not match expected format")

            

    def on_clear_click(self):
        app.clear_text(self.text_widget)
        self.message_label.config(text="")

    def go_back(self):
        app.show_frame("main")
    
    def on_instruction_click(self):
        # Changing the instruction truth to its complement acts as a toggle for instructions
        self.instruction_truth = not self.instruction_truth
        if self.instruction_truth:
            msg = """Use '|' for 'or', '&' for 'and' and '~' for the complement of a variable. Ex: ~A | A&B
            Or enter the minterms as a tuple followed by the don't care terms as a tuple Ex: (1,4,5,6,7) (0,8,9) """
            self.message_label.config(text=msg, fg = "white")
        else:
            self.message_label.config(text="", fg = "white")

class Simplify(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#292929")
        
        self.text_widget = tk.Text(self, height=2, width=70, bg="#292929", fg="white")
        self.text_widget.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Intialize intruction truth
        self.instruction_truth = False
        instruction_button = tk.Button(self, text="Instructions", bg = "#555555", fg="white", font=24, height=2, command= self.on_instruction_click)
        instruction_button.grid(row=1, column=3,  padx=10, pady=10, sticky ="we")

        # Create a button to get the content of the Text widget
        evaluate_button = tk.Button(self, text="Visualize Expression", font=24, height=2, bg="#800080", fg="white", command= self.on_evaluate_click)
        evaluate_button.grid(row=1, column=0,  padx=10, pady=10, sticky ="we")

        clear_entry_button = tk.Button(self, text="Clear Entry", bg="#555555", font=24, height=2, command= self.on_clear_click)
        clear_entry_button.grid(row=1, column=1, padx=10, pady=10, sticky ="we")

        self.message_label = tk.Label(self, text="", fg="white", bg="#292929", font=12)
        self.message_label.grid(row=2, column=0, pady=10, columnspan=2)

        go_back_button = tk.Button(self, text="Go Back", bg="#800000", fg="white", command= self.go_back)
        go_back_button.grid(row=0, column=3, pady=40, padx=20)

        # Setup grid configuration
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=6)
        self.rowconfigure(4, weight=6)

    def on_evaluate_click(self):
        content = app.get_text(self.text_widget)
        
        try:
            # Attempt to parse the input as a boolean expression
            expression = sympify(content)
            self.message_label.config(text=content, fg="white")
        except:
            try:
                # Attempt to parse the input as two tuples
                
                tuple_strings = content.split()

                # Convert each tuple string to an actual tuple
                tuples = [tuple(map(int, s.strip('()').split(','))) for s in tuple_strings]
                msg = f"{tuples}"
                self.message_label.config(text=msg, fg="white")
                
                
            except:
                # If both attempts fail, raise an exception
                msg = """The expression you input in invalid. Please Check your syntax. See Instruction to see use of proper syntax."""
                self.message_label.config(text=msg,fg="red")
                # raise ValueError("Input does not match expected format")

    def on_clear_click(self):
        app.clear_text(self.text_widget)

    def go_back(self):
        app.show_frame("main")



app = App()
app.mainloop()
