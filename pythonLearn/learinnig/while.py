number = 22
run = True
while run:
    ipt = int(input('请输入数字'))
    if ipt == number:
        print('yes,you are right')
        run = False
    elif ipt > number:
        print('you are wrong,too big')
    else:
        print('you are wrong,too small')
print('done')