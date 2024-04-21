from tkinter import Tk, HORIZONTAL
from tkinter.ttk import Label, Scale

from PIL import Image, ImageTk


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("form")
        self.geometry("400x300")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # show a label
        self.label = Label(self,
                           background="green",
                           text='This is a label',
                           font=('arial', 30, 'bold'))
        # self.label.place(x=50, y=10)
        self.label.grid(row=0, column=0, sticky="news")  # news mean expand: North, East, West, South

        self.slider = Scale(self,
                            from_=4,
                            to=1,
                            orient=HORIZONTAL,
                            command=self.receive)
        self.slider.set(4)
        self.slider.grid(row=1, column=0, sticky="news")

        img = Image.open("1.jpg")
        zoom = 4
        pixels_x, pixels_y = img.size
        img = img.resize((round(pixels_x / zoom), round(pixels_y / zoom)))

        photo = ImageTk.PhotoImage(img)
        self.label.configure(image=photo)
        self.label.image = photo

    def receive(self, event):
        print("ok", self.slider.get())
        img = Image.open("1.jpg")
        # img = img.resize((100, 200))
        value = self.slider.get()
        zoom = value
        pixels_x, pixels_y = img.size
        img = img.resize((round(pixels_x / zoom), round(pixels_y / zoom)))

        photo = ImageTk.PhotoImage(img)
        self.label.configure(image=photo)
        self.label.image = photo


if __name__ == "__main__":
    app = Window()
    app.mainloop()