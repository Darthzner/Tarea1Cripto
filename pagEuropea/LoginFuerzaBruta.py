import time
import string
import random
from selenium import webdriver
#from selenium.webdriver.chrome import options
#from selenium.webdriver.common.keys import Keys


def Login():
    letter = string.ascii_lowercase
    driver = webdriver.Chrome('C:/Seleniu_Chrome_driver/chromedriver')
    driver.get("https://www.trendingpc.es/mi-cuenta/")
    time.sleep(3)    
    for i in range(100):       
           
        usuario= driver.find_element_by_id("username")
        usuario.clear()
        usuario.send_keys("carrascolester17@gmail.com")
        str = ''.join(random.choice(letter) for k in range(10))
        clave= driver.find_element_by_id("password")
        clave.clear()
        clave.send_keys(str)    
        driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/button').click()    
        
        
        
        print(i+1)
        
    time.sleep(10)
    driver.quit()
    

if __name__ == "__main__":
    Login()

