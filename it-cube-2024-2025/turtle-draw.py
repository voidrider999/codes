import tkinter as tk
from tkinter import ttk
from turtle import RawTurtle
from PIL import Image
from io import BytesIO

def draw_manual():
    turtle.getscreen().colormode(255)
    turtle.pencolor((red.get(), green.get(), blue.get()))
    turtle.setheading(heading.get())
    turtle.forward(length.get())
    x, y = int(turtle.xcor()), int(turtle.ycor())
    rgb = (red.get(), green.get(), blue.get())
    print(f'x:{x}, y:{y}, heading:{heading.get()}, RGB:{rgb}')

def draw_repeat(length_diff, heading_diff, red_diff, green_diff, blue_diff):
    length.set(length.get() + length_diff)
    heading.set((heading.get() + heading_diff) % 360)

    newr = min(red.get() + red_diff, 255)
    red.set(max(newr, 0))

    newg = min(green.get() + green_diff, 255)
    green.set(max(newg, 0))

    newb = min(blue.get() + blue_diff, 255)
    blue.set(max(newb, 0))

    draw_manual()

def tab_manual_mode(parent):
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

    label = ttk.Label(frame, text='Красный')
    label.pack()
    red_sb = ttk.Spinbox(frame, textvariable=red, from_=0, to=255, increment=1)
    red_sb.pack()

    label = ttk.Label(frame, text='Зеленый')
    label.pack()
    green_sb = ttk.Spinbox(frame, textvariable=green, from_=0, to=255, increment=1)
    green_sb.pack()

    label = ttk.Label(frame, text='Синий')
    label.pack()
    blue_sb = ttk.Spinbox(frame, textvariable=blue, from_=0, to=255, increment=1)
    blue_sb.pack()

    def on_draw_click():
        draw_manual()

    draw_btn = ttk.Button(frame, text='Рисовать', command=on_draw_click)
    draw_btn.pack(pady=5)

    return frame

def tab_repeat_mode(parent):
    frame = ttk.Frame(parent)

    label = ttk.Label(frame, text='Изменение длины')
    label.pack()
    length_sb = ttk.Spinbox(frame, from_=-100, to=100, increment=1)
    length_sb.set(0)
    length_sb.pack()

    label = ttk.Label(frame, text='Изменение поворота')
    label.pack()
    heading_sb = ttk.Spinbox(frame, from_=-360, to=360, increment=5)
    heading_sb.set(0)
    heading_sb.pack()

    label = ttk.Label(frame, text='Изменение красного')
    label.pack()
    red_sb = ttk.Spinbox(frame, from_=-255, to=255, increment=1)
    red_sb.set(0)
    red_sb.pack()

    label = ttk.Label(frame, text='Изменение зеленого')
    label.pack()
    green_sb = ttk.Spinbox(frame, from_=-255, to=255, increment=1)
    green_sb.set(0)
    green_sb.pack()

    label = ttk.Label(frame, text='Изменение синего')
    label.pack()
    blue_sb = ttk.Spinbox(frame, from_=-255, to=255, increment=1)
    blue_sb.set(0)
    blue_sb.pack()

    label = ttk.Label(frame, text='Повторы')
    label.pack()
    repeat_sb = ttk.Spinbox(frame, from_=0, to=1000, increment=1)
    repeat_sb.set(1)
    repeat_sb.pack()

    def on_draw_click():
        for _ in range(int(repeat_sb.get())):
            draw_repeat(
                int(length_sb.get()),
                int(heading_sb.get()),
                int(red_sb.get()),
                int(green_sb.get()),
                int(blue_sb.get()),
            )

    draw_btn = ttk.Button(frame, text='Рисовать', command=on_draw_click)
    draw_btn.pack(pady=5)

    return frame

def frame_buttons():
    frame = ttk.Frame() 

    def on_undo_click():
        turtle.undo()
        turtle.undo()

        color = turtle.pencolor() # строка цвета или кортеж
        if isinstance(color, str):
            r, g, b = [c//256 for c in root.winfo_rgb(color)]
        else:
            r, g, b = color
        red.set(int(r))
        green.set(int(g))
        blue.set(int(b))

    undo_btn = ttk.Button(frame, text='Отменить', command=on_undo_click)
    undo_btn.pack(pady=2)

    def on_clear_click():
        turtle.reset()
        length.set(10)
        heading.set(0)
        red.set(0)
        green.set(0)
        blue.set(0)

    clear_btn = ttk.Button(frame, text='Очистить', command=on_clear_click)
    clear_btn.pack(pady=2)

    def on_save_click():
        canvas.update()
        eps = canvas.postscript(colormode='color')
        im = Image.open(BytesIO(bytes(eps, 'ascii')))
        im.save('image.png')

    save_btn = ttk.Button(frame, text='Сохранить', command=on_save_click)
    save_btn.pack(pady=2)

    return frame

root = tk.Tk()
root.title('Turtle Draw')
root.eval('tk::PlaceWindow . center')

length = tk.IntVar(value=10)
heading = tk.IntVar(value=0)
red = tk.IntVar(value=0)
green = tk.IntVar(value=0)
blue = tk.IntVar(value=0)

# создать виджеты верхнего уровня
mode_nb = ttk.Notebook()
mode_nb.add(tab_manual_mode(mode_nb), text='Ручной')
mode_nb.add(tab_repeat_mode(mode_nb), text='Повторы')
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
