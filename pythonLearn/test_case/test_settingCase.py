from learinnig.logins import Login
import unittest
from time import sleep
import unittest
from time import sleep

from learinnig.logins import Login


class SettingCase(unittest.TestCase):
    '''商户设置测试用例'''
    #正常商品名称
    def test_normal_name(self):
        self.dr = Login('18691627338','123456789')
        self.dr.driver.find_element_by_class_name('guidance-close').click()
        self.dr.driver.find_element_by_xpath("//ul[@id='side-menu']/li[3]/a/span").click()
        sleep(2)
        self.dr.driver.find_element_by_link_text('商户信息').click()
        self.dr.driver.find_element_by_css_selector("header > div").click()
        sleep(3)
        self.dr.driver.find_element_by_xpath("//input[@type='text']").clear()
        self.dr.driver.find_element_by_xpath("//input[@type='text']").send_keys('厉害的店')
        self.dr.driver.find_element_by_css_selector('div.btn.button-primary').click()
        sleep(5)
        success_message = self.dr.driver.find_element_by_css_selector('div.merchant-name.ng-binding').text
        self.assertIn('厉害的店',success_message)
    def tearDown(self):
        self.dr.driver.quit()
#unittest.main()
