import pyperclip as pc
import tkinter as tk
from tkinter import ttk
from gerador_conta import *

root = tk.Tk()
root.title('Gerador de conta bancaria')
root.geometry('300x500+750+250')
root.resizable(False, False)
root.iconbitmap(default='images\\nmea.ico')

lista_bancos = ['Banco do Brasil', 'Caixa', 'Santander', 'Itau', 'HSBC', 'Citibank', 'Bradesco', 'Real', 'Indiferente']
img_fundo = tk.PhotoImage(file='images\\fundo.png')
img_botao = tk.PhotoImage(file='images\\btn_gerar.png')
img_botao_copy = tk.PhotoImage(file='images\\btn_copy.png')
img_botao_copied = tk.PhotoImage(file='images\\btn_copied.png')
img_botao_sair = tk.PhotoImage(file='images\\btn_sair.png')
agencia_var = tk.StringVar()
conta_var = tk.StringVar()
banco_var = tk.StringVar()


def gerar():
    bank = btn_select_banks.get()
    bank_to_show = select_bank(bank)
    agencia = str(bank_to_show[1]).split()[1]
    conta = str(bank_to_show[1]).split()[3]
    label_conta.config(text=conta)
    label_agencia.config(text=agencia)
    label_banco.config(text=str(bank_to_show[0]))
    agencia_var.set(agencia)
    conta_var.set(conta)
    banco_var.set(bank_to_show[0])
    button_copiar_agencia.config(image=img_botao_copy)
    button_copiar_banco.config(image=img_botao_copy)
    button_copiar_conta.config(image=img_botao_copy)


def copiar_para_clipboard(value):
    value = value.get()
    if len(value) > 6 and value not in lista_bancos:
        button_copiar_conta.config(image=img_botao_copied)
        button_copiar_agencia.config(image=img_botao_copy)
        button_copiar_banco.config(image=img_botao_copy)
    elif value in lista_bancos:
        button_copiar_agencia.config(image=img_botao_copy)
        button_copiar_banco.config(image=img_botao_copied)
        button_copiar_conta.config(image=img_botao_copy)
    else:
        button_copiar_agencia.config(image=img_botao_copied)
        button_copiar_banco.config(image=img_botao_copy)
        button_copiar_conta.config(image=img_botao_copy)
    pc.copy(value)


label_fundo = tk.Label(root, image=img_fundo)
label_fundo.pack()

btn_select_banks = tk.ttk.Combobox(root, values=lista_bancos)
btn_select_banks.set('Indiferente')
btn_select_banks.place(x=21, y=133, width=263, height=35)

button_gerar = tk.Button(root, image=img_botao)
button_gerar.place(x=79, y=180, width=142, height=40)
button_gerar.config(command=lambda: gerar())

label_conta = tk.Label(root, text='')
label_conta.place(x=21, y=264, width=213, height=33)

button_copiar_conta = tk.Button(root, image=img_botao_copy)
button_copiar_conta.place(x=240, y=264, width=50, height=33)
button_copiar_conta.config(command=lambda: copiar_para_clipboard(conta_var))

label_agencia = tk.Label(root, text='')
label_agencia.place(x=21, y=336, width=213, height=33)

button_copiar_agencia = tk.Button(root, image=img_botao_copy)
button_copiar_agencia.place(x=240, y=336, width=50, height=33)
button_copiar_agencia.config(command=lambda: copiar_para_clipboard(agencia_var))

label_banco = tk.Label(root, text='')
label_banco.place(x=21, y=399, width=213, height=33)

button_copiar_banco = tk.Button(root, image=img_botao_copy)
button_copiar_banco.place(x=240, y=399, width=50, height=33)
button_copiar_banco.config(command=lambda: copiar_para_clipboard(banco_var))

button_sair = tk.Button(root, image=img_botao_sair, command=root.destroy)
button_sair.place(x=79, y=448, width=145, height=40)

root.mainloop()
