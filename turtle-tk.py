import tkinter as tk
from tkinter import ttk
from turtle import RawTurtle

root = tk.Tk()
root.geometry("250x500")
root.eval('tk::PlaceWindow . center')

label = ttk.Label(text='Длина')
label.pack()
length_sb = ttk.Spinbox(from_=1, to=100, increment=1)
length_sb.set(1)
length_sb.pack()

label = ttk.Label(text='Поворот')
label.pack()
heading_sb = ttk.Spinbox(from_=-360, to=360, increment=10)
heading_sb.set(0)
heading_sb.pack()

label = ttk.Label(text='Red')
label.pack()
red_sb = ttk.Spinbox(from_=0, to=255, increment=1)
red_sb.set(0)
red_sb.pack()

label = ttk.Label(text='Green')
label.pack()
green_sb = ttk.Spinbox(from_=0, to=255, increment=1)
green_sb.set(0)
green_sb.pack()

label = ttk.Label(text='Blue')
label.pack()
blue_sb = ttk.Spinbox(from_=0, to=255, increment=1)
blue_sb.set(0)
blue_sb.pack()

def draw():
    turtle.setheading(int(heading_sb.get()))
    turtle.getscreen().colormode(255)
    turtle.pencolor((
        int(red_sb.get()),
        int(green_sb.get()),
        int(blue_sb.get()),
    ))
    turtle.forward(int(length_sb.get()))

draw_btn = ttk.Button(text='Draw', command=draw)
draw_btn.pack()

canvas = tk.Canvas(width=250, height=250)
canvas.pack()

turtle = RawTurtle(canvas)
print(turtle.xcor(), turtle.ycor())

root.mainloop()
