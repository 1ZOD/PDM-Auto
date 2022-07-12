from tkinter import filedialog
import pandas as pd
import tkinter as tk
import tkinter.messagebox


class Util:
    def pegar_caminho(self):
        selecionar_excel = filedialog.askopenfilename(initialdir="/",title="Select file",filetypes=(('Microsoft Excel Worksheet', '*.xlsx'),("all files", "*.*")))
        return selecionar_excel

    def lista_codigos_extraidos(self):
        arquivo = self.pegar_caminho()
        excel = pd.read_excel(arquivo, usecols=[0,2],skiprows=2)
        teste = pd.DataFrame(excel,columns = ['Global Article', 'Status'])

        lista_filtrada = []
        artigo = []
        status = []

        for a in teste['Global Article']:
            artigo.append(a)
        for m in teste['Status']:
            status.append(m)

        lista_codigos = []
        index = 0
        for a in artigo:
            lista_codigos.append(a)
            b = status[index]
            lista_codigos.append(b)
            index += 1

        lista_dict = {lista_codigos[i]: lista_codigos[i+1] for i in range(0, len(lista_codigos),2)}
        for key, val in lista_dict.items():
            if val != "Dropped" and val != "drop":
                lista_filtrada.append(key)
        return lista_filtrada


    def filtro_modelname_planilha(self):
        arquivo = self.pegar_caminho()
        excel = pd.read_excel(arquivo, usecols=[0,4],skiprows=2)
        teste = pd.DataFrame(excel,columns = ['Global Article', 'Model name'])
        modelos = []
        artigos = []

        for a in teste['Global Article']:
            modelos.append(a)
        for m in teste['Model name']:
            artigos.append(m)

        nova_lista = []
        index = 0
        for a in artigos:
            nova_lista.append(a)
            b = modelos[index]
            nova_lista.append(b)
            index += 1
        return nova_lista
        
    def ler_txt(self):
        try:
            with open("arquivo.txt") as txt:
                texto = txt.readlines() 
                comprimento_txt = len(texto)
                return comprimento_txt
        except:
            pass

    def verifica_se_txt_esta_no_codigo(self):
        try:
            f = open('arquivo.txt')
            f.close()
        except:
            arquivo = open("arquivo.txt","w",encoding="utf-8")
            lista = self.lista_codigos_extraidos()
            for item in lista:
                arquivo.write("%s\n" % item)

    def lista_de_artigos_originais(self):
        lista_de_artigos_originais = []
        with open("arquivo.txt",encoding="utf-8") as a:
            texto= a.readlines() 
        for codigo in texto:
            lista_de_artigos_originais.append(codigo)
        return lista_de_artigos_originais

    def cria_txt_com_a_lista_de_artigos_que_faltam(self,lista_de_artigos_que_foram_processados):
        lista_de_artigos_originais = self.lista_de_artigos_originais()
        nova_lista= []
        for codigo in lista_de_artigos_originais:
            if codigo not in lista_de_artigos_que_foram_processados:
                nova_lista.append(codigo)
            with open("arquivo.txt","w",encoding="utf-8") as arquivo:
                arquivo.writelines(nova_lista)


   





