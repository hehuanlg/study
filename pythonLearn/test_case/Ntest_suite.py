import unittest
from loginCase import LoginCase
from HTMLTestRunner_PY3 import HTMLTestRunner
from settingCase import SettingCase
import time
if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [LoginCase("test_error_user"),LoginCase("test_login_success"),
             SettingCase('test_normal_name')]
    suite.addTests(tests)
    #报告名设置为当前时间
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    ad = 'c:\\pythonLearn\\test_case\\report' + '\\'
    filename = ad + now + 'result.html'

    with open(filename,'wb') as f:
        runner = HTMLTestRunner(stream=f,title='login test report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(suite)