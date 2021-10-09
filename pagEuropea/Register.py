import time
#import string
#import random
from selenium import webdriver
#from selenium.webdriver.chrome import options
#from selenium.webdriver.common.keys import Keys




def Register():
    driver = webdriver.Chrome('C:/Seleniu_Chrome_driver/chromedriver')
    driver.get("https://www.trendingpc.es/mi-cuenta/")
    time.sleep(3)    
    reg_email= driver.find_element_by_id("reg_email")
    reg_email.clear()
    reg_email.send_keys("carrascolester17@gmail.com")    
    driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/button').click()
    time.sleep(5)
    driver.quit()
    

if __name__ == "__main__":
    Register()


