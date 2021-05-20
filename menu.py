from tkinter import *
from tkinter import font
from configuration import configs

def menu():
    menu = Tk()
    menu.geometry('500x200')
    menu.title('Menu')

    myFont = font.Font(family = 'Helvetica', size = 16)

    def window():
        menu.destroy()
        c = configs()
        
        
    new_champ = Button(menu, text='Novo Campeonato',command = window,  fg='green', width=30, font = myFont)
    new_champ.pack(pady = 10)

    last_champs = Button(menu,text='Ultimos Campeonatos', fg='gray',width=30, font = myFont)
    last_champs.pack()
    menu.mainloop()

menu()