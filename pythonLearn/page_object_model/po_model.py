from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
class Page(object):
    """
    基础类，用于对象类继承
    """
    login_url = 'http://mail.163.com'
    def __init__(self,selenium_driver,base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.driver.implicitly_wait(10)


    def on_page(self):
        #获取当前浏览器url
        return self.driver.current_url == (self.base_url + self.url)
    #内部函数
    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        self.driver.switch_to.frame('x-URS-iframe')
        #断言，若为假则输出后面的字符串
        assert self.on_page(),'did not land on %s' % url

    def open(self):
        self._open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

class LoginPage(Page):
    """
    登录页面模型
    """
    url = '/'
    #定位器

    username_loc = (By.NAME, "email")
    password_loc = (By.NAME, 'password')
    submit_loc = (By.ID, 'dologin')
    #Action
    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()
def test_user_login(driver,username,password):
    """登录测试"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()
def main():
    try:
        driver = webdriver.Firefox()
        username = 'hehuanlg'
        password = input('password:')
        test_user_login(driver,username,password)
        sleep(3)
        text = driver.find_element_by_id("spnUid").text
        assert(text=='hehuanlg@163.com'),'登录失败'
    finally:
        driver.close()
if __name__ == "__main__":
    main()

