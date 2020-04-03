from tkinter import *
import webbrowser, os


def openMod():
    webbrowser.open('https://www.gtavicecity.ru')


def openVK():
    webbrowser.open('https://vk.com/dozer_service')


def openGTASA():
    os.startfile('gta_sa.exe')
    quit()


def openGTASAMP():
    os.startfile('samp.exe')
    quit()


def openDELETE():
    root = Tk()
    root.title('Дополнительная информация')
    root.geometry('350x500')
    root.resizable(width=False, height=False)
    root.iconbitmap('iconlc+.ico')

    lab = Label(root, text='''Доп.информация:

Язык программирования
на котором работает лаунчер:
~~~ Python 3.7.4 32bit ~~~

Модули Python,
используемые в
работе лаунчера:
~~~ tkinter, os, webbrowser ~~~

Разработчик сборки и лаунчера:
~~~ doZer Service ~~~

Программист(ы):
~~~ Матвей Воронцов ~~~''')
    lab.config(font=('Times', 18))
    lab.pack()

    root.mainloop()


def openINST():
    os.startfile('инструкция.txt')


window = Tk()
window.title('GTA SA LaUncher+')
window.resizable(width=False, height=False)
window.geometry('650x322')
window.iconbitmap('iconlc+.ico')

photo = PhotoImage(file="fon.png")
one = Label(window, image=photo)
one.image = photo  # just keeping a reference
one.grid()

dev = Button(window, text='Страница разработчика')
dev.config(width=21, height=1, bg='white smoke', fg='black', command=openVK)
dev.place(x=2, y=296)

playClassic = Button(window, text='''Играть в классическую
GTA (GTA SA)''')
playClassic.config(width=21, height=2, bg='white smoke', fg='black', command=openGTASA)
playClassic.place(x=485, y=66)

playMultiplayer = Button(window, text='''Играть в мультиплеерную
GTA (GTA SAMP 0.3.7)''')
playMultiplayer.config(width=21, height=2, bg='white smoke', fg='black', command=openGTASAMP)
playMultiplayer.place(x=485, y=107)

download = Button(window, text='''Скачать дополнительные
моды (модификации)''')
download.config(width=21, height=2, bg='white smoke', fg='black', command=openMod)
download.place(x=485, y=148)

delete = Button(window, text='''Дополнительная
информация''')
delete.config(width=21, height=2, bg='white smoke', fg='black', command=openDELETE)
delete.place(x=485, y=189)

inst = Button(window, text='Инструкция')
inst.config(width=21, height=2, bg='white smoke', fg='black', command=openINST)
inst.place(x=485, y=230)

text3 = Label(window, text='Created by: doZer Service | Matvey Vorontsov', fg='black')
text3.config(font=('Arial', 8))
text3.place(x=419, y=303)

window.mainloop()
