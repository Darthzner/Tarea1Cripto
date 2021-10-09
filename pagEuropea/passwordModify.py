import time
#import string
#import random
from selenium import webdriver
#from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys


def ModifyPass():
    driver = webdriver.Chrome('C:/Seleniu_Chrome_driver/chromedriver')
    driver.get("https://www.trendingpc.es/mi-cuenta/")
    time.sleep(3)    
    usuario= driver.find_element_by_id("username")
    usuario.clear()
    usuario.send_keys("carrascolester17@gmail.com")
    clave= driver.find_element_by_id("password")
    clave.clear()
    clave.send_keys("Solidsnake023A")    
    driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/button').click()    
    time.sleep(2)
    driver.get("https://www.trendingpc.es/mi-cuenta/edit-account/")
    time.sleep(3)  
    
    contraseniaA = driver.find_element_by_id("password_current")
    contraseniaA.clear()
    contraseniaA.send_keys("Papita12345678")
    contrasenia = driver.find_element_by_id("password_1")
    contrasenia.clear()
    contrasenia.send_keys("Papita12345678")
    rcontrasenia= driver.find_element_by_name('password_2')
    rcontrasenia.clear()
    
    rcontrasenia.send_keys("Papita12345678")
    driver.find_element_by_xpath('//*[@id="post-12"]/div/div/div/form/p[5]/button').click()    
    
    time.sleep(5)
    
    driver.quit()
    

    
    

if __name__ == "__main__":
    ModifyPass()

