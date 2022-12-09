from tkinter import Tk, Button, Entry, Label, Text, StringVar, OptionMenu, END, Listbox
import tkinter.filedialog as fd
from controller import searchContact, addContact, deleteContact, readDatabase, sizeDatabase, importData, exportData, sortedData


def main():

    windows = Tk()
    windows.title("Адресная книга")
    windows.geometry("643x312")
    windows.resizable(0, 0)

    """Обработчик события - поиска среди адресатов по введеному слову."""
    def eventSearch():
        faind = faind_user_entry.get()
        search = searchContact(faind)

        if(len(search) == 0): outputContacts()
        else:
            contacts.delete(0, END)
            for user in search:
                contacts.insert(END, f"{','.join(user).replace(',', ' ')}\n")
    
    """Обработчик события - добавление контакта в базу."""
    def eventAdd(contact=["","","","",""]):
        window_add_user = Tk()
        window_add_user.title("Добавить адресата")
        window_add_user.geometry("248x200")
        window_add_user.resizable(0, 0)
        
        list_parametrs = ["Фамилия: ", "Имя: ", "Отчество: ", "Раб. телефон: ", "Доп. телефон: "]
        list_label_entry = [Label(window_add_user, text=name) for name in list_parametrs]
        list_entry = [Entry(window_add_user, width=20) for i in range(len(list_label_entry))]

        for i in range(len(contact)):
            list_entry[i].insert(END, str(contact[i]))

        for i in range(len(list_label_entry)):
            list_label_entry[i].grid(row=i, column=0, padx=10, pady=5, sticky="w", ipadx=0)
            list_entry[i].grid(row=i, column=1, columnspan=3, padx=10, pady=5, ipadx=0)

        def exitWindow():
            parametrs = [parametr.get() for parametr in list_entry]
            window_add_user.destroy()
            addContact(parametrs)
            sortedData()
            outputContacts()

        buttonEnter = Button(window_add_user, text="Добавить", font=("Time New Roman", 10), width=25, height=1, command=exitWindow)
        buttonEnter.grid(row=5, column=0, columnspan=3, padx=18, pady=5)
    
    """Обработчик события - удаление контакта из базы."""
    def eventDelete():
        size_list = contacts.size()
        list_i = contacts.get(first=0, last=size_list)

        index_user = int(contacts.curselection()[0])

        contacts.delete(first=contacts.curselection())
        deleteContact(list_i[index_user])
    
    """Функция подтягивания актуальной базы. Вывод на экран списка контактов."""
    def outputContacts():
        row = sizeDatabase()
        contacts.delete(0, END)
        sortedData()
        
        for i in range(2, row + 1):
            contact = readDatabase(i)
            contacts.insert(END, f"{','.join(contact).replace(',', ' ')}\n")
    
    """Обработчик события - изменение данных контакта."""
    def eventChange():
        index_contact = contacts.curselection()
        contact = contacts.get(first=index_contact)
        new_contact = contact.split()

        if (new_contact): eventAdd(new_contact)
    
    """Обработчик события - импорт данных из файла."""
    def loadDatabase():
        file_types = (("Текстовый файл", "*.txt"), ("MS Excel 2007", "*.xlsx"), ("База даных SQL", "*db"))
        file_name = fd.askopenfilename(title="Выбрать файл", initialdir="/", filetypes=file_types)
        
        importData(file_name)
        outputContacts()
    
    """Обработчик события - экспорт данных в файл."""
    def unloadData():
        type_file = format_data.get()
        exportData(type_file)
        outputContacts()
    
    # Окно вывода адресатов.
    contacts = Listbox(windows, width=74, height=14)
    contacts.grid(row=2, column=0, columnspan=3, rowspan=20, padx=10, pady=0)

    # Окно ввода для поиска пользователя.
    faind_user_entry = Entry(windows, width=55)
    faind_user_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=5, ipadx=0)

    # Заголовок к окну с списком всех адресатов/ найденных адресатов.
    label_list_2 = Label(windows,text="Список адресатов: ")
    label_list_2.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=0, ipadx=0)

    # Создаем кнопку выполняющую поиск по заданным текстовым параметрам.
    faind_button = Button(windows, text="Найти ->", font=("Time New Roman", 10), width=10, height=1, command=eventSearch)
    faind_button.grid(row=0, column=0, padx=10, pady=0)

    # Меню управления программой.
    buttom_name_1 = ["Добавить пользователя", "Удалить пользователя", "Изменить пользователя", "Загрузить данные", "Выгрузить данные"]
    buttom_list_1 = [Button(windows, text=name, font=("Time New Roman", 10), width=20, height=1) for name in buttom_name_1]

    for i in range(len(buttom_list_1)):
        if (i == 0 or i == 1): buttom_list_1[i].grid(row=i, column=4, padx=0, pady=5)
        else: buttom_list_1[i].grid(row=i, column=4, padx=0, pady=3)

    buttom_list_1[0].config(command=eventAdd)
    buttom_list_1[1].config(command=eventDelete)
    buttom_list_1[2].config(command=eventChange)
    buttom_list_1[3].config(command=loadDatabase)
    buttom_list_1[4].config(command=unloadData)

    # Список возможных форматов экспорта/импорта данных.
    format_exit_data = ["txt", "xlsx", "db"] 

    # Выпадающее меню с форматами выходных файлов.
    format_data = StringVar(windows)
    format_data.set(format_exit_data[0])
    opt = OptionMenu(windows, format_data, *format_exit_data)
    opt.config(width=14, height=1, font=("Time New Roman", 12))
    opt.grid(row=5, column=4, padx=0, pady=0)
    
    # exportData(format_data.get())

    outputContacts()

    windows.mainloop()
