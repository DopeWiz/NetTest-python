#Tool by:- DopeWiz(https://github.com/DopeWiz)

import os
from time import sleep


temp = ["\n##-- "," --##"]
def end():
    print(temp[0]+"Quiting!!"+temp[1])
    sleep(0.5)
    exit()

def net_test():
    i=1
    while True:
        try:
            print(temp[0]+"Trying"+temp[1])
            print('Try:\t'+str(i)+"\t(Might take some time if slow connection a$
            res = os.system('ping -c 1 8.8.8.8 > /dev/null')
            i+=1
            if(res==0):
                print(temp[0]+"Network Reachable!!"+temp[1])
            elif(res==256):
                print(temp[0]+"No internet access!!"+temp[1])
            elif(res==2):
                print(temp[0]+"Aborted by user"+temp[1])
                end()
            else:
                print(temp[0]+"No Connection!!"+temp[1])
            sleep(0)
        except KeyboardInterrupt:
           print(temp[0]+"Aborted by user"+temp[1])
           end()
net_test()
