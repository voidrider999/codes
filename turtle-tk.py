# TODO return to canvas when moved out of it
# TODO color picker (fg, bg)
# TODO turn turtle in real time

import tkinter as tk
from tkinter import ttk
from turtle import RawTurtle

root = tk.Tk()
root.eval('tk::PlaceWindow . center')

frame = ttk.Frame(padding=(2, 2))

label = ttk.Label(frame, text='Длина')
label.pack()
length_sb = ttk.Spinbox(frame, from_=1, to=100, increment=1)
length_sb.set(1)
length_sb.pack()

def on_heading_validate():
#    turtle.setheading(int(heading_sb.get()))
    print('okay')
    return True

label = ttk.Label(frame, text='Поворот')
label.pack()
heading_sb = ttk.Spinbox(
    frame,
    from_=-360,
    to=360,
    increment=10,
    validate='focusout',
    validatecommand=on_heading_validate,
)
heading_sb.set(0)
heading_sb.pack()

label = ttk.Label(frame, text='Red')
label.pack()
red_sb = ttk.Spinbox(frame, from_=0, to=255, increment=1)
red_sb.set(0)
red_sb.pack()

label = ttk.Label(frame, text='Green')
label.pack()
green_sb = ttk.Spinbox(frame, from_=0, to=255, increment=1)
green_sb.set(0)
green_sb.pack()

label = ttk.Label(frame, text='Blue')
label.pack()
blue_sb = ttk.Spinbox(frame, from_=0, to=255, increment=1)
blue_sb.set(0)
blue_sb.pack()

def on_draw_click():
    turtle.getscreen().colormode(255)
    turtle.pencolor((
        int(red_sb.get()),
        int(green_sb.get()),
        int(blue_sb.get()),
    ))
    turtle.forward(int(length_sb.get()))

draw_btn = ttk.Button(frame, text='Draw', command=on_draw_click)
draw_btn.pack()

canvas = tk.Canvas()

# если не указать вес, то он не растянет ячейки грида по ширине и высоте
# даже если ряд всего один, вес указывать нужно
root.rowconfigure(index=0, weight=1)
for c in range(2): root.columnconfigure(index=c, weight=1)
frame.grid(row=0, column=0)
# sticky=nswe растягивает виджет на всю ячейку (с севера на юг и с запада
# на восток)
canvas.grid(row=0, column=1, sticky='nswe')

turtle = RawTurtle(canvas)
root.mainloop()
