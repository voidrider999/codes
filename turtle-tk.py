# TODO color picker (fg, bg)
# TODO очистить канвас
# TODO undo

import tkinter as tk
from tkinter import ttk
from turtle import RawTurtle
from PIL import Image
from io import BytesIO

def draw_absolute():
    turtle.getscreen().colormode(255)
    turtle.pencolor((red.get(), green.get(), blue.get()))
    turtle.setheading(heading.get())
    turtle.forward(length.get())
    x, y = int(turtle.xcor()), int(turtle.ycor())
    rgb = (red.get(), green.get(), blue.get())
    print(f'x:{x}, y:{y}, heading:{heading.get()}, RGB:{rgb}')

def tab_absolute_mode(parent):
    frame = ttk.Frame(parent)

    label = ttk.Label(frame, text='Длина')
    label.pack()
    length_sb = ttk.Spinbox(frame, textvariable=length, from_=-100, to=100,
         increment=1)
    length_sb.pack()

    def on_heading_click():
        turtle.setheading(heading.get())

    label = ttk.Label(frame, text='Поворот')
    label.pack()
    heading_sb = ttk.Spinbox(frame, textvariable=heading, from_=-360, to=360, 
        increment=5, command=on_heading_click)
    heading_sb.pack()

    label = ttk.Label(frame, text='Red')
    label.pack()
    red_sb = ttk.Spinbox(frame, textvariable=red, from_=0, to=255, increment=1)
    red_sb.pack()

    label = ttk.Label(frame, text='Green')
    label.pack()
    green_sb = ttk.Spinbox(frame, textvariable=green, from_=0, to=255, increment=1)
    green_sb.pack()

    label = ttk.Label(frame, text='Blue')
    label.pack()
    blue_sb = ttk.Spinbox(frame, textvariable=blue, from_=0, to=255, increment=1)
    blue_sb.pack()

    def on_draw_click():
        draw_absolute()

    draw_btn = ttk.Button(frame, text='Рисовать', command=on_draw_click)
    draw_btn.pack(pady=5)

    return frame

def tab_relative_mode(parent):
    frame = ttk.Frame(parent)

    label = ttk.Label(frame, text='Длина')
    label.pack()
    length_sb = ttk.Spinbox(frame, from_=-100, to=100, increment=1)
    length_sb.set(0)
    length_sb.pack()

    label = ttk.Label(frame, text='Поворот')
    label.pack()
    heading_sb = ttk.Spinbox(frame, from_=-360, to=360, increment=5)
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
        length.set(length.get() + int(length_sb.get()))
        heading.set((heading.get() + int(heading_sb.get())) % 360)
        red.set((red.get() + int(red_sb.get())) % 256)
        green.set((green.get() + int(green_sb.get())) % 256)
        blue.set((blue.get() + int(blue_sb.get())) % 256)
        draw_absolute()

    draw_btn = ttk.Button(frame, text='Рисовать', command=on_draw_click)
    draw_btn.pack(pady=5)

    return frame

def frame_buttons():
    frame = ttk.Frame() 

    def on_save_click():
        canvas.update()
        eps = canvas.postscript(colormode='color')
        im = Image.open(BytesIO(bytes(eps, 'ascii')))
        im.save('result.png')

    save_btn = ttk.Button(frame, text='Сохранить', command=on_save_click)
    save_btn.pack()

    def on_back_click():
        canvas.update()
        w, h = canvas.winfo_width(), canvas.winfo_height()
        window_caption_h = 15

        move_counter = 0
        while True:
            x, y = int(turtle.xcor()), int(turtle.ycor())
            print(x, y, w, h)
            if x > -w/2 and x < w/2 and y > -h/2 and y < h/2 - window_caption_h:
                break
            turtle.backward(1)

            move_counter += 1
            if move_counter > 110:
                turtle.teleport(0, 0)
                break

    back_btn = ttk.Button(frame, text='Вернуться', command=on_back_click)
    back_btn.pack()

    return frame

root = tk.Tk()
root.eval('tk::PlaceWindow . center')

length = tk.IntVar(value=10)
heading = tk.IntVar(value=0)
red = tk.IntVar(value=0)
green = tk.IntVar(value=0)
blue = tk.IntVar(value=0)

# создать виджеты верхнего уровня
mode_nb = ttk.Notebook()
mode_nb.add(tab_absolute_mode(mode_nb), text='Абсолютный')
mode_nb.add(tab_relative_mode(mode_nb), text='Относительный')
btn_frame = frame_buttons()
canvas = tk.Canvas()

# разместить виджеты верхнего уровня
for r in range(2):
    root.rowconfigure(index=r, weight=1)
for c in range(2):
    root.columnconfigure(index=c, weight=1)
mode_nb.grid(row=0, column=0)
btn_frame.grid(row=1, column=0)
# sticky=nswe растягивает виджет на всю ячейку (с севера на юг и с запада
# на восток)
canvas.grid(row=0, column=1, rowspan=2, sticky='nswe')

turtle = RawTurtle(canvas)
root.mainloop()
