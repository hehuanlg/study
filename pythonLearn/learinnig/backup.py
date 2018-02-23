import os
import time
source = ['C:\\pythonLearn']

target_dir = 'D:\\Backup'

target = target_dir + os.sep +time.strftime('%Y%m%d%h%M%S') + '.rar'
rar_command = "rar -qr {0} {1}".format(target, ' '.join(source))
if os.system(rar_command) == 0:
    print('successful backup to',target)
else:
    print('backup failed')
