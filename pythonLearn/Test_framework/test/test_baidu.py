import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_framework.utils.config import Config,DRIVER_PATH
from Test_framework.utils.log import logger
class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    #只获取当前文件的上级路径
    # base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
    # #放driver的地址
    # driver_path = os.path.abspath(base_path+'\drivers\chromedriver.exe')

    locator_kw = (By.ID,'kw')
    locator_su = (By.ID,'su')
    locator_result = (By.XPATH,'//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH+'\chromedriver.exe')
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()
    def test_search_0(self):
        self.driver.find_element(*self.locator_kw).send_keys('hello')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)

    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys('python')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)







if __name__ == '__main__':
    unittest.main()
