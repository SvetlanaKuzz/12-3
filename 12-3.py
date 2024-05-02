from tkinter import * #Импортируем все классы и функции из библиотеки
class IceCreamStand:

    def __init__(self, root):
        self.root = root
        self.root.title("Ice Cream Stand") #Устанавливаем заголовок главного окна
        self.root.geometry("800x600")  # Задаем размер окна
        self.root.minsize(600, 600)  # Задаем минимальный размер окна
        self.root.configure(bg='pink')

        self.text_frame = Frame(self.root, bg="white", padx=50, pady=30)
        self.text_frame.pack(padx=50, pady=50)

        self.name = Label(self.text_frame, text="Добро пожаловать!", bg="white", font=("Arial", 16), padx=0, pady=0)
        self.name.pack()

        self.flavours = Label(self.text_frame, text="Информация о сортах мороженого:", bg="white", font=("Arial", 16), padx=0, pady=0)
        self.flavours.pack()

        self.info_label = Label(self.text_frame,text="Ванильное\nШоколадное\nКлубничное",bg="white", font=("Arial", 16), padx=30, pady=50)
        self.info_label.pack()

        self.open_label = Label(self.text_frame, text="Часы работы:\n10am-10pm", bg="white",font=("Arial", 16), padx=20, pady=0)
        self.open_label.pack()
def main():
    root = Tk()
    app = IceCreamStand(root)
    root.mainloop()

if __name__ == "__main__":
    main()