import time
import string
import random
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys




def Register():
    driver = webdriver.Chrome('../Seleniu_Chrome_driver/chromedriver.exe')
    driver.get("https://bip.cl/acount/registro/")
    time.sleep(3)    
    name= driver.find_element_by_id("nombre")
    name.clear()
    name.send_keys("Lester")
    apellido= driver.find_element_by_id("apellido")
    apellido.clear()
    apellido.send_keys("Carrasco Muñoz")
    rut= driver.find_element_by_id("rut")
    rut.clear()
    rut.send_keys("201623790")
    fono= driver.find_element_by_id("fono")
    fono.clear()
    fono.send_keys("966679198")
    email= driver.find_element_by_id("email")
    email.clear()
    email.send_keys("carrascolester17@gmail.com")
    remail= driver.find_element_by_id("remail")
    remail.clear()
    remail.send_keys("carrascolester17@gmail.com")
    contrasenia= driver.find_element_by_id("contrasenia")
    contrasenia.clear()
    contrasenia.send_keys("asd1234")
    rcontrasenia= driver.find_element_by_id("rcontrasenia")
    rcontrasenia.clear()
    rcontrasenia.send_keys("asd1234@gmail.com")
    driver.find_element_by_id('btnRegistro').click()
    time.sleep(5)
    

if __name__ == "__main__":
    Register()




 