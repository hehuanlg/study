from time import sleep
from selenium import webdriver
import unittest
from learinnig.logins import Login
class LoginCase(unittest.TestCase):
    '''登录测试用例'''
    #正确用户名密码
    def test_login_success(self):
        self.dr = Login('18691627338','123456789')
        self.dr.driver.find_element_by_class_name('guidance-close').click()
        success_message = self.dr.driver.find_element_by_class_name('title').text
        self.assertTrue('储值卡消费' in success_message)
    
    #用户名错误    
    def test_error_user(self):
        self.dr = Login('18691627666','123456789')
        error_user = self.dr.driver.find_element_by_css_selector('p.ngMessages-err.ng-scope').text
        self.assertIn('账号或者密码不正确',error_user)
    
    #密码错误
    def test_error_pwd(self):
        self.dr = Login('18691627338','12345678')
        error_pwd = self.dr.driver.find_element_by_css_selector('p.ngMessages-err.ng-scope').text
        self.assertIn('账号或者密码不正确',error_pwd)
    
    #用户名为空
    def test_null_user(self):
        self.dr = Login('','123456789')
        null_user = self.dr.driver.find_element_by_css_selector('div.ngMessages-err.ng-scope.ng-active').text
        self.assertIn('请输入登录账号',null_user)
        
    #密码为空
    def test_null_pwd(self):
        self.dr = Login('18691627338','')
        null_pwd = self.dr.driver.find_element_by_css_selector('div.ngMessages-err.ng-scope.ng-active').text
        self.assertIn('请输入密码',null_pwd) 
    
    #关闭所有窗口    
    def tearDown(self):
        self.dr.driver.quit()
#unittest.main()
