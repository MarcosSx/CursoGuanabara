from tkinter import *


def adicionar_valores(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)


def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))


def limpa():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')


# CORES
cor_azul = '#081326'
cor_branca = '#ffffff'
cor_preta = '#000000'
cor_cinza = '#b8b8b8'
cor_laranja = '#ff7b00'

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(bg=cor_preta)

frame_tela = Frame(janela, width=235, height=50, bg=cor_azul)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

todos_valores = ''
valor_texto = StringVar()

lbl_tela = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor=E, justify=RIGHT,
                 font=('Ivy 18'), bg=cor_azul, fg=cor_branca)
lbl_tela.place(x=0, y=0)

btn_limpar = Button(frame_corpo, text='C', width=11, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED,
                    overrelief=RIDGE, command=limpa)
btn_limpar.place(x=0, y=0)

btn_resto = Button(frame_corpo, text='Rest', width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED,
                   overrelief=RIDGE, command=lambda: adicionar_valores('%'))
btn_resto.place(x=118, y=0)

btn_divisao = Button(frame_corpo, text='/', width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'),
                     relief=RAISED, overrelief=RIDGE, command=lambda: adicionar_valores('/'))
btn_divisao.place(x=177, y=0)

btn_7 = Button(frame_corpo, text='7', width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED,
               overrelief=RIDGE, command=lambda: adicionar_valores('7'))
btn_7.place(x=0, y=52)

btn_8 = Button(frame_corpo, text='8', width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED,
               overrelief=RIDGE, command=lambda: adicionar_valores('8'))
btn_8.place(x=59, y=52)

btn_9 = Button(frame_corpo, text='9', width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED,
               overrelief=RIDGE, command=lambda: adicionar_valores('9'))
btn_9.place(x=118, y=52)

btn_multi = Button(frame_corpo, text='*', width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'),
                   relief=RAISED, overrelief=RIDGE, command=lambda: adicionar_valores('*'))
btn_multi.place(x=177, y=52)

btn_4 = Button(frame_corpo, text='4', width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED,
               overrelief=RIDGE, command=lambda: adicionar_valores('4'))
btn_4.place(x=0, y=104)

btn_5 = Button(frame_corpo, text='5', width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED,
               overrelief=RIDGE, command=lambda: adicionar_valores('5'))
btn_5.place(x=59, y=104)

btn_6 = Button(frame_corpo, text='6', width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED,
               overrelief=RIDGE, command=lambda: adicionar_valores('6'))
btn_6.place(x=118, y=104)

btn_subtracao = Button(frame_corpo, text='-', width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'),
                       relief=RAISED, overrelief=RIDGE, command=lambda: adicionar_valores('-'))
btn_subtracao.place(x=177, y=104)

btn_1 = Button(frame_corpo, text='1', width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED,
               overrelief=RIDGE, command=lambda: adicionar_valores('1'))
btn_1.place(x=0, y=156)

btn_2 = Button(frame_corpo, text='2', width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED,
               overrelief=RIDGE, command=lambda: adicionar_valores('2'))
btn_2.place(x=59, y=156)

btn_3 = Button(frame_corpo, text='3', width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED,
               overrelief=RIDGE, command=lambda: adicionar_valores('3'))
btn_3.place(x=118, y=156)

btn_soma = Button(frame_corpo, text='+', width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'),
                  relief=RAISED, overrelief=RIDGE, command=lambda: adicionar_valores('+'))
btn_soma.place(x=177, y=156)

btn_zero = Button(frame_corpo, text='0', width=11, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED,
                  overrelief=RIDGE, command=lambda: adicionar_valores('0'))
btn_zero.place(x=0, y=208)

btn_ponto = Button(frame_corpo, text='.', width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED,
                   overrelief=RIDGE, command=lambda: adicionar_valores('.'))
btn_ponto.place(x=118, y=208)

btn_igual = Button(frame_corpo, text='=', width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'),
                   relief=RAISED, overrelief=RIDGE, command=calcular)
btn_igual.place(x=177, y=208)

janela.mainloop()
