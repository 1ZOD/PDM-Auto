from tkinter import filedialog
import tkinter as tk
import tkinter.messagebox
from utils import *
from pdm_web import *
from botoes_aplicaçao import *
import os



class Processamento:
    def __init__(self):
        self.processo_fluxo_completo()
        pass

    def processo_fluxo_completo(self):
        lista_de_artigos_que_foram_processados = []
        while True:
            lista_de_artigos_originais = Util().lista_de_artigos_originais()
            for codigo in lista_de_artigos_originais:
                Pdm().preencher_campo_artigo(codigo)   
                lista_de_artigos_que_foram_processados.append(codigo)
                verificacao = True
                while verificacao:
                    Botoes().tela1()
                    try :
                        Pdm().clicar_na_janela_de_criaçao_do_pdf()
                        verificacao = False
                    except Exception:
                        tk.messagebox.showinfo(title="ERROR", message="Select the required fields")
                
                if Botoes().selecionar_pdf_excel() ==  1:
                    Util().cria_txt_com_a_lista_de_artigos_que_faltam(lista_de_artigos_que_foram_processados)
                    tk.messagebox.showinfo(title="DonwLoad", message="Please wait donwload has been completed")
                    Pdm().volta_pagina_home()
                    
                else:
                    Util().cria_txt_com_a_lista_de_artigos_que_faltam(lista_de_artigos_que_foram_processados)
                    Pdm().realiza_a_troca_das_guias_do_google()
                    Botoes().tela2()
                    Pdm().realiza_o_donwload_do_pdf(codigo)


            if len(lista_de_artigos_originais) == 0 :
                tk.messagebox.showinfo(title="End", message="All articles have been processed")              
                os.remove("arquivo.txt")
                break
                