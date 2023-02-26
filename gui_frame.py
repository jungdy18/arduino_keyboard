import tkinter
import tkinter.ttk
from math import ceil

from sys import exit as end


class KeyMapper:
    def __init__(self, master=tkinter.Tk()):
        # Main Window
        self.master = master
        self.master.title("virtual keyboard")
        self.gray = "#383838"
        self.master.configure(bg=self.gray)
        self.user_scr_width = int(self.master.winfo_screenwidth()) * 0.78
        self.user_scr_height = int(self.master.winfo_screenheight()) * 0.70
        self.master.resizable(False, False)
        self.master.geometry(f"{int(self.user_scr_width)}x{int(self.user_scr_height)}")
        self.master.attributes('-topmost', True)

    def place_note(self,dict_keys,dict_values):
        notebook = tkinter.ttk.Notebook(self.master, height = 200)
        notebook.pack(side = "bottom", anchor = "w", fill = "x")
        for i in range(len(dict_keys)):
            frame = tkinter.Frame(notebook, height = 200)
            detail_frame = ScrollableFrame(frame)
            keys = dict_values[i]
            key_frame_height = ceil(len(keys)/18)*self.user_scr_height*0.095
            self.key_list(detail_frame.scrollable_frame,key_frame_height,keys).pack(padx = self.user_scr_width*0.04)
            detail_frame.pack(fill="both")
            frame.pack()
            notebook.add(frame, text=dict_keys[i])

    def key_list(self,frame,h,key_list):
        key_array = tkinter.Frame(frame, width = self.user_scr_width*0.95 ,height =h)
        x_pos = self.user_scr_width*0.025
        y_pos = self.user_scr_height*0.025
        offset = self.user_scr_height*0.085
        for key in key_list:
            x_pos = x_pos + offset
            if x_pos>self.user_scr_width*0.8:
                y_pos = y_pos + offset
                x_pos = self.user_scr_width*0.025 + offset
            self.key_button(key_array,key).place(x=x_pos,y=y_pos, width = self.user_scr_width*0.03, height=self.user_scr_width*0.03)
        return key_array

    def key_button(self, frame ,key):
        if len(key)==1:
                button = tkinter.Button(frame,text = key[0], overrelief="solid", anchor="w", bg= "pink")
        else:
                button = tkinter.Button(frame,text = (key[0]+"\n   "+key[1]), overrelief="solid", anchor="w", bg= "pink")
        return button

    def start(self):
        self.master.mainloop()

class ScrollableFrame(tkinter.ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tkinter.Canvas(self)
        scrollbar = tkinter.ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tkinter.ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")



keyboard = KeyMapper()
note_list = ["sex","sex","sex"]


alphabet = [["A/ㅁ"],["B","ㅠ"],["/"],["⏎"]]
number = [["1","!"],["2","@"],["3","#"]]
dictionary = {"alphabet":alphabet, "number":number}

keyboard.place_note(list(dictionary.keys()),list(dictionary.values()))

keyboard.start()