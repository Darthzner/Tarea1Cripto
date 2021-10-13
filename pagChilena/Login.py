import time
#import string
#import random
from selenium import webdriver
#from selenium.webdriver.chrome import options
#from selenium.webdriver.common.keys import Keys


def Login():
    driver = webdriver.Chrome('../Seleniu_Chrome_driver/chromedriver.exe')
    driver.get("https://bip.cl/canasta")
    time.sleep(3)    
    usuario= driver.find_element_by_id("usuario")
    usuario.clear()
    usuario.send_keys("carrascolester17@gmail.com")
    clave= driver.find_element_by_id("clave")
    clave.clear()
    clave.send_keys("123")    
    driver.find_element_by_id('btnIngreso').click()
    time.sleep(15)
    driver.quit()
    

if __name__ == "__main__":
    Login()

