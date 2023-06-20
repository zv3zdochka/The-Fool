import tkinter as tk

class RectangleAnimator:
    def __init__(self):
        self.rectangle_coordinates = []
        self.root = tk.Tk()
        self.setup_window()
        self.create_canvas()

        # Start the main loop of the program
        self.main_loop()

        self.root.mainloop()

    def setup_window(self):
        self.root.wait_visibility(self.root)
        self.root.wm_attributes("-fullscreen", 1)
        self.root.wm_attributes("-transparentcolor", self.root['bg'])

        self.frame = tk.Frame(self.root)
        self.frame.pack()

    def create_canvas(self):
        self.canvas = tk.Canvas(self.frame, width=self.root.winfo_width(), height=self.root.winfo_height())
        self.canvas.pack()

    def draw_rectangle(self, x1, y1, x2, y2):
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="", outline="yellow", width=5)

    def clear_canvas(self):
        self.canvas.delete("all")

    def update_coordinates(self, new_coordinates):
        self.rectangle_coordinates = new_coordinates

    def main_loop(self):
        # Clear the canvas before each loop
        self.clear_canvas()

        for coords in self.rectangle_coordinates:
            # Draw the rectangle using the coordinates
            self.draw_rectangle(*coords)

        # Call the main_loop function again
        self.root.after(1000, self.main_loop)

    def start(self):
        RectangleAnimator()
