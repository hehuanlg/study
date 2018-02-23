from selenium import webdriver
import unittest
from time import sleep

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.maximize_window()
    
    #定义登录方法
    def login(self,username,password):                
        self.driver.get('https://www.dianpuguanjia.com/#/login')
        sleep(6)
        self.driver.find_element_by_class_name('active').click()
        self.driver.find_element_by_name('telephone').clear()
        self.driver.find_element_by_name('telephone').send_keys(username)
        self.driver.find_element_by_name('password').clear()
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_id('login_submit_btn').click()
        sleep(3)
  
    #正确用户名、密码登录
    def test_01_login_success(self):
        self.login('18691627338','123456789')
        #sleep(3)
        self.driver.find_element_by_class_name('guidance-close').click()
        success_message = self.driver.find_element_by_class_name('title').text
        #self.driver.get_screenshot_as_file('D:\\test\\login_success.jpg')
        self.assertTrue('储值卡消费' in success_message)
        #self.driver.find_element_by_class_name('dropdown').click()
        #self.driver.find_element_by_link_text('退出登录').click()
        
    #错误用户名正确密码
    def test_02_error_user(self):
        self.login('18691627666','123456789')
        #sleep(2)
        error_message = self.driver.find_element_by_css_selector('p.ngMessages-err.ng-scope').text
        #self.driver.get_screenshot_as_file('D:\\test\\error_user.jpg')
        self.assertIn('账号或者密码不正确',error_message)
        
    #正确用户名错误密码
    def test_03_error_pwd(self):
        self.login('18691627338','12345678')
        #sleep(3)
        error_pwd = self.driver.find_element_by_css_selector('p.ngMessages-err.ng-scope').text
        #self.driver.get_screenshot_as_file('D:\\test\\error_pwd.jpg')
        self.assertIn('账号或者密码不正确',error_pwd)

    #账户为空
    def test_04_null_user(self):
        self.login('','123456789')
        #sleep(3)
        error_null_user = self.driver.find_element_by_css_selector('div.ngMessages-err.ng-scope.ng-active').text
        #self.driver.get_screenshot_as_file('D:\\test\\null_user.jpg')
        self.assertIn('请输入登录账号',error_null_user)

    #密码为空
    def test_05_null_pwd(self):
        self.login('18691627338','')
        #sleep(3)
        error_null_pwd = self.driver.find_element_by_css_selector('div.ngMessages-err.ng-scope.ng-active').text
        #self.driver.get_screenshot_as_file('D:\\test\\null_pwd.jpg')
        self.assertIn('请输入密码',error_null_pwd)
        
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
