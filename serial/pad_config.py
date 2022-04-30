#! /usr/bin/env python
# coding: utf-8
# coding=utf-8
# -*- coding: utf-8 -*-

import pygame,sys
from pygame.locals import *

pygame.joystick.init()


try:
    j = pygame.joystick.Joystick(0) # create a joystick instance
    j.init() # init instance
    print ('Joystick Name:' + j.get_name())
    print ('button : ' + str(j.get_numbuttons()))
    print ('axis : ' + str(j.get_numaxes()))
    print ('ball : ' + str(j.get_numballs()))
except pygame.error:
    print ('Joystick is not found.')
    pygame.quit()
    sys.exit()



def main():
    pygame.init()

    while 1:
        for e in pygame.event.get(): # イベントチェック
            # if e.type == JOYHATMOTION: # 終了が押された？
            #     pygame.quit()
            #     sys.exit()
            if (e.type == KEYDOWN and
                e.key  == K_ESCAPE): # ESCが押された？
                pygame.quit()
            # Joystick関連のイベントチェック
            if e.type == pygame.locals.JOYAXISMOTION: # 7
                joyget()


def joyget():

    steering = j.get_axis(0)
    gas = j.get_axis(2) # 1, gt force pro 5, dualshock 3
    brake = j.get_axis(3)

    steering = int(((j.get_axis(0)*-1*180)+180)/2)
    gas = int(j.get_axis(2))+93
    brake = int((j.get_axis(3)*21+207)/2)

    sys.stdout.write('\r'+'steering: '+str(steering)+'  '+'gas: '+str(gas)+'  '+'brake: '+str(brake))
    sys.stdout.flush()
    # print('\r' + 'steering: '+str(steering)+' '+'gas: '+''+str(gas)+' '+'brake: '+''+str(brake))


if __name__ == '__main__': main()
# end of file