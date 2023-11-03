import tkinter as tk
from tkinter import ttk
from pynput import keyboard
from math import log2

# TODO <remove>
from icecream import ic
# TODO </remove>

from data import data

def app():
    def create_grid_square(row, col, value):
        colors = ['00', '19', '32', '4b', '64', '7d', '96', 'af', 'c8', 'e1', 'fa', 'ff']
        
        s = ttk.Style()
        s.configure('wrap.TFrame', background="#ddd")
        s.configure('frame.TFrame', background="#ff0")
        s.configure('frameNone.TFrame', background="#eee")
        for i in range(11):
            s.configure(f'frame{2**(i+1)}.TFrame', background=f"#ff{colors[i]}00")
        wrapper = ttk.Frame(
            master=bottom_section,
            width=68,
            height=68,
            style='wrap.TFrame',
        )
        wrapper.grid(row=row, column=col)

        value2 = value if value == None or value <= 2048 else ""
        squer_frame = ttk.Frame(
            master=wrapper,
            width=60,
            height=60,
            style=f'frame{value2}.TFrame',
        )
        squer_frame.place(relx=0.5, rely=0.5, anchor='center')

        value3 = 0 if value == None else int(log2(value))-1 if value<=2048 else -1
        bg = f"#ff{colors[value3]}00" if value != None else "#eee"
        label = ttk.Label(
            master=wrapper,
            text=f"{value if value != None else ''}",
            font=('Arial', 16, ),
            background=f"{bg}",
            
        )
        label.place(relx=0.5, rely=0.5, anchor='center')

    window = tk.Tk()
    window.title("copy of 2048 game")
    window.geometry("300x400+0+0")
    score_bar = ttk.Label(
        master=window,
        text=f"score: {data['score']}",
        font=('Arial', 16, ),
        # width=300,
    )
    score_bar.pack()
    highscore_bar = ttk.Label(
        master=window,
        text=f"highscore: {data['highscore']}",
        font=('Arial', 16, ),
        # width=300,
    )
    highscore_bar.pack()
    bottom_section = ttk.Frame(
        master=window,
        width=300,
        height=300
    )
    bottom_section.pack()
    
    for i in range(4):
        for j in range(4):
            create_grid_square(i, j, data['map'][j][i])

    window.update()    
    with keyboard.Events() as events:
        is_running = True
        while is_running:
            event = events.get()
            if type(event) == keyboard.Events.Press:
                for i in range(4):
                    for j in range(4):
                        create_grid_square(i, j, data['map'][j][i])
                score_bar.config(text=f"score: {data['score']}")
                window.update()
            if event.key == keyboard.Key.esc:
                is_running = False
