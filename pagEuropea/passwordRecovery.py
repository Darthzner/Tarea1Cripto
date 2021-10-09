import time
#import string
#import random
from selenium import webdriver
#from selenium.webdriver.chrome import options
#from selenium.webdriver.common.keys import Keys


def Recovery():
    driver = webdriver.Chrome('C:/Seleniu_Chrome_driver/chromedriver')
    driver.get("https://www.trendingpc.es/mi-cuenta/lost-password/")
    time.sleep(3)    
    usuario= driver.find_element_by_id("user_login")
    usuario.clear()
    usuario.send_keys("carrascolester17@gmail.com")    
    driver.find_element_by_xpath('//*[@id="post-12"]/div/div/form/p[3]/button').click()
    time.sleep(5)
    driver.quit()
    

if __name__ == "__main__":
    Recovery()
