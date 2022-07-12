import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
from botoes_aplicaçao import Botoes
from pdm_web import Pdm
from utils import Util
import os

class Canvas:
    def __init__(self):  
        pass

    def canvasx(self):
        window = tk.Tk()

        #Define o tamanho da tela
        largura = 862
        altura = 519
        largura_tela= window.winfo_screenwidth()
        altura_tela = window.winfo_screenheight()
        posx = largura_tela/2 - largura/2
        posy = altura_tela/2 - altura/2
        window.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
        window.resizable(False, False)

        adidas_png = "./img/adidas.png"
        iconbitmap = "./img/iconbitmap.gif"
        gerador = "./img/generate.png"
        box = "./img/TextBox_Bg.png"
        icone_arquivo = "./img/path_picker.png"
        lixo = "./img/lixo.png"
        filtro = "./img/filtro.png"

        logo = tk.PhotoImage(file = iconbitmap)
        window.call('wm', 'iconphoto', window._w, logo)
        window.title("Adidas Tools")

        #O Canvas é uma área retangular destinada a desenhar imagens ou outros layouts complexos.
        canvas = tk.Canvas(window, bg="#3A7FF6",height=519, width=862,bd= 0,highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        #Cria dois retangulos na tela, o primeiro é o fundo branco da direita , e o outro é pequeno e fica no canto esquerdo
        canvas.create_rectangle(431,0,431 + 431, 0 + 519, fill="#FCFCFC",outline="")
        canvas.create_rectangle(40,160,40 + 60,160 + 5,fill="#FCFCFC",outline="")


        #Importa a foto do campo do botao aquele redondinho
        caixa_de_texto_bg = tk.PhotoImage(file= box)

        #Coloca a imagem no retangulo
        # usuario_campo
        canvas.create_image(650.5, 167.5, image= caixa_de_texto_bg)
        # senha_campo
        canvas.create_image(650.5, 248.5, image= caixa_de_texto_bg)

        #Adiciona o campo de digitaçao
        usuario_digita = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
        usuario_digita.place(x=490.0, y=137+25, width=321.0, height=35)
        usuario_digita.focus()

        senha_digita = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0,show = "*")
        senha_digita.place(x=490.0, y=218+25, width=321.0, height=35)

        #Adiciona o Texto nos campos
        canvas.create_text(575.5, 88.0, text="Login",fill="#515486", font=("Arial-BoldMT", int(20.0)))
        canvas.create_text(490.0, 152.0, text="Username", fill="#515486",font=("Arial-BoldMT", int(13.0)), anchor="w")
        canvas.create_text(490.0, 234.5, text="Password", fill="#515486",font=("Arial-BoldMT", int(13.0)), anchor="w")
        canvas.create_text(720.5, 290.5, text="Save Login", fill="#515486",font=("adineue TEXT", int(10.0)), anchor="w")
        canvas.create_text(646.5, 428.5, text="Generate",fill="#FFFFFF", font=("Arial-BoldMT", int(13.0)))

        # Criado o campo da esquerda 
        adidas_logo = tk.PhotoImage(file = adidas_png)
        canvas.create_image(210.0, 50.5, image= adidas_logo)

        def botao_para_selecionar_artigo():
            Botoes().botao_continuar_onde_parou() 

        #Import o png e cria um botao flat
        continuar_img= tk.PhotoImage(file = icone_arquivo)
        continuar_de_onde_parou = tk.Button(image= continuar_img,text ="",borderwidth=0, bg='#f6f7f9',highlightthickness=0, command=botao_para_selecionar_artigo ,relief="flat", font=("Arial-BoldMT", int(9.0)))
        continuar_de_onde_parou.place(x=800, y=20.5, width=40, height=25)

        def salvar_login():
                usuario = usuario_digita.get()
                senha = senha_digita.get()
                if chkValue.get() == 1:
                    arquivo = open("login.txt","w",encoding="utf-8")
                    for valores in usuario,senha:
                        arquivo.write("%s\n" % valores)
                else:
                    os.remove("login.txt")
                
        chkValue = tk.IntVar() 
        chkExample = tk.Checkbutton(window, text='',variable = chkValue, onvalue=1, offvalue=0, bg='#ffffff', command= salvar_login) 
        chkExample.place(x=810.5, y=278.5)


        def verificacao_se_os_campos_login_estao_preenchidos():
            """
            Está função pega as infomações passadas do login
            """
            user = usuario_digita.get()
            senha = senha_digita.get()

            if not user:
                tk.messagebox.showerror(title="Wrong username", message="Please, write the username")
                return

            if not senha:
                tk.messagebox.showerror(title="Wrong password", message="Please, write the password")
                return

            window.destroy()
            Util().verifica_se_txt_esta_no_codigo()
            Pdm().tela_login_pdm(user,senha)


        generate_btn_img = tk.PhotoImage(file = gerador)
        generate_btn = tk.Button(image=generate_btn_img, borderwidth=0, highlightthickness=0, command= verificacao_se_os_campos_login_estao_preenchidos,relief="flat")
        generate_btn.place(x=547, y=401, width=180, height=55)


        def apagar_planilha():
            Botoes().remover_planilha_geral() 

        lixo_btn_img = tk.PhotoImage(file = lixo)
        lixo_btn = tk.Button(image=lixo_btn_img,borderwidth=0, bg='#f6f7f9',highlightthickness=0, command= apagar_planilha,relief="flat")
        lixo_btn.place(x=760, y=20.5, width=40, height=25)

        def filtrar_planilha():
            Botoes().filtro_planilha()

        filtro_img = tk.PhotoImage(file = filtro)
        filtro_btn = tk.Button(image= filtro_img,borderwidth=0, bg='#f6f7f9',highlightthickness=0, command= filtrar_planilha,relief="flat")
        filtro_btn.place(x=725, y=20.5, width=40, height=25)


        #Cria o Titulo do lado esquerdo
        title = tk.Label(text="Welcome to Adidas Tools", bg="#3A7FF6",fg="white", font=("adineue TEXT", int(18.0)))
        title.place(x=25.0, y=120.0)
        # lista_total_codigos = Util().ler_txt()
        info_text = tk.Label(
        text=("Excel file name: \n"
            "Article number: \n"
            "Processed articles: 5\n"
            "\n\n\n\n\n\n\n"
            "v 1.0"),
            bg="#3A7FF6", fg="white", justify="left",
            font=("adineue TEXT", int(14.0)))

        info_text.place(x=27.0, y=200.0)

        
        # Verifica se o TXT existe, se sim ele chama o campo para passar o artigo, caso contrario o campo é removido
        try:
            f = open('arquivo.txt')
            f.close()
        except:
            continuar_de_onde_parou.place(x=30000.5, y=30000.5)
            lixo_btn.place(x=30000.5, y=30000.5)
            filtro_btn.place(x=30000.5, y=30000.5)

        try: 
            nova_lista = []
            with open("login.txt") as login:
                texto = login.readlines()
                for logar in texto:
                    nova_lista.append(logar)
           
            chkValue.set(True)

            usuario_digita.insert(0, nova_lista[0])
            senha_digita.insert(0, nova_lista[1])

        except :
            pass

                
        window.mainloop()
    
if __name__ == '__main__':
    Canvas().canvasx()