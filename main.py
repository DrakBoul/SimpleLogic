import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("SimpleLogic")

        # Center the window on the screen
        window_width = self.winfo_screenwidth() - 100
        window_height = self.winfo_screenheight() - 100
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_position = (screen_width) // 2 + 200
        y_position = (screen_height) // 2 + 200
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.frames = {}
        self.show_frame("main")

        # Configure columns and rows to center the content
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def show_frame(self, frame_name):
        """This function raises the frame given by the frame_name passed as an argument"""
        match frame_name:
            case "main":
                main_frame = MainFrame(self, self.show_frame)
                self.frames["main"] = main_frame
            case "Visualize":
                visualize_frame = Visualize(self, self.show_frame)
                self.frames["Visualize"] = visualize_frame
            case "Simplify":
                simplify_frame = Simplify(self, self.show_frame)
                self.frames["Simplify"] = simplify_frame
        frame = self.frames[frame_name]
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

class MainFrame(tk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)

        self.label1 = tk.Label(self, text="Welcome to Simple Logic!", font=("Helvetica", 30))
        self.label1.grid(row=0, column=0, padx=100, pady=10, columnspan=2, sticky="nsew")

        self.b1 = tk.Button(self, text="Visualize Expressions", font=("Helvetica", 22), width=25, command=lambda: show_frame("Visualize"))
        self.b1.grid(row=1, column=0, padx=200, pady=50, sticky="nsew")

        self.b2 = tk.Button(self, text="Simplify Expressions", font=("Helvetica", 22), width=15, command=lambda: show_frame("Simplify"))
        self.b2.grid(row=2, column=0, padx=200, pady=50, sticky="nsew")

        # Configure columns and rows to center the content
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # Center the label in the frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

class Visualize(tk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)

class Simplify(tk.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)
        
app = App()
app.mainloop()
