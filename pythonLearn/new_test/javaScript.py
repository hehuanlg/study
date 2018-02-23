from selenium import webdriver
from time import sleep
import logging
#调用javascrript控制水平和垂直滚动条
logging.basicConfig(level=logging.DEBUG)
dr = webdriver.Firefox()
dr.get('http://www.baidu.com')
dr.set_window_size(600,600)
dr.find_element_by_id('kw').send_keys('selenium')
dr.find_element_by_id('kw').click()
sleep(2)
js = 'scrollTo(100,450);'
dr.execute_script(js)
