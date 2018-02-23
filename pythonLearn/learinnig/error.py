'''while True:
    try:
        a = input('输入第一个数字\n')
        b = input('输入第二个数字\n')
        c = int(a) + int(b)
    except ValueError:
        print('only number')
    else:
        print (c)
        break
'''
'''try:
    with open('c:\cats.txt') as file:
        files = file.read()
except FileNotFoundError:
    print('no file')
else:
    print(files)
'''
a = 'c:\\alice.txt'
with open(a) as file:
    files = file.read().split()
b = files.lower().count('the')
print(b)
print(len(files))
