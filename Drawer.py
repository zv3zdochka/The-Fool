import tkinter as tk

def draw_rectangle(canvas, x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill="", outline="yellow", width=5)

def clear_canvas(canvas):
    canvas.delete("all")

def main_loop(canvas, rectangle_coordinates):
    # Очистка холста перед каждым циклом
    clear_canvas(canvas)

    for coords in rectangle_coordinates:
        # Рисование четырехугольника по координатам
        draw_rectangle(canvas, *coords)

    # Вызов функции main_loop повторно
    root.after(1000, main_loop, canvas, rectangle_coordinates)

# Пример координат четырехугольников
rectangle_coordinates = [
    (50, 25, 150, 75),
    (100, 50, 200, 100),
    (150, 75, 250, 125)
]

root = tk.Tk()

root.wait_visibility(root)
root.wm_attributes("-fullscreen", 1)
root.wm_attributes("-transparentcolor", root['bg'])

frame = tk.Frame(root)
frame.pack()

canvas = tk.Canvas(frame, width=root.winfo_width(), height=root.winfo_height())
canvas.pack()

# Запуск основного цикла программы
main_loop(canvas, rectangle_coordinates)

root.mainloop()
