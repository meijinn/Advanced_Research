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
    print "Joystick�̖���:" + j.get_name()
    print "�{�^���� : " + str(j.get_numbuttons())
    print "���o�[�� : " + str(j.get_numaxes())
    print "�{�[���� : " + str(j.get_numballs())
except pygame.error:
    print 'Joystick��������܂���ł����B'
    pygame.quit()
    sys.exit()



def main():
    pygame.init()

    while 1:
        for e in pygame.event.get(): # �C�x���g�`�F�b�N
            if e.type == JOYHATMOTION: # �I���������ꂽ�H
                pygame.quit()
                sys.exit()
            if (e.type == KEYDOWN and
                e.key  == K_ESCAPE): # ESC�������ꂽ�H
                pygame.quit()
            # Joystick�֘A�̃C�x���g�`�F�b�N
            if e.type == pygame.locals.JOYAXISMOTION: # 7
                joyget()


            #    x , y = j.get_axis(4), j.get_axis(5)
            #    print 'x and y : ' + str(x) +' , '+ str(y)
            #elif e.type == pygame.locals.JOYBALLMOTION: # 8
            #    print 'ball motion'
            #elif e.type == pygame.locals.JOYHATMOTION: # 9
            #    print 'hat motion'
            #elif e.type == pygame.locals.JOYBUTTONDOWN: # 10
            #    print str(e.button)+'�Ԗڂ̃{�^���������ꂽ'
            #elif e.type == pygame.locals.JOYBUTTONUP: # 11
            #    print str(e.button)+'�Ԗڂ̃{�^���������ꂽ'


def joyget():
# Joystick�֘A�̃C�x���g�`�F�b�N
    input_array = []
    input_array = getUserInput(j.get_axis(0),j.get_axis(1),j.get_axis(2))
# steering��throttle�̖߂�l�𓾂�

    steering = constrain(input_array[0])
    throttle = input_array[1]

    sys.stdout.write("steering: \033[2K\033[G%s" % 'steering: '+str(steering)+' '+'throttle: '+''+str(throttle))
    sys.stdout.flush()

def getUserInput(ster_ax,gas_ax,brake_ax):

    steering = int(((j.get_axis(0)*180)+180)/2)
    gas = (j.get_axis(1))+93
    brake = (j.get_axis(2)*-1*21+207)/2
    throttle = int((gas+brake)/2)
    return steering, throttle


def constrain(ster_data):

    if(ster_data > 145):
        steering = 145
        return steering
    if(ster_data < 45):
        steering = 45
        return steering
    else:
        return ster_data


if __name__ == '__main__': main()
# end of file