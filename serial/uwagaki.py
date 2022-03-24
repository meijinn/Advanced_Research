import sys, time

for i in range(10):
    s = str(i)
    sys.stdout.write("\033[G%s" % s)
    sys.stdout.flush()
    time.sleep(0.5)
print("")