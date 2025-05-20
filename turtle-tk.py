# TODO color picker (fg, bg)

import tkinter as tk
from tkinter import ttk
from turtle import RawTurtle
from PIL import Image
from io import BytesIO

root = tk.Tk()
root.eval('tk::PlaceWindow . center')

frame = ttk.Frame(padding=(2, 2))

label = ttk.Label(frame, text='Длина')
label.pack()
length_sb = ttk.Spinbox(frame, from_=-100, to=100, increment=1)
length_sb.set(10)
length_sb.pack()

def on_heading_click():
    turtle.setheading(int(heading_sb.get()))

label = ttk.Label(frame, text='Поворот')
label.pack()
heading_sb = ttk.Spinbox(frame, from_=-360, to=360, increment=5,
    command=on_heading_click)
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
    turtle.setheading(int(heading_sb.get()))
    turtle.forward(int(length_sb.get()))
    x, y = int(turtle.xcor()), int(turtle.ycor())
    print(f'curx:{x}, cury:{y}')

draw_btn = ttk.Button(frame, text='Рисовать', command=on_draw_click)
draw_btn.pack(pady=5)

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
