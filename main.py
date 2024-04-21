import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kéo Dãn Ô Lưới")

        # Tạo các widget
        label1 = tk.Label(self.root, text="Widget 1", bg="red")
        label2 = tk.Label(self.root, text="Widget 2", bg="green")
        label3 = tk.Label(self.root, text="Widget 3", bg="blue")

        # Đặt widget vào ô lưới
        label1.grid(row=0, column=0, sticky="nsew")
        label2.grid(row=1, column=0, sticky="nsew")
        label3.grid(row=2, column=0, sticky="nsew")

        # Cài đặt thuộc tính weight cho hàng và cột
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Hiển thị cửa sổ
        self.root.mainloop()

app = App()
