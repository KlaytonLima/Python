from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.geometry('450x300')
janela.resizable(False, False)
janela.configure(background='#4169E1')
janela.title("")

"""FRAMES"""
frame_1 = Frame(janela, width=430, height=180, bg='#4682B4')
frame_1.place(x=10, y=44)
"""LABELS"""
lb_title = Label(janela, text="Calculadora de IMC", font=('Ivy 16 bold'), width=20, bg='#4682B4', fg='white')
lb_title.place(x=0, y=0, relwidth=1)
lb_peso = Label(frame_1, text="Peso", font='Arial 15 bold', bg='#4682B4')
lb_peso.place(x=5, y=5)
lb_altura = Label(frame_1, text="Altura", font='Arial 15 bold', bg='#4682B4')
lb_altura.place(x=5, y=60)
"""ENTRYS"""
entry_peso = Entry(frame_1, width=25, highlightthickness=1, font='Arial 15 bold', justify=CENTER)
entry_peso.place(x=90, y=8)
entry_altura = Entry(frame_1, width=25, highlightthickness=1, font='Arial 15 bold', justify=CENTER)
entry_altura.place(x=90, y=60)
def f_calcular():
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())
    imc = peso/(altura*altura)
    resultado = "{:.2f}".format(imc)

    if imc <= 16.9:
        lb_imc = Label(frame_1, text=(resultado), font='Arial 15 bold', bg='#4682B4', fg='red', width=40, justify=CENTER)
        lb_imc.place(x=5, y=98)
        lb_resultado = Label(frame_1, text="Muito abaixo do peso", font='Arial 15 bold', bg='#4682B4', fg='red', width=40, justify=CENTER)
        lb_resultado.place(x=5, y=125)
    elif imc >= 17 and imc <= 18.4:
        lb_imc = Label(frame_1, text=(resultado), font='Arial 15 bold', bg='#4682B4', fg='yellow', width=40, justify=CENTER)
        lb_imc.place(x=5, y=98)
        lb_resultado = Label(frame_1, text="Abaixo do peso", font='Arial 15 bold', bg='#4682B4', fg='yellow', width=40, justify=CENTER)
        lb_resultado.place(x=5, y=125)
    elif imc >= 18.5 and imc <= 24.9:
        lb_imc = Label(frame_1, text=(resultado), font='Arial 15 bold', bg='#4682B4', fg='green', width=40, justify=CENTER)
        lb_imc.place(x=5, y=98)
        lb_resultado = Label(frame_1, text=" Em forma ", font='Arial 15 bold', bg='#4682B4', fg='green', width=40, justify=CENTER)
        lb_resultado.place(x=5, y=125)
    elif imc >= 25 and imc <= 29.9:
        lb_imc = Label(frame_1, text=(resultado), font='Arial 15 bold', bg='#4682B4', fg='yellow', width=40, justify=CENTER)
        lb_imc.place(x=5, y=98)
        lb_resultado = Label(frame_1, text="Acima do peso", font='Arial 15 bold', bg='#4682B4', fg='yellow', width=40, justify=CENTER)
        lb_resultado.place(x=5, y=125)
    elif imc >= 30 and imc <= 34.9:
        lb_imc = Label(frame_1, text=(resultado), font='Arial 15 bold', bg='#4682B4', fg='lightorange', width=40, justify=CENTER)
        lb_imc.place(x=5, y=98)
        lb_resultado = Label(frame_1, text="Obesidade grau 1", font='Arial 15 bold', bg='#4682B4', fg='lightorange', width=40, justify=CENTER)
        lb_resultado.place(x=5, y=125)
    elif imc >= 35 and imc <= 40:
        lb_imc = Label(frame_1, text=(resultado), font='Arial 15 bold', bg='#4682B4', fg='orange', width=40, justify=CENTER)
        lb_imc.place(x=5, y=98)
        lb_resultado = Label(frame_1, text="Obesidade grau 2", font='Arial 15 bold', bg='#4682B4', fg='orange', width=40, justify=CENTER)
        lb_resultado.place(x=5, y=125)
    elif imc >= 40:
        lb_imc = Label(frame_1, text=(resultado), font='Arial 15 bold', bg='#4682B4', fg='red', width=40, justify=CENTER)
        lb_imc.place(x=5, y=98)
        lb_resultado = Label(frame_1, text="Obesidade grau 3", font='Arial 15 bold', bg='#4682B4', fg='red', width=40, justify=CENTER)
        lb_resultado.place(x=5, y=135)
"""BUTTONS"""
bt_calcular = Button(janela, text="Calcular", font='Arial 15 bold', bg='#4682B4', fg='black', width=25, highlightthickness=1,
                     highlightbackground='#4682B4', command=lambda: [f_calcular()])
bt_calcular.place(x=69, y=244)


janela.mainloop()
