import time
#import string
#import random
from selenium import webdriver
#from selenium.webdriver.chrome import options
#from selenium.webdriver.common.keys import Keys


def Login():
    driver = webdriver.Chrome('C:/Seleniu_Chrome_driver/chromedriver')
    driver.get("https://www.trendingpc.es/mi-cuenta/")
    time.sleep(3)    
    usuario= driver.find_element_by_id("username")
    usuario.clear()
    usuario.send_keys("carrascolester17@gmail.com")
    clave= driver.find_element_by_id("password")
    clave.clear()
    clave.send_keys("Papita12345678")    
    driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/button').click()
    time.sleep(15)
    driver.quit()
    

if __name__ == "__main__":
    Login()

