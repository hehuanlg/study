import threading
from time import sleep,ctime

def music(func,loop):
    for i in range(loop):
        print('listening to %s! %s' % (func,ctime()))
        sleep(2)

def movie(func,loop):
    for i in range(loop):
        print('watching %s! %s' % (func,ctime()))
        sleep(5)
# if __name__ == '__main__':
#     music('smpp',2)
#     movie('cctv',2)
#     print('all end',ctime())

threads = []
t1 = threading.Thread(target=music,args=('pdd',2))
threads.append(t1)
t2 = threading.Thread(target=movie,args=('cctv',2))
threads.append(t2)
if __name__ == '__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
print('all end %s' % ctime())