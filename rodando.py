import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

class trabalho():
    def __init__(self):
        self.dunf=tk.Tk()
        self.dunf.geometry("1000x500+200+100")
        self.dunf.title("Pesquisa no predio")
        self.dunf.iconbitmap("predio.ico")
        self.dunf.resizable(0,0)
        self.qnt_pessoas=0
        self.coleta=[]
        self.primaria()
        self.dunf.mainloop()
    def primaria(self):
        self.fundo = LabelFrame(self.dunf, bg="#0c66ed",text="Pesquisa para o prédio",font="Helvetica 20 bold",width=1000,height=500,bd=3,labelanchor="n")
        self.fundo.place(x=0,y=0)
        self.contador=Label(self.fundo,bg="#0c66ed",text=f"Quantidade intrevistada:{self.qnt_pessoas}",fg="white",font="Helvetica 12 bold")
        self.contador.place(x=750,y=0)
        self.prime=StringVar()
        self.segun=StringVar()
        self.ar=LabelFrame(self.fundo, bg="#0c66ed",text="Qual elevador voce mais usa ?",font="Arial 20 bold",width=600,height=70,bd=0,fg="white")
        self.ar.place(x=200,y=50)
        self.br=LabelFrame(self.fundo, bg="#0c66ed",text="Em qual periodo voce mais usa ?",font="Arial 20 bold",width=600,height=70,bd=0,fg="white")
        self.br.place(x=200,y=120)
        self.A=Radiobutton(self.ar,font="Arial 12 bold",variable=self.prime,value="Elevador_A",text="Elevador_A",bg="#0c66ed",bd=1,fg="black")
        self.A.place(x=50,y=0)
        self.B=Radiobutton(self.ar,font="Arial 12 bold",variable=self.prime,value="Elevador_B",text="Elevador_B",bg="#0c66ed",bd=1,fg="black")
        self.B.place(x=250,y=0)
        self.C=Radiobutton(self.ar,font="Arial 12 bold",variable=self.prime,value="Elevador_C",text="Elevador_C",bg="#0c66ed",bd=1,fg="black")
        self.C.place(x=450,y=0)
        self.M=Radiobutton(self.br,font="Arial 12 bold",variable=self.segun,value="Maturtino",text="Maturtino",bg="#0c66ed",bd=1,fg="black")
        self.M.place(x=50,y=0)
        self.V=Radiobutton(self.br,font="Arial 12 bold",variable=self.segun,value="Vespertino",text="Vespertino",bg="#0c66ed",bd=1,fg="black")
        self.V.place(x=250,y=0)
        self.N=Radiobutton(self.br,font="Arial 12 bold",variable=self.segun,value="Noturno",text="Noturno",bg="#0c66ed",bd=1,fg="black")
        self.N.place(x=450,y=0)

        self.add=Button(self.fundo, bg="white",text="Proximo",command=self.prox,font="Arial 12 bold",fg="black")
        self.add.place(x=700,y=400)
        self.final_buton=Button(self.fundo, bg="white",text="Finalizar",command=self.final,font="Arial 12 bold",fg="black")
        self.final_buton.place(x=800,y=400)

    def prox(self):
        self.elevador=self.prime.get()
        self.tempo=self.segun.get()
        if self.elevador and self.tempo not in "":
            self.coleta.append([self.elevador,self.tempo])
            self.qnt_pessoas+=1
            self.complemento1()
        else:
            messagebox.showerror("Erro","Existe algum campo não marcado")
    def final(self):
        if self.qnt_pessoas>=10:
            cont={}
            cont_={}
            for ele_peri in self.coleta:
                dois = tuple(ele_peri)  
                peri=ele_peri[1]
                if dois in cont:
                    cont[dois] += 1
                else:
                    cont[dois] = 1
                if peri in cont_:
                    cont_[peri] += 1
                else:
                    cont_[peri] = 1
            
            peri_mais = max(cont_, key=cont_.get)
            peri_menos_= [periudo for periudo, count in cont_.items() if count == min(cont_.values())]
            if len(peri_menos_)>=2:
                pri,seg=peri_menos_
                peri_menos_=f"{pri} e {seg}"
            if len(peri_menos_)==1:
                peri_menos_ = min(cont_, key=cont_.get)

            maior_uso = [ele_peri for ele_peri, count in cont.items() if count == max(cont.values())]
            for mais_uso in maior_uso:
                ele,perildo=mais_uso
            self.contador=Label(self.fundo,bg="#0c66ed",text=f"O Elevador mais utilizado é o {ele} no período {perildo}",fg="white",font="Helvetica 12 bold")
            self.contador.place(x=200,y=250)
            self.contador=Label(self.fundo,bg="#0c66ed",text=f"O período mais utilizado é o {peri_mais}, o período menos utilizado é o {peri_menos_}",fg="white",font="Helvetica 12 bold")
            self.contador.place(x=200,y=300)
        else:
            messagebox.showinfo("Aviso","Minimo de entrevistados, não atingido\n(Minimo= 10)")
    def complemento1(self):
        self.fundo.destroy()
        self.primaria()
trabalho()