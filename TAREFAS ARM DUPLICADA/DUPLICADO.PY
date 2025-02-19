from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui
import pandas as pd

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  
service = Service(r"C:/Program Files/Google/Chrome/Application/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get(r'https://wmswmos1942.cbd.root.gpa/manh/index.html?i=214')


def macro(by, caminho):
    return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((by, caminho)))


id_input = macro(By.XPATH, '//*[@id="username"]')
id_input.send_keys("5446902")

senha_input = macro(By.XPATH,'//*[@id="password"]')
senha_input.send_keys("@Gpafevereiro2024")


senha_input.send_keys(Keys.RETURN)  
time.sleep(3)  


actions = ActionChains(driver)

def coord(x, y,texto):
    actions.move_by_offset(x, y).click().perform()
    time.sleep(0.5)
    actions.send_keys(texto).perform()

lat = coord(14, 23, "")

input = macro(By.XPATH, '//*[@id="mps_menusearch-1230-inputEl"]')
input.send_keys("Menu RF")
time.sleep(0.5)
input.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
input.send_keys(Keys.ENTER)
imagem = r'//depo0903/gpa$/PAC/Daniel Menezes/Python/SELENIUM/TAREFAS ARM DUPLICADA/INFORMATIVO.png'

for i in range (5):
    try:
        img_list = pyautogui.locateAllOnScreen(r'//depo0903/gpa$/PAC/Daniel Menezes/Python/SELENIUM/TAREFAS ARM DUPLICADA/INFORMATIVO.png', confidence=0.8)
        if img_list:
            firs_img = img_list[0]
            position = pyautogui.center(img_list)
            print("imagem encontrada")
            pyautogui.moveTo(position, duration= 0.5)
            pyautogui.click(position)
            break
        else:
            print("imagem nao encontrada")
    except:
        print("erro ao procurar imagem")
        



time.sleep(1000)
