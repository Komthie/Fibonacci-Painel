import tkinter as tk
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image







def formula():
    window = tk.Toplevel(painel)
    window.geometry('1060x740')
    window.configure(background='black', borderwidth=5)
    window.title('Formula of Fibonacci')
    window.resizable()
    formula_f = Label(window, text="""
The Fibonacci sequence is a sequence of integers, usually starting with 0 and 1, in which each subsequent term corresponds to the sum of the two preceding ones.\n 
The sequence is named after the Italian mathematician Leonardo of Pisa,\n 
also known as Fibonacci, who introduced it to the West in the 13th century,\n
but it was already known in India.\n
The general formula for calculating a term in the Fibonacci sequence is:\n
\n
$$F(n) = F(n-1) + F(n-2)$$\n
\n
where:\n
- $F(n)$ is the nth term of the sequence\n
- $F(n-1)$ is the previous term\n
- $F(n-2)$ is the term before the previous one\n
\n
The first 10 terms of the Fibonacci sequence are:\n
0, 1, 1, 2, 3, 5, 8, 13, 21, 34\n
Each number in the sequence is the sum of the two preceding ones. For example, 2 (the fourth term) is the sum of 1 (the third term) and 1 (the second term).\n 
Similarly, 21 (the ninth term) is the sum of 13 (the eighth term) and 8 (the seventh term), and so on.\n
The Fibonacci sequence has many interesting applications in mathematics,\n
computer science, and even in art and nature.\n
    """)
    formula_f.configure(background='black', foreground='white', font=fonte_medieval)
    formula_f.pack()
    minubar = Menu(window)
    sei = Menu(minubar, tearoff=0)
    sei.add_command(label="Exit", command=sair)
    minubar.add_cascade(label='Settings', menu=sei)
    window.config(menu=minubar)
def nova_janela():
    janela = tk.Toplevel(painel)
    janela.geometry('600x240')
    janela.configure(background='#000000')
    janela.title = 'History of Fibonacci'
    historia = Label(janela, text="""
Fibonacci, also known as Leonardo Bonacci, was an Italian mathematician 
born in Pisa in the 12th century. He is best known for introducing t
he Fibonacci sequence to the Western world in his book "Liber Abaci."
The sequence starts with 0 and 1, 
and each subsequent number is the sum of the two preceding numbers(0, 1, 1, 2, 3, 5, 8,
and so on).Fibonacci's work revolutionized mathematics and had a profound impact on 
fields like number theory and computer science.
The sequence named after him appears in various natural phenomena, 
such as the arrangement of leaves on a stem and the spiral of a shell.
Fibonacci's contributions to mathematics extended beyond the sequence.
He also introduced the Hindu-Arabic numeral system to Europe,
which replaced Roman numerals and revolutionized arithmetic calculations.
Overall, Fibonacci's legacy lies in his pioneering work that significantly 
influenced the development of mathematics and its applications in various disciplines.
    """)
    historia.configure(bg='#000000', foreground='white')
    historia.pack()

    minubar = Menu(janela)
    sei = Menu(minubar, tearoff=0)
    sei.add_command(label="Exit", command=sair)
    minubar.add_cascade(label='Settings', menu=sei)
    janela.config(menu=minubar)

def how_to():
    win = tk.Toplevel(painel)
    win.geometry('560x60')
    win.configure(background='black', borderwidth=5)
    win.title('How To Use')
    win.resizable(False, False)
    formula_f = Label(win, text='enter the number you want to know from the Fibonacci sequence\ninto the panel input')
    formula_f.pack()
    formula_f.configure(background='black', foreground='white', font=fonte_medieval2)

def sair():
    painel.destroy()

def fibonacci(n):
    fibo_sequence = [0, 1]

    for i in range(2, n):
        next_term = fibo_sequence[-1] + fibo_sequence[-2]
        fibo_sequence.append(next_term)

    return fibo_sequence

def calcular_fibonacci():
    try:
        n_termos = int(entrysequence.get())
        sequencia = fibonacci(n_termos)
        resultado.config(text=f"Sequence of Fibonacci: {sequencia}", borderwidth=6, background='black', foreground='white', font=fonte_medieval)
        resultado.place(x=70, y=10)
    except ValueError:
        resultado.config(text="Insira um número válido..")



# Crie a janela principal
painel = tk.Tk()
painel.geometry('550x350')
painel.title('Fibonacci Painel')
painel.configure(background='#000000')
painel.resizable()
painel.iconbitmap('C:/Users/PEDRO MORAES/Downloads/brand_hello_kitty_icon_158867.ico')


menubar = Menu(painel)

seila = Menu(menubar, tearoff=0)
seila.add_command(label="New")
seila.add_command(label="Exit", command=sair)
menubar.add_cascade(label='Settings', menu=seila)

fibo = Menu(menubar, tearoff=0)
fibo.add_command(label='Formula', command=formula)
fibo.add_command(label='History', command=nova_janela)
fibo.add_command(label='Photos')
menubar.add_cascade(label='Fibonacci', menu=fibo)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="How to use", command=how_to)
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)
painel.config(menu=menubar)

#
img3 = ImageTk.PhotoImage(Image.open('C:/Users/PEDRO MORAES/Downloads/fi.jpg'))
panel = tk.Label(painel, image = img3)
panel.place(x=1,
            y=2
            )


#Crie coded by komthe
coded = tk.Label(painel, text='coded by Komthe', background='black', foreground='#DF7CFA', cursor='hand2')
coded.place(x=435, y=330)

fonte_medieval = font.Font(family="Courier", size=12)
fonte_medieval2 = font.Font(family="Courier", size=8)


sequence = Label(painel, text='SEQUENCE OF FIBONACCI', background='#000000', font=fonte_medieval, foreground='white')
sequence.place(x=180, y=150)

entrysequence = Entry(painel, background='#000000', borderwidth=3, foreground='white', font=fonte_medieval)
entrysequence.place(x=180, y=180)


resultado = tk.Label(painel, text="", font=font.Font(family="Courier", size=10))
resultado.pack()

botao_fibonacci = Button(painel, text='Fibonacci', foreground='black', cursor='hand2', background='white', borderwidth=2, font=fonte_medieval, command=calcular_fibonacci)
botao_fibonacci.place(x=230, y=210)


painel.mainloop()
