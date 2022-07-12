import tkinter as tk
from tkinter import *
import os
import sys
from utils import Util
from pdm_web import Pdm

class Botoes:
    def tela1(self):
        window = tk.Tk()
        largura = 480
        altura = 230
        largura_tela= window.winfo_screenwidth()
        altura_tela = window.winfo_screenheight()
        posx = largura_tela/1 - largura/1
        posy = altura_tela/2 - altura/2
        window.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
        window.resizable(False,False)

        iconbitmap = "./img/iconbitmap.gif"
        logo = tk.PhotoImage(file = iconbitmap)
        window.call('wm', 'iconphoto', window._w, logo)
        window.title("Adidas Tools")


        alert = Label(window, text='Please click in the Model Name and then select the Options \n'
                                    'you want to choose in the fields below:\n'
                                    ' -Model Name after\n'
                                    ' -Check the ID "Material Way" field\n'
                                    ' -Check the ID "Related Color Ways\n '
                                    ' -Select the Factory Way (-A)\n' ,height=8)
        alert.place(x=35, y=10.0)       
           

        def finalizar_tarefas():
            window.destroy()
            sys.exit()

        b1 = Button(window, text = "Continue",height=1, width=11, command=window.destroy)
        b1.place(x=120, y=170.0) 
        b2 = Button(window, text = "Abort",height=1, width=11, command= finalizar_tarefas)
        b2.place(x=250, y=170.0)

        window.mainloop()

    def tela2(self):

        tk.messagebox.showinfo(title="Download", message="Please, Wait until the page loads completely")

        #Define o tamanho da tela
        window = tk.Tk()
        largura = 400
        altura = 100
        largura_tela= window.winfo_screenwidth()
        altura_tela = window.winfo_screenheight()
        posx = largura_tela/1 - largura/1
        posy = altura_tela/2 - altura/2
        window.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
        window.resizable(False,False)

        #Pegando o caminho das pastas
        iconbitmap = "./img/iconbitmap.gif"
        logo = tk.PhotoImage(file = iconbitmap)
        window.call('wm', 'iconphoto', window._w, logo)
        window.title("Adidas Tools")


        alert = Label(window, text="Download the file?",height=2)
        alert.pack()
        pane = Frame(window)
        pane.pack() 


        def finalizar_tarefas():
            window.destroy()
            sys.exit()

        b1 = Button(pane, text = "Yes",height=1, width=5, command= window.destroy)
        b1.pack(side = LEFT)
        b2 = Button(pane, text = "No",height=1, width=5, command= finalizar_tarefas)
        b2.pack(side = LEFT)
        window.mainloop()


    def botao_continuar_onde_parou(self):

        window = tk.Tk()
        largura = 400
        altura = 120
        largura_tela= window.winfo_screenwidth()
        altura_tela = window.winfo_screenheight()
        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2
        window.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
        window.resizable(False,False)

        # Pegando o caminho das pastas
        
        window.iconbitmap("./img/app_icon.ico")
        window.title("Adidas Tools")


        alert = Label(window, text="Insert last article: \n(The program will START with the code below!!!)",height=2)
        alert.pack()
       
        numero_do_artigo_digitado = tk.Entry(window)
        numero_do_artigo_digitado.pack()
        numero_do_artigo_digitado.focus()


        def lista_de_codigos_do_txt():
            lista_de_codigos = []
            with open("arquivo.txt") as a:
                texto= a.readlines() 
                for codigo in texto:
                    lista_de_codigos.append(codigo)
                return lista_de_codigos
        
        def escolha_do_artigo():
            codigo_encontrado = False
            artigo = numero_do_artigo_digitado.get().upper()
            lista_de_codigos = list(lista_de_codigos_do_txt())
            nova_lista = []

            for codigo in lista_de_codigos:
                if str(codigo[:6]) == str(artigo):
                    tk.messagebox.showinfo(title="OK", message="Found article")    
                    codigo_encontrado = True
                if codigo_encontrado:
                    nova_lista.append(codigo)      
                    with open("arquivo.txt","w") as arquivo:
                        arquivo.writelines(nova_lista)
            window.destroy()
            
        b1 = Button( window,text = "Ok",height=1, width=5, command= escolha_do_artigo)
        b1.pack()

        window.mainloop()

    def remover_planilha_geral(self):

        window = tk.Tk()
        largura = 400
        altura = 120
        largura_tela= window.winfo_screenwidth()
        altura_tela = window.winfo_screenheight()
        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2
        window.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
        window.resizable(False,False)
        
        window.iconbitmap("./img/app_icon.ico")
        window.title("Adidas Tools")

        alert = Label(window, text="Remove current sheet ? \n(The program will ask for the path from excel again!!!)",height=2)
        alert.pack()
        
        def apagar_txt():
            try :
                os.remove("arquivo.txt")
                tk.messagebox.showinfo(title="Article", message="Your spreadsheet has been deleted")
            except :
                tk.messagebox.showinfo(title="Article", message="No worksheets left")  
            window.destroy()
            
        b1 = Button( window,text = "Ok",height=1, width=5, command= apagar_txt)
        b1.pack()

        window.mainloop()


    def filtro_planilha(self):
       
        window = tk.Tk()
        largura = 400
        altura = 120
        largura_tela= window.winfo_screenwidth()
        altura_tela = window.winfo_screenheight()
        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2
        window.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
        window.resizable(False,False)
        
        window.iconbitmap("./img/app_icon.ico")
        window.title("Adidas Tools")

        alert = Label(window, text="Enter the model name: \n(The program will filter with this Model name!!!)",height=2)
        alert.pack()
       
        numero_do_artigo_digitado = tk.Entry(window)
        numero_do_artigo_digitado.pack()
        numero_do_artigo_digitado.focus()
            
        def fazendo_filtagem():
            model_name = numero_do_artigo_digitado.get().upper()
            lista_de_codigos = Util().filtro_modelname_planilha()
            nova_lista = []
            comparador = 2

            index = 0
            for valor in lista_de_codigos:
                index += 1
                if valor == model_name:
                    nova_lista.append([lista_de_codigos[index]])
                    comparador = 1
                if model_name not in lista_de_codigos:
                    comparador = 0
            
            window.destroy()
            if comparador == 1:
                tk.messagebox.showinfo(title="Article", message="Found:"+"\n"+ model_name +"\n"+ str(nova_lista)) 
                arquivo = open("arquivo.txt","w",encoding="utf-8")
                for item in nova_lista:
                    arquivo.write("%s\n" % item[0])

            if comparador == 0:
                tk.messagebox.showinfo(title="Article", message="Not Found:"+"\n"+ model_name +"\n"+ "Try Again") 

        b1 = Button( window,text = "Ok",height=1, width=5, command= fazendo_filtagem)
        b1.pack()

        window.mainloop()

    def selecionar_pdf_excel(self):

        
        #Define o tamanho da tela
        window = tk.Tk()
        largura = 400
        altura = 100
        largura_tela= window.winfo_screenwidth()
        altura_tela = window.winfo_screenheight()
        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2
        window.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
        window.resizable(False,False)

        #Pegando o caminho das pastas
        iconbitmap = "./img/iconbitmap.gif"
        logo = tk.PhotoImage(file = iconbitmap)
        window.call('wm', 'iconphoto', window._w, logo)
        window.title("Adidas Tools")


        alert = Label(window, text="Select PDF in Excel ?",height=2)
        alert.pack()
        pane = Frame(window)
        pane.pack() 

        navegador = Pdm().navegar_retornado()
        

        def escolheu_pdf():
            global verifica
            window.destroy()
            navegador.find_element_by_xpath('/html/body/form[1]/table/tbody/tr[5]/td[2]/div/a[1]/img').click()
            navegador.switch_to.window(navegador.window_handles[1])
            navegador.close()
            valor = 0
            verifica = valor
            return verifica
            

            
        def escolheu_excel():
            global verifica
            window.destroy()
            navegador.find_element_by_xpath('/html/body/form[1]/table/tbody/tr[3]/td[2]/table/tbody/tr[15]/td[3]/input').click()
            navegador.find_element_by_xpath('/html/body/form[1]/table/tbody/tr[5]/td[2]/div/a[1]/img').click()
            navegador.switch_to.window(navegador.window_handles[1])
            navegador.close()
            valor = 1
            verifica = valor
            return verifica

            

        b1 = Button(pane, text = "PDF",height=1, width=5,command= escolheu_pdf)
        b1.pack(side = LEFT)
        b2 = Button(pane, text = "Excel",height=1, width=5,command= escolheu_excel)
        b2.pack(side = LEFT)


        window.mainloop()
        return verifica
