import serial
import time

ser = serial.Serial("/dev/ttyUSB0",115200,timeout = 0.1)
time.sleep(2)

ser.write(chr(123))
ser.close()