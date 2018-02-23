from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.implicitly_wait(10)
#窗口切换
search_windows = driver.current_window_handle
driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()
all_handles = driver.window_handles
for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print('login window')
        driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys('user')
        driver.find_element_by_id('TANGRAM__PSP_3__password').send_keys('pas')
        time.sleep(2)
for handle in all_handles:
    if handle == search_windows:
        driver.switch_to.window(handle)
        print('search window')
        driver.find_element_by_class_name('close-btn').click()
        driver.find_element_by_id('kw').send_keys('selenium')
        driver.find_element_by_id('su').click()
        time.sleep(2)
driver.quit()
#接受警告框
# link = driver.find_element_by_link_text('设置')
# ActionChains(driver).move_to_element(link).perform()
# driver.find_element_by_link_text('搜索设置').click()
# driver.find_element_by_class_name('prefpanelgo').click()
# time.sleep(2)
# driver.switch_to_alert().accept()
# driver.quit()
