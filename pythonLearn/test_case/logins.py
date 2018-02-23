from selenium import webdriver
from time import sleep
class Login():
    def __init__(self,username,password):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.dianpuguanjia.com/#/login')
        sleep(6)
        self.driver.find_element_by_class_name('active').click()
        self.driver.find_element_by_name('telephone').clear()
        self.driver.find_element_by_name('telephone').send_keys(username)
        self.driver.find_element_by_name('password').clear()
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_id('login_submit_btn').click()
        sleep(3)