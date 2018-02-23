from selenium import webdriver
from time import sleep
def login(username,password):
    driver = webdriver.Firefox()
    driver.get('https://www.dianpuguanjia.com/#/login')
    sleep(6)
    driver.find_element_by_class_name('active').click()
    driver.find_element_by_name('telephone').clear()
    driver.find_element_by_name('telephone').send_keys(username)
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_id('login_submit_btn').click()
    sleep(3)