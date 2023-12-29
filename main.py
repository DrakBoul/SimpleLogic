import tkinter as tk
from tkinter import font
from functions import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from timing_diagram_v1 import plot_timing_diagram

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
        
        custom_font_label = font.Font(family="Helvetica", size=14)
        
        self.text_widget = tk.Text(self, height=2, width=50, font=custom_font_label, bg="#292929", fg="white")
        self.text_widget.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Initialize instruction truth
        self.instruction_truth = False
        instruction_button = tk.Button(self, text="Instructions", bg = "#555555", fg="white", font=24, height=2, command= self.on_instruction_click)
        instruction_button.grid(row=1, column=3,  padx=10, pady=10, sticky ="we")

        # Create a button to get the content of the Text widget
        evaluate_button = tk.Button(self, text="Visualize Expression", font=24, height=2, bg="#008080", fg="white", command= self.on_evaluate_click)
        evaluate_button.grid(row=1, column=0,  padx=10, pady=10, sticky ="we")

        clear_entry_button = tk.Button(self, text="Clear", bg="#555555", font=24, height=2, command= self.on_clear_click)
        clear_entry_button.grid(row=1, column=1, padx=10, pady=10, sticky ="we")

        self.message_label = tk.Label(self, text="", fg="#800000", bg="#292929", font=12)
        self.message_label.grid(row=2, column=0, pady=10, columnspan=4)

        go_back_button = tk.Button(self, text="Go Back", bg="#800000", fg="white", font=24, height =2, command= self.go_back)
        go_back_button.grid(row=0, column=3, pady=40, padx=20, sticky="ew", )

        # Frame for matplot lib figure
        self.plot_frame = tk.Frame(self, bg="#292929")
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
            self.generate_matplotlib_plot(content)
        except Exception as e:
            print(e)
            msg = """The expression you input in invalid. Please Check your syntax. See Instruction to see use of proper syntax."""
            self.message_label.config(text=msg,fg="red")


    def generate_matplotlib_plot(self, content):
        # Clear any existing widgets in the plot_frame
        for widget in self.plot_frame.winfo_children():
            widget.destroy()
        expression, var_str = content.split(',')
        variables = var_str.split()
        
        fig, ax = plt.subplots( len(variables) + 1, 1, figsize=(10, 6), sharex=True)

        plot_timing_diagram(ax, variables, expression)

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)

    def on_clear_click(self):
        app.clear_text(self.text_widget)
        self.message_label.config(text="")
        for widget in self.plot_frame.winfo_children():
            widget.destroy()
        

    def go_back(self):
        app.show_frame("main")
    
    def on_instruction_click(self):
        # Changing the instruction truth to its complement acts as a toggle for instructions
        self.instruction_truth = not self.instruction_truth
        if self.instruction_truth:
            intructions = """
            Works for up to and including 6 variables. Use '|' for 'or', '&' for 'and' and '~' for the complement of a variable. 
            After entering your expression enter the variables used in your expression space seperated. Ex: ~A | A & B, A B
            """
            self.message_label.config(text=intructions, fg = "white")
        else:
            self.message_label.config(text="", fg = "white")

