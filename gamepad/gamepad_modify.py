#! /usr/bin/env python
# coding: utf-8
# coding=utf-8
# -*- coding: utf-8 -*-

import pygame
import serial
from pygame.locals import *

ser = serial.Serial("/dev/ttyUSB0",115200,timeout=1)

pygame.joystick.init()

try:# 例外があるかもしれないが、実行したい処理
    j = pygame.joystick.Joystick(0) # create a joystick instance
    j.init() # init instance
    print ("Joystick name: ") + j.get_name()
    print ("Number of buttons: ") + str(j.get_numbuttons())
except pygame.error:# 例外時の処理
    print ('Joystick is not found')

def main():
    
    initialize()

    while 1:
        for e in pygame.event.get(): # イベントチェック
            if e.type == QUIT: # 終了が押された？
                pygame.quit()
                sys.exit()
            if (e.type == KEYDOWN):
                if (e.key  == K_ESCAPE): # ESCが押された？
                    pygame.quit()
            if e.type == pygame.locals.JOYAXISMOTION: # 7
                Senddata = [90, 100]
                Senddata = joyget()
                Sendster = Senddata[0]
                Sendvel = Senddata[1]
                serial_write(Sendster,Sendvel)


def initialize():
    pygame.init()
    screen = pygame.display.set_mode((400,300))
    pygame.display.set_caption("keyboard event")
    screen.fill((0,0,0))

def joyget():    
 # Joystick関連のイベントチェック
        
    input_array = []
    input_array = getUserInput(j.get_axis(0),j.get_axis(4),j.get_axis(3))
    # steeringとthrottleの戻り値を得る

    steering = constrain(input_array[0])
    throttle = input_array[1]
    # 戻り値を配列に代入

    print ('steering ' + str(steering))
    # print 'gas and brake ' + str(gas) +' , '+ str(brake)
    print ('throttle ' + str(throttle))

    return steering,throttle


def getUserInput(axis_0,axis_4,axis_3):
    
    steering = int(((j.get_axis(0)*-180)+180)/2)
    gas = (j.get_axis(4)*-1)+92
    brake = (j.get_axis(3)*21+207)/2
    throttle = int((gas+brake)/2)
    return steering,throttle


def constrain(ster_data):
    
    if(ster_data > 145):
        steering = 145
        return steering
    if(ster_data < 45):
        steering = 45
        return steering
    else:
        return ster_data


def serial_write(ster,vel):
    ser.write(chr(ster))
    ser.write(chr(vel))

if __name__ == '__main__': main() # モジュールを直接実行したら、main()を実行
# end of file