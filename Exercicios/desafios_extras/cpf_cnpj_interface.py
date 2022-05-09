import tkinter as tk
import cpf_cnpj_utils
import pyperclip as pc

# CORES
cor_azul = '#081326'
cor_branca = '#ffffff'
cor_preta = '#000000'
cor_cinza = '#b8b8b8'
cor_laranja = '#ff7b00'

root = tk.Tk()
root.title('Gerador/Validador de CPF e CNPJ')
root.iconbitmap(default='icones\\ico.ico')
root.config(background=cor_branca, padx=5, pady=5)


def validate_cpf_cnpj(stringvar, button):
    cpf_cnpj = stringvar.get()
    if cpf_cnpj_utils.validator_cpf_cnpj(cpf_cnpj):
        response_label.config(text='Documento Valido!!!')
    else:
        response_label.config(text='Documento Invalido!!!')


def generate_cpf_cnpj(stringvar, button):
    if sel() == 3:
        response_label.config(text='Selecione um documento')
    else:
        cpf_cnpj = cpf_cnpj_utils.cpf_cnpj_generator(sel(), True)
        stringvar.set(cpf_cnpj)
        pc.copy(cpf_cnpj)
        response_label.config(text=f'{sel()} copiado para clipboard')


def sel():
    selection = var.get()
    if selection == 1:
        response_label.config(text='Voce selecionou CNPJ')
        return 'CNPJ'
    elif selection == 2:
        response_label.config(text='Voce selecionou CPF')
        return 'CPF'
    else:
        selection = 3
        return selection


main_frame = tk.Frame(root, width=270, height=25, bg=cor_cinza)
main_frame.pack()

main_title = tk.Label(main_frame, text='Gerador/Validador de CPF e CNPJ', bg=cor_cinza, font=('Helvetica', 12, 'bold'))
main_title.place(x=2, y=0)

options_frame = tk.Frame(root, width=270, height=50, bg=cor_azul)
options_frame.pack()

options_label = tk.Label(options_frame, text='Selecione um tipo de documento:', bg=cor_azul, fg=cor_laranja)
options_label.place(x=10, y=5)
var = tk.IntVar()

option_cpf = tk.Radiobutton(options_frame, text='CPF', value=2, variable=var, command=sel, bg=cor_azul, fg=cor_laranja)
option_cpf.place(x=10, y=25)
option_cnpj = tk.Radiobutton(options_frame, text='CNPJ', value=1, variable=var, command=sel, bg=cor_azul,
                             fg=cor_laranja)
option_cnpj.place(x=75, y=25)

generate_frame = tk.Frame(root, width=270, height=25, bg=cor_azul)
generate_frame.pack()

generate_label = tk.Label(generate_frame, text='Gerar: ', bg=cor_azul, fg=cor_laranja)
generate_label.place(x=10, y=0)

generate_string_var = tk.StringVar()
generate_entry = tk.Label(generate_frame, textvariable=generate_string_var, width=21, bg=cor_cinza)
generate_entry.place(x=55, y=0)

generate_button = tk.Button(generate_frame, text=' Gerar  ')
generate_button.place(x=217, y=0)
generate_button.config(command=lambda: generate_cpf_cnpj(generate_string_var, generate_button))

validate_frame = tk.Frame(root, width=270, height=25, bg=cor_azul)
validate_frame.pack()

validate_label = tk.Label(validate_frame, text='Validar:', bg=cor_azul, fg=cor_laranja)
validate_label.place(x=10, y=0)

validate_string_var = tk.StringVar()
validate_entry = tk.Entry(validate_frame, textvariable=validate_string_var, width=25, justify=tk.CENTER)
validate_entry.place(x=55, y=0)

validate_button = tk.Button(validate_frame, text='Validar')
validate_button.place(x=217, y=0)
validate_button.config(command=lambda: validate_cpf_cnpj(validate_string_var, validate_button))

response_frame = tk.Frame(root, width=270, height=50, bg=cor_azul, pady=5)
response_frame.pack()

response_label = tk.Label(response_frame,
                          text='Bem vindo ao Gerador/Validador de CPF e CNPJ\nGere ou valide um documento!',
                          bg=cor_azul,
                          fg=cor_laranja)
response_label.place(x=10, y=0)

root.mainloop()
