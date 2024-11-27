import tkinter as tk

# Função calculadora:


def calculadora(num1=None, op='', num2=None):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1/num2
    else:
        print('Operação usada foi inválida!')


# Interface Gráfica:
root = tk.Tk()  # => iniciando a interface Tkinter
root.title('Calculadora TK')  # => Criando um titulo para a aplicação
# = > Criando a janela de Width = 400, height = 400 , x = 200, y = 200
root.geometry('400x400+200+200')

# Criando o grid

e0 = tk.Entry(root, bg='blue')

b7 = tk.Button(root, text='7', bg='gray')
b8 = tk.Button(root, text='8', bg='gray')
b9 = tk.Button(root, text='9', bg='gray')
bs = tk.Button(root, text='+', bg='gray')
b4 = tk.Button(root, text='4', bg='gray')
b5 = tk.Button(root, text='5', bg='gray')
b6 = tk.Button(root, text='6', bg='gray')
bsu = tk.Button(root, text='-', bg='gray')
b1 = tk.Button(root, text='1', bg='gray')
b2 = tk.Button(root, text='2', bg='gray')
b3 = tk.Button(root, text='3', bg='gray')
bmu = tk.Button(root, text='*', bg='gray')
bd = tk.Button(root, text='/', bg='gray')
b0 = tk.Button(root, text='0', bg='gray')
bi = tk.Button(root, text='=', bg='gray')

bi['command'] = lambda: calculcadora()

e0.grid(row=0)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
bs.grid(row=1, column=3)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
bsu.grid(row=2, column=3)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
bmu.grid(row=3, column=3)

bd.grid(row=4, column=0)
b0.grid(row=4, column=1)
bi.grid(row=4, column=2)


root.mainloop()  # => Iniciando o Programar


print('Desligando....')
