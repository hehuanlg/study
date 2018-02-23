from selenium import webdriver
#添加cookie
dr = webdriver.Firefox()
dr.get('http://www.baidu.com')
cookie = dr.get_cookies()
dr.add_cookie({'name':'hhhhh','value':'yyyyy'})
for cook in dr.get_cookies():
    print(cook)
print(cookie)
dr.quit()