import tkinter as tk
from tkinter import ttk
from turtle import RawTurtle

red = 0
green = 0
blue = 0
angle = 0
length = 0

root = tk.Tk()
root.geometry("250x500")
root.eval('tk::PlaceWindow . center')

label = ttk.Label(text='Длина')
label.pack()
length_sb = ttk.Spinbox(from_=0, to=100, increment=1)
length_sb.set(length)
length_sb.pack()

label = ttk.Label(text='Поворот')
label.pack()
angle_sb = ttk.Spinbox(from_=0, to=360, increment=10)
angle_sb.set(angle)
angle_sb.pack()

label = ttk.Label(text='Red')
label.pack()
red_sb = ttk.Spinbox(from_=0, to=255, increment=1)
red_sb.set(red)
red_sb.pack()

label = ttk.Label(text='Green')
label.pack()
green_sb = ttk.Spinbox(from_=0, to=255, increment=1)
green_sb.set(green)
green_sb.pack()

label = ttk.Label(text='Blue')
label.pack()
blue_sb = ttk.Spinbox(from_=0, to=255, increment=1)
blue_sb.set(blue)
blue_sb.pack()

def draw():
    turtle.forward(10)

draw_btn = ttk.Button(text='Draw', command=draw)
draw_btn.pack()

canvas = tk.Canvas(width=250, height=250)
canvas.pack()

turtle = RawTurtle(canvas)
print(turtle.xcor(), turtle.ycor())

root.mainloop()
