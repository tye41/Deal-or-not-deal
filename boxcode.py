# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:58:41 2020

@author: Ryan
"""
import pygame
class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('close.png')
        self.openimage=pygame.image.load('open.png')
        self.active=True
        self.money=0
        self.pos=pygame.Rect(0,0,0,0)
        self.special=False
        
    