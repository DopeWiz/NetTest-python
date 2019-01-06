import os
import time

def net_test():
    try:
        i=1
        while True:
            print('\n##-- Trying --##')
            print('Try:\t'+str(i))
            res = os.system('ping -c 1 8.8.8.8 > /dev/null')
            i+=1
            if(res==0):
                print("\nNetwork Reachable!!")
                time.sleep(0.5)
                exit()
            time.sleep(0.7)
    except KeyboardInterrupt:
        print('\n##--Quiting--##')
        time.sleep(0.5)
        exit()

net_test()