class Simplify(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#292929")
        
        # Intialize fonts
        custom_font_title = font.Font(family="Helvetica", size=20)
        custom_font_label = font.Font(family="Helvetica", size=14)

        self.text_widget = tk.Text(self, height=2, width=50, bg="#292929", fg="white", font=custom_font_label)
        self.text_widget.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Intialize intruction truth
        self.instruction_truth = False
        instruction_button = tk.Button(self, text="Instructions", bg = "#555555", fg="white", font=24, height=2, command= self.on_instruction_click)
        instruction_button.grid(row=1, column=2,  pady=40, padx=20, sticky="ew")

        # Create a button to get the content of the Text widget
        evaluate_button = tk.Button(self, text="Simplify Expression", font=24, height=2, bg="#800080", fg="white", command= self.on_evaluate_click)
        evaluate_button.grid(row=1, column=0,  padx=10, pady=10, sticky ="we")

        clear_entry_button = tk.Button(self, text="Clear", bg="#555555", font=24, height=2, command= self.on_clear_click)
        clear_entry_button.grid(row=1, column=1, padx=10, pady=10, sticky ="we")

        self.message_label = tk.Label(self, text="", fg="white", bg="#292929", font=12)
        self.message_label.grid(row=2, column=0, pady=10, columnspan=4, sticky="new")

        results_frame = tk.Frame(self, bg="#292929")
        results_frame.grid(row=3, column=0, columnspan=4, rowspan=2, sticky="nsew")
        # Wraplength is used to prevent overflow, it is specified in centimeters rather then screen units
        # to allow for a more consistent visual across devices of different resolution
        self.pos_label_title = tk.Label(results_frame, text="", fg="white", bg="#292929", font=custom_font_title, wraplength="10c")
        self.pos_label_title.grid(row=0, column=0, columnspan=2, sticky="nw")
        self.pos_label = tk.Label(results_frame, text="", fg="white", bg="#292929", font=custom_font_label)
        self.pos_label.grid(row=1, column=0, sticky="nw")
        self.pos_gate_count = tk.Label(results_frame, text="", fg="white", bg="#292929", font=custom_font_label)
        self.pos_gate_count.grid(row=2, column=0, sticky="nw")
        self.pos_input_count = tk.Label(results_frame, text="", fg="white", bg="#292929", font=custom_font_label)
        self.pos_input_count.grid(row=3, column=0, sticky="nw")

        self.sop_label_title = tk.Label(results_frame, text="", fg="white", bg="#292929", font=custom_font_title)
        self.sop_label_title.grid(row=0, column=1, sticky="nw")
        self.sop_label = tk.Label(results_frame, text="", fg="white", bg="#292929", font=custom_font_label, wraplength="10c")
        self.sop_label.grid(row=1, column=1, sticky="nw")
        self.sop_gate_count = tk.Label(results_frame, text="", fg="white", bg="#292929", font=custom_font_label)
        self.sop_gate_count.grid(row=2, column=1, sticky="nw")
        self.sop_input_count = tk.Label(results_frame, text="", fg="white", bg="#292929", font=custom_font_label)
        self.sop_input_count.grid(row=3, column=1, sticky="nw")

        go_back_button = tk.Button(self, text="Go Back", bg="#800000", fg="white", width=10, height =2, font=24, command= self.go_back)
        go_back_button.grid(row=0, column=2, pady=40, padx=20, sticky = "ew")

        # Setup grid configuration for Simplify frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=10)

        # Setup grid configuration for Results Frame
        results_frame.columnconfigure(0, weight=1)
        results_frame.columnconfigure(1, weight=1)
        results_frame.rowconfigure(0, weight=1)
        results_frame.rowconfigure(1, weight=1)
        results_frame.rowconfigure(2, weight=1)
        results_frame.rowconfigure(3, weight=1)
        

    def on_evaluate_click(self):
        content = app.get_text(self.text_widget)
        
        try:
            # Attempt to parse the input as a boolean expression
            
            pos_form = convert_to_pos(content)
            sop_form = convert_to_sop(content)
            pos_inputs = get_num_gate_inputs(pos_form)
            pos_gate_count = get_num_gates(pos_form)
            sop_inputs = get_num_gate_inputs(sop_form)
            sop_gate_count = get_num_gates(sop_form)

            self.pos_label_title.config(text="Minimized POS form:")
            self.pos_label.config(text=f"F= {pos_form}")
            self.pos_gate_count.config(text=f"Number of Gates used: {pos_gate_count}")
            self.pos_input_count.config(text=f"Number of inputs used: {pos_inputs}")


            self.sop_label_title.config(text="Minimized SOP form:")
            self.sop_label.config(text=f"F= {sop_form}")
            self.sop_gate_count.config(text=f"Number of Gates used: {sop_gate_count}")
            self.sop_input_count.config(text=f"Number of inputs used: {sop_inputs}")
         
                
        except Exception as e:
            print(e)
            msg = """The expression you input in invalid. Please Check your syntax. See Instruction to see use of proper syntax."""
            self.message_label.config(text=msg,fg="red")

    def on_clear_click(self):
        app.clear_text(self.text_widget)
        self.message_label.config(text="")
        self.pos_label_title.config(text="")
        self.pos_label.config(text="")
        self.pos_gate_count.config(text="")
        self.pos_input_count.config(text="")
        self.sop_label_title.config(text="")
        self.sop_label.config(text="")
        self.sop_gate_count.config(text="")
        self.sop_input_count.config(text="")


    def go_back(self):
        app.show_frame("main")

    def on_instruction_click(self):
        # Changing the instruction truth to its complement acts as a toggle for instructions
        self.instruction_truth = not self.instruction_truth
        if self.instruction_truth:
            intructions = """
            Works for up to and including 6 variables. Use '|' for 'or', '&' for 'and' and '~' for the complement of a variable. 
            After entering your expression enter the variables used in your expression space seperated. Ex: ~A | A & B, A B
            """
            self.message_label.config(text=intructions, fg = "white")
        else:
            self.message_label.config(text="", fg = "white")



app = App()
app.mainloop()
