import time
for i in range(10):
    print(str(i)+'\n'+str(i)+'\n'+str(i)+'\n'+'\033[3A')
    time.sleep(1)


# import sys,time
# for x in range(10):
#     sys.stdout.write('\r'+str(x))
#     sys.stdout.flush()
#     time.sleep(1)