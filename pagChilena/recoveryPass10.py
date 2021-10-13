import time
#import string
#import random
from selenium import webdriver
#from selenium.webdriver.chrome import options
#from selenium.webdriver.common.keys import Keys


def Recovery():
    for item in range(10):
     
        driver = webdriver.Chrome('../Seleniu_Chrome_driver/chromedriver.exe')
        driver.get("https://bip.cl/acount/recordar/")
        time.sleep(3)    
        usuario= driver.find_element_by_id("usuario")
        usuario.clear()
        usuario.send_keys("carrascolester17@gmail.com")    
        driver.find_element_by_id('btnRecordar').click()
        time.sleep(5)
        driver.quit()
    

if __name__ == "__main__":
    Recovery()
