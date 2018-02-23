'''name = input('请输入用户名')
name = str(name)
if not name.strip():
    print('over')
else:
    with open('c:\guest.txt','a') as guests:
        guests.write(name+'\n')
    print('open')
    '''
name = input('请输入用户名：\n')
name = str(name)
while name.strip():
    print('welcome to programming')
    with open('c:\guest_book.txt','a') as guests:
        guests.write(name+'\n')
    break
else:
    print('no')
