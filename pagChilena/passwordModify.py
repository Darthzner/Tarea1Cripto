import time
#import string
#import random
from selenium import webdriver
#from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys


def ModifyPass():
    driver = webdriver.Chrome('C:/Seleniu_Chrome_driver/chromedriver')
    driver.get("https://bip.cl/canasta")
    time.sleep(3)    
    usuario= driver.find_element_by_id("usuario")
    usuario.clear()
    usuario.send_keys("carrascolester17@gmail.com")
    clave= driver.find_element_by_id("clave")
    clave.clear()
    clave.send_keys("123")    
    driver.find_element_by_id('btnIngreso').click()    
    time.sleep(2)
    driver.get("https://bip.cl/acount/micuenta")
    time.sleep(3)
    driver.find_element_by_id("btnMiPerfil").click()
    time.sleep(2)
    contrasenia = driver.find_element_by_id("contrasenia")
    contrasenia.clear()
    contrasenia.send_keys("1234")
    rcontrasenia= driver.find_element_by_name('rcontrasenia')
    rcontrasenia.clear()
    rcontrasenia.send_keys("1234")
    driver.find_element_by_id('btnGuardarPerfil').click()    
    
    time.sleep(5)
    driver.quit()
    

    
    

if __name__ == "__main__":
    ModifyPass()

