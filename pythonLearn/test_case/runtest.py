import os,time,unittest,smtplib
from HTMLTestRunner_PY3 import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
#发邮件
def send_mail(file_new):
    user = 'hehuanlg@163.com'
    password = input('password:')
    receiver = input('to:')

    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,'html','utf-8')
    msg['subject'] = Header('自动化测试报告','utf-8')
    msg['From'] = user
    msg['To'] = receiver
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(user,password)
    smtp.sendmail(user,receiver,msg.as_string())
    smtp.quit()
    print('发送成功')

#查找新生成的报告
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport+'\\'+fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return(file_new)
if __name__ == '__main__':
    test_dir = 'C:\\pythonLearn\\test_case'
    test_report = 'C:\\pythonLearn\\test_case\\report'
    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern='test_*.py')
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    filename = test_report + '\\' + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况',
                            verbosity=2)
    runner.run(discover)
    fp.close()
    new_report = new_report(test_report)
    send_mail(new_report)


