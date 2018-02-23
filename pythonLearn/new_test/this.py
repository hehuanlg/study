# a = ['a','b','c','d','e','f']
# b = ['1','2','3','4','5','6']
# for key,value in zip(a,b):
#     print(key,value)
# aa = 'test'
# try:
#     print(aa)
#     #open('abc.txt','r')
# except Exception as msg:
#     print(msg)
# else:
#     print('no error')
from selenium import webdriver
from time import sleep,ctime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
first_url = 'http://www.baidu.com'
# print('now url %s' %(first_url))
# driver.get(first_url)
# size = driver.find_element_by_id('kw').size
# print(size)
# dirver.quit()
driver.get(first_url)

#显式等待
# print(ctime())
# for i in range(10):
#     try:
#         el = driver.find_element_by_id('kw22')
#         if el.is_displayed():
#             print('ok')
#             break
#     except:pass
#     sleep(1)
# else:
#     print('timeout')
# driver.quit()
# print(ctime())

element = WebDriverWait(driver,5,1).until(EC.presence_of_element_located((By.ID,'kw')))
element.send_keys('selenium')
driver.quit()

#隐式等待
# driver.implicitly_wait(10)
# try:
#     print(ctime())
#     driver.find_element_by_id('kw')
#     print('yes')
# except Exception as msg:
#     print(msg)
# finally:
#     print(ctime())
#     driver.quit()

#死等：sleep