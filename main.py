import tkinter as tk

from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame


class App(tb.Window):
    def __init__(self):
        super().__init__()

        self.title("SimpleLogic")
        self.geometry("3000x2000")
        self.frames = {}
        self.show_frame("main")



    def show_frame(self, frame_name):
# add frames to blank spaces
            match frame_name:
                case "main":
                    main_frame = MainFrame(self, self.show_frame)
                    self.frames["main"] = main_frame
                case "add expressions":
                    main_frame = AddExpressions(self, self.show_frame)
                    self.frames["add expressions"] = main_frame
                
            frame = self.frames[frame_name]
            frame.grid(row=0, column=0, sticky="nsew")
            frame.tkraise()

class MainFrame(tb.Frame):
    def __init__(self, parent, show_frame):
        super().__init__(parent)

        self.label1 = tb.Label(self, text="Welcome to Simple Logic!", font=("Helvetica", 30), bootstyle="default")
        self.label1.grid(row=0, column=0, padx=200, pady=200, columnspan=2, sticky="nsew")
        self.b1 = tb.Button(self, text="Add Expressions", bootstyle="success, outline", command=lambda: show_frame("add expressions"))
        self.b1.grid(row=1, column=0, padx = 200, pady=200)


class AddExpressions(tb.Frame):
     def __init__(self, parent, show_frame):
          super().__init__(parent)


app = App()
app.mainloop()
