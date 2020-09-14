# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:05:26 2020

@author: Ryan
"""

import random as r
import pygame
import boxcode

pygame.init()


bg_size= width,height= 900,600
screen=pygame.display.set_mode(bg_size)
pygame.display.set_caption('Deal or not deal?')

Red=(255,0,0)
White=(255,255,255)
Black=(0,0,0)
acc=pygame.image.load('accept.png')
den=pygame.image.load('deny.png')


numarray=[0.01,0.2,0.5,1,2,5,10,20,50,100,200,500,1000,2500,5000,7500,10000,25000,
               50000,100000,200000,300000,400000,500000,1000000,5000000]
r.shuffle(numarray)
openbox=0
openboxlist=[6,10,13,16,18,20,21,22,23,24]
duplist=[6,10,13,16,18,20,21,22,23,24]
boxall=pygame.sprite.Group()
for i in range(26):
    temp=boxcode.Box()
    temp.money=numarray[i]
    boxall.add(temp)


score_font=pygame.font.Font('font.ttf',16)
deal_font=pygame.font.Font('font.ttf',36)
ans_font= pygame.font.SysFont('Optima',36)
string_font=pygame.font.Font('font.ttf',20)
running=True
flag=0
while running:
    screen.fill((129,216,209))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN :
            for each in boxall:
                if event.button==1 and each.pos.collidepoint(event.pos) and not each.special and openbox<24:
                    if openbox==0:
                        each.special=True
                        openbox+=1
                    else:
                        each.active=False
                        try:
                            numarray.remove(each.money)
                            openbox+=1
                        except:
                            pass
                    
            if event.button==1 and pygame.Rect(700,500,64,64).collidepoint(event.pos):
                for each in boxall:
                    if each.special:
                        request=ans_font.render('You accept bankdeal:$%s. Your box contains:$%s'%(str(store),str(each.money)),True, White)
                        screen.blit(request,(100,500))
                        temp=ans_font.render('Game over!',True, White)
                        screen.blit(temp,(300,450))
                        pygame.image.save(screen,"screenshot.jpg")
                        running=False
            
            if event.button==1 and pygame.Rect(800,500,64,64).collidepoint(event.pos):
                for each in boxall:
                    if each.special:
                        request=ans_font.render('You reject bankdeal:$%s. You gain $%s.'%(str(store),str(each.money)),True, White)
                        screen.blit(request,(100,500))
                        temp=ans_font.render('Game over!',True, White)
                        screen.blit(temp,(350,450))
                        pygame.image.save(screen,"screenshot.jpg")
                        running=False
                
    if openbox in openboxlist:
        openboxlist.remove(openbox)
        flag=1
    else:
        flag=0                 
    x,y=20,20
    for each in boxall:
        if x<800:
            if each.active:
                screen.blit(each.image,(x,y))
                if each.special:
                    score_text=string_font.render('chosen one' ,True,Red)
                    screen.blit(score_text,(x-10,y+65))
            else:
                screen.blit(each.openimage,(x,y))
                score_text=score_font.render('%s' %str(each.money),True,Black)
                screen.blit(score_text,(x,y+65))
        else:
            x=20
            y+=100
            if each.active:
                screen.blit(each.image,(x,y))
                if each.special:
                    score_text=score_font.render('chosen one' ,True,Red)
                    screen.blit(score_text,(x,y+65))
            else:
                screen.blit(each.openimage,(x,y))
                score_text=score_font.render('%s' %str(each.money),True,Black)
                screen.blit(score_text,(x,y+65))
        each.pos=pygame.Rect(x,y,64,64)
        x+=100
    
    if running:
        if openbox==1:
            store=40000
            score_text=deal_font.render('Bankdeal:$%s' %str(50000),True,Red)
            screen.blit(score_text,(300,500))
            screen.blit(acc,(700,500))
        if flag:
            bankmoney=sum(numarray)/len(numarray)
            if openbox==6 or openbox==10:
                store=int(bankmoney*r.uniform(0.2,0.4))
            if openbox==13 or openbox==16 or openbox==18:
                store=int(bankmoney*r.uniform(0.4,0.6))
            if openbox==20 or openbox==21:
                if bankmoney<40000:
                    store=int(bankmoney*r.uniform(0.9,1.2))
                else:
                    store=int(bankmoney*r.uniform(0.7,0.9))
            if openbox==22 or openbox==23 or openbox==24:
                if bankmoney<20000:
                    store=int(bankmoney*r.uniform(1.1,1.3))
                elif bankmoney>100000:
                    store=int(bankmoney*r.uniform(0.7,0.9))
                else:
                    store=int(bankmoney)
        else:
            if openbox in duplist:
                score_text=deal_font.render('Bankdeal:$%s' %str(store),True,Red)
                screen.blit(score_text,(300,500))
                screen.blit(acc,(700,500))
                if openbox==24:
                    screen.blit(den,(800,500))
            
            arraystring=''
            duparray=numarray[:]
            duparray.sort(reverse=True)
            for each in duparray:
                if each>=50000:
                    arraystring+=str(each)
                    arraystring+='/'
            arraystring=string_font.render('Possible grand:%s'%arraystring,True,Black)
            screen.blit(arraystring,(10,450))
        
        
    pygame.display.update()
    
openwin=True
shot=pygame.image.load("screenshot.jpg")
while openwin:
    screen.blit(shot,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
             if event.button==1:
                 pygame.quit()
                 exit()
    
    
    
    



    
  


