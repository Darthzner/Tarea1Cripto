import time
import string
import random
from selenium import webdriver
#from selenium.webdriver.chrome import options
#from selenium.webdriver.common.keys import Keys


def Login():
    letter = string.ascii_lowercase
    driver = webdriver.Chrome('C:/Seleniu_Chrome_driver/chromedriver')
    driver.get("https://bip.cl/canasta")
    time.sleep(3)    
    for i in range(100):
        usuario= driver.find_element_by_id("usuario")
        usuario.clear()
        usuario.send_keys("carrascolester17@gmail.com")
        clave= driver.find_element_by_id("clave")
        str = ''.join(random.choice(letter) for k in range(10))
        clave.clear()
        clave.send_keys(str)    
        driver.find_element_by_id('btnIngreso').click()
        time.sleep(1.5)
        driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/button[1]').click()
        print(i+1)
        
    time.sleep(10)
    driver.quit()
    

if __name__ == "__main__":
    Login()

