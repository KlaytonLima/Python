from tkinter import *

janela = Tk()

janela.geometry('300x300')
janela.title("")
janela.resizable(False, False)
"""LABEL"""
lb_login = Label(janela, text="LOGIN", font='Ivy 20 bold', bg='blue', width=20)
lb_login.grid(row=0, column=0)
lb_usuario = Label(janela, text="Usuário", font='Ivy 15 bold')
lb_usuario.grid(row=1, column=0)
lb_senha = Label(janela, text="Senha", font='Ivy 15 bold')
lb_senha.grid(row=4, column=0)
"""ENTRY"""
entry_usuario = Entry(janela, font='Ivy 15 bold')
entry_usuario.grid(row=2, column=0)
entry_senha = Entry(janela, font='Ivy 15 bold')
entry_senha.grid(row=5, column=0)
"""ROW"""
lb_row_1 = Label(janela, text="")
lb_row_1.grid(row=3, column=0)
lb_row_2 = Label(janela, text="")
lb_row_2.grid(row=6, column=0)
"""BUTTON"""
bt_acessar = Button(janela, text='Acessar', font='Ivy 15 bold')
bt_acessar.grid(row=7, column=0)


janela.mainloop()
