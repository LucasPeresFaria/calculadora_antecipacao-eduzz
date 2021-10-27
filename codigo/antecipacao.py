import sys
# -*- coding: utf-8 -*-

from tkinter import *
from func import bissexto, quant_dias, valor, porcentagem_taxa
import ctypes

taxa_eduzz = 2.99

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["padx"] = 20
        self.container1["pady"] = 5        
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["pady"] = 20
        self.container6["pady"] = 10
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["pady"] = 2
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["pady"] = 2
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 2
        self.container9.pack()

        self.container10 = Frame(master)
        self.container10["pady"] = 2
        self.container10.pack()

        self.container11 = Frame(master)
        self.container11["pady"] = 2
        self.container11.pack()

        self.container12 = Frame(master)
        self.container12["pady"] = 2
        self.container12.pack()
#-------------------------------------------------------------------------

        self.titulo = Label(self.container1, text="Calculo de antecipacao")
        self.titulo["font"] = ("Calibri", "12", "bold")
        self.titulo["pady"] = 20
        self.titulo.pack()

        self.lblidfatura = Label(self.container2, text="Valor de ganho", font=self.fonte, width=30)
        self.lblidfatura.pack(side=LEFT)

        self.txtfatura = Entry(self.container2)
        self.txtfatura["width"] = 25
        self.txtfatura["font"] = self.fonte
        self.txtfatura.pack(side=LEFT)

        self.lblrecebimento = Label(self.container3, text="Data de recebimento DD/MM/AAAA", font=self.fonte, width=30)
        self.lblrecebimento.pack(side=LEFT)

        self.txtrecebimento = Entry(self.container3)
        self.txtrecebimento["width"] = 25
        self.txtrecebimento["font"] = self.fonte
        self.txtrecebimento.pack(side=LEFT)

        self.lblantecipacao = Label(self.container4, text="Data de antecipacao DD/MM/AAAA", font=self.fonte, width=30)
        self.lblantecipacao.pack(side=LEFT)

        self.txtantecipacao = Entry(self.container4)
        self.txtantecipacao["width"] = 25
        self.txtantecipacao["font"] = self.fonte
        self.txtantecipacao.pack(side=LEFT)

        self.checkblackfriday = Checkbutton(self.container5, text = 'Black Friday', var=blackfriday, onvalue=1, offvalue=0)
        self.checkblackfriday.pack(side=LEFT)

        self.bntCalcular = Button(self.container6, text="Calcular", font=self.fonte, width=12)
        self.bntCalcular["pady"] = 5
        self.bntCalcular.pack (side=LEFT)
        self.bntCalcular.bind("<Button-1>", self.calcular)

        self.bntLimpar = Button(self.container6, text="Limpar", font=self.fonte, width=12)
        self.bntLimpar["pady"] = 5
        self.bntLimpar.pack (side=LEFT)
        self.bntLimpar.bind("<Button-1>", self.limpar)

        self.msg1 = Label(self.container7, text="")
        self.msg1["font"] = ("Verdana", "9")
        self.msg1.pack()

        self.msg2 = Label(self.container8, text="")
        self.msg2["font"] = ("Verdana", "9")
        self.msg2.pack(side=LEFT)
        self.msg2.pack()

        self.msg3 = Label(self.container9, text="")
        self.msg3["font"] = ("Verdana", "9")
        self.msg3.pack()

        self.msg4 = Label(self.container10, text="")
        self.msg4["font"] = ("Verdana", "9")
        self.msg4.pack()

        self.msg5 = Label(self.container10, text="")
        self.msg5["font"] = ("Verdana", "9")
        self.msg5.pack()
#-----------------------------------------------------------------------

    def calcular(self, event):

        if blackfriday.get() == 0:
            taxa_eduzz = 2.99
        else:
            taxa_eduzz = 0.99

        fatura = self.txtfatura.get()
        recebimento = self.txtrecebimento.get()
        antecipado = self.txtantecipacao.get()

        #CHAMANDO AS FUNÇOES EM FUNC.PY
        ano = bissexto(recebimento, antecipado)
        dias = quant_dias(ano, recebimento, antecipado)
        cobranca = valor(taxa_eduzz, dias, fatura)
        porcentagem = porcentagem_taxa(dias, taxa_eduzz)

        self.msg1["text"] = "Quantidade de dias antecipados: " + str(dias) + " dias"
        self.msg2["text"] = "Taxa: " + str(round(porcentagem,2)) + "%"
        self.msg3["text"] = "O valor cobrado R$" + str(round(cobranca, 2)) + " reais"

        formula_dia = 30 - dias
        self.msg4["text"] = "-------------------------------------------------------"
        self.msg5["text"] = "Formula: " + str(taxa_eduzz) + " + " + str(formula_dia) + " * 0.1% = " + str(round(porcentagem,2)) + "%"
    
    def limpar(self, event):
        self.txtfatura.delete(0, 'end')
        self.txtrecebimento.delete(0, 'end')
        self.txtantecipacao.delete(0, 'end')
        self.checkblackfriday.deselect()

ctypes.windll.kernel32.FreeConsole()

root = Tk()
root.title("Calculadora de antecipacao")
root.iconbitmap('antecipacao1.ico')

blackfriday = IntVar()
blackfriday.set(0)

Application(root)
root.mainloop()