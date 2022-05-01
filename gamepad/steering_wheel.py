#! /usr/bin/env python
# coding: utf-8
# coding=utf-8
# -*- coding: utf-8 -*-


import pygame,serial,sys
from pygame.locals import *

ser = serial.Serial("/dev/ttyUSB0",115200,timeout=1)

pygame.joystick.init()


try:# ��O�����邩������Ȃ����A���s����������
    j = pygame.joystick.Joystick(0) # create a joystick instance
    j.init() # init instance
    print ("Joystick name: ") + j.get_name()
    print ("Number of buttons: ") + str(j.get_numbuttons())
except pygame.error:# ��O���̏���
    print ('Joystick is not found')
    pygame.quit()
    sys.exit()


def main():
    pygame.init()

    while 1: # �A���[�v
        for e in pygame.event.get(): # �C�x���g�`�F�b�N
            # if e.type == JOYHATMOTION: # �I���������ꂽ�H
            #     pygame.quit()
            #     sys.exit()
            #if (e.type == KEYDOWN):
            #    if (e.key  == K_ESCAPE): # ESC�������ꂽ�H
            #        pygame.quit()
            if e.type == pygame.locals.JOYAXISMOTION: # 7 �Q�[���p�b�h�̃{�^���C�x���g
                gamepad_event()


def gamepad_event():
    
    Senddata = joyget()
    for i in range(2):
        low = Senddata[i]&31
        high = (Senddata[i]>>5)&31
        head = ((Senddata[i]>>10)&31)+128+i
        ser.write(chr(head))
        ser.write(chr(high))
        ser.write(chr(low))

    

def joyget():    
 # Joystick�֘A�̃C�x���g�`�F�b�N
    input_array = []
    input_array = getUserInput(j.get_axis(0),j.get_axis(1),j.get_axis(2))
    # steering��throttle�̖߂�l�𓾂�

    steering = constrain(input_array[0])
    throttle = input_array[1]
    # �߂�l��z��ɑ��

    sys.stdout.write('\r'+'steering: '+str(steering)+' '+'throttle: '+''+str(throttle))
    sys.stdout.flush()

    # print ('steering ' + str(steering))
    # print 'gas and brake ' + str(gas) +' , '+ str(brake)
    # print ('throttle ' + str(throttle))

    return steering,throttle


def getUserInput(ster_ax,gas_ax,brake_ax):
    
    steering = int(((j.get_axis(0)*180)+180)/2)
    gas = (j.get_axis(1))+93
    brake = (j.get_axis(2)*-1*21+207)/2
    throttle = int((gas+brake)/2)
    return steering,throttle


def constrain(ster_data):

    if(ster_data > 180):
        steering = 180
        return steering
    if(ster_data < 0):
        steering = 0
        return steering
    else:
        return ster_data


# def serial_write(ster,vel):

#     ser.write(chr(ster))
#     ser.write(chr(vel))

if __name__ == '__main__': main() # ���W���[���𒼐ڎ��s������Amain()�����s
# end of file