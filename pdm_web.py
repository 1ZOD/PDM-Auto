from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import tkinter as tk
import pyautogui
from tkinter import *

class Pdm:
    def __init__(self):
        pass

    def tela_login_pdm(self,user,senha):
        global navegador 
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        navegador = webdriver.Chrome(options=options)
        navegador.get("https://pdm.adidas.com/adipdm/mypdm_dev.jsp")    
        navegador.find_element_by_xpath('//*[@id="adfsDomain"]').send_keys(Keys.DOWN * 3)
        navegador.find_element_by_xpath("/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[5]/td[2]/input").send_keys(user)
        navegador.find_element_by_xpath("/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[6]/td[2]/input").send_keys(senha)
        time.sleep(2)
        navegador.find_element_by_xpath("/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[7]/td[2]/div/a/img").click()
    
    def preencher_campo_artigo(self,codigo):
        navegador.get("https://pdm.adidas.com/adipdm/bom_product_brief_search_view.jsp?report=&view=optimized")
        navegador.find_element_by_xpath('//*[@id="DIV4_HEIGHT"]/form/table/tbody/tr[13]/td[2]/input').send_keys(codigo)
    

    def clicar_na_janela_de_criaçao_do_pdf(self):
        navegador.find_element_by_xpath('/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/form[1]/table[1]/tbody/tr/td/table/tbody/tr[15]/td[1]/input[2]').click()
        time.sleep(3)
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.find_element_by_xpath('/html/body/form[1]/table/tbody/tr[3]/td[2]/table/tbody/tr[9]/td[2]/input').click()
        navegador.find_element_by_xpath('/html/body/form[1]/table/tbody/tr[3]/td[2]/table/tbody/tr[10]/td[2]/input').click()
        navegador.find_element_by_xpath('/html/body/form[1]/table/tbody/tr[3]/td[2]/table/tbody/tr[11]/td[2]/input').click()
        navegador.find_element_by_xpath('/html/body/form[1]/table/tbody/tr[3]/td[2]/table/tbody/tr[12]/td[2]/input').click()
        navegador.find_element_by_xpath('/html/body/form[1]/table/tbody/tr[3]/td[2]/table/tbody/tr[13]/td[2]/input').click()
        navegador.find_element_by_xpath('/html/body/form[1]/table/tbody/tr[3]/td[2]/table/tbody/tr[14]/td[2]/input').click()

    def navegar_retornado(self):
        return navegador
        
    def realiza_a_troca_das_guias_do_google(self):
        navegador.switch_to.window(navegador.window_handles[0])
        navegador.switch_to.window(navegador.window_handles[1])

    def realiza_o_donwload_do_pdf(self,codigo):
        pyautogui.size()
        (1920,1080)
        pyautogui.hotkey('Ctrl',"s")
        time.sleep(4)
        pyautogui.typewrite(codigo)
        pyautogui.press("Enter")
        navegador.close()
        navegador.switch_to.window(navegador.window_handles[0])

    def volta_pagina_home(self):
        navegador.switch_to.window(navegador.window_handles[0])