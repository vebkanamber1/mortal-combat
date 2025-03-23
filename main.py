
import pygame
import os
import sys
import random

pygame.init()
from past.translation import transform

WIDTH= 1400
HEIGHT = 600
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
lvl ='menu'
clock = pygame.time.Clock()
font = pygame.font.SysFont('Aria', 40 )
from load import *



def startMenu():
    sc.fill('grey')
    button_group.draw(sc)
    button_group.update()
    pygame.display.update()





class Button(pygame.sprite.Sprite):
    def __init__(self, image, pos,nex_lvl,  text):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.text = text

        self.next_lvl = nex_lvl
    def update(self):
        global lvl

        text_render = font.render(self.text, True, 'white')
        sc.blit(text_render, (self.rect.x + 80, self.rect.y +5))

        click = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.rect.left < click[0]< self.rect.right and self.rect.top < click[1]< self.rect.bottom:
                lvl = self.next_lvl

            if lvl =='game':
                restart()
            if lvl == 'end':
                exit()





# class Player_1(pygame.sprite.Sprite):
#     def __init__(self, image_lists):
#         pygame.sprite.Sprite.__init__(self)
#         self.image_lists = image_lists
#         self.image = self.image_lists['idle'][0]
#         self.current_list_image = self.image_lists['idle']
#         self.rect = self.image.get_rect()
#         self.anime_idle = True
#         self.anime_run = False
#         self.anime_atk = False
#         self.frame = 0
#         self.timer_anime =0
#         self.dir = 'right'
#         self.hp = 100
#         self.jump_step = -20
#         self.jump = False
#         self.flag_damage = False
#         self.mask = pygame.mask.from_surface(self.image)
#         self.mask_outline = self.mask.outline()
#         self.mask_list = []
#         self.rect.center= (500,380)
#         self.hp_bar ='blue'
#         self.key = pygame.key.get_pressed()
#         self.mask = pygame.mask.from_surface(self.image)
#         self.mask_outline =self.mask.outline()
#
#
#
#
#
#
#
#     def update(self):
#         if self.rect.center[0] - player_2.rect.center[0]<0:
#             self.dir = 'right'
#         else:
#             self.dir ='left'
#         self.key = pygame. key.get_pressed()
#         self.move()
#         self.animation()
#         self.attack()
#         self.jumps()
#         self.draw_hp_bar()
#         # if pygame.sprite.spritecollide(self, player_2_group, False):
#         #     player_2.hp -= 0.05
#         if self.anime_atk and self.flag_damage:
#             if len(set(self.mask_list) & set(player_2.mask_list)) >0:
#                 player_2.hp -= 14
#                 self.flag_damage = False
#
#
#         # if pygame.sprite.spritecollide(self, )
#         self.mask = pygame.mask.from_surface(self.image)
#         self.mask_outline = self.mask.outline()
#         self.mask_list = []
#         for i in self.mask_outline:
#             self.mask_list.append((i[0] + self.rect.x, i[1] + self.rect.y))
#         for point in self.mask_list:
#             x = point[0]
#             y = point[1]
#
#
#
#
#     def move(self):
#         if self.key[pygame.K_d]:
#             self.rect.x +=2
#             self.anime_idle = False
#             if not self.anime_atk:
#                 self.anime_run =True
#         elif self.key[pygame.K_a]:
#             self.rect.x -= 2
#             self.anime_idle = False
#             if not self.anime_atk:
#                 self.anime_run = True
#
#         else:
#             if not self.anime_atk:
#                 self.anime_idle = True
#             self.anime_run = False
#
#     def jumps(self):
#         if self.key[pygame.K_SPACE]:
#             self.jump =True
#         if self.jump:
#             if self.jump_step <=20:
#                 self.rect.y += self.jump_step
#                 self.jump_step += 1
#             else:
#                 self.jump = False
#                 self.jump_step = -20
#
#     def attack(self):
#         if self.key[pygame.K_e] and not self.anime_atk:
#             self.frame = 0
#             self.anime_atk = True
#             self.anime_idle = False
#             self.anime_run = False
#             self.flag_damage = True
#
#
#
#
#     def animation(self):
#         self.timer_anime += 2
#         if self.timer_anime /FPS > 0.1:
#             if self.frame == len(self.current_list_image) - 1:
#                 self.frame = 0
#                 if self.anime_atk:
#                     self.current_list_image = player_1_idle_image
#                     self.anime_atk = False
#                     self.anime_idle = True
#             else:
#                 self.frame += 1
#             self.timer_anime = 0
#         if self.anime_idle:
#             self.current_list_image = self.image_lists['idle']
#         elif self.anime_run:
#             self.current_list_image = self.image_lists['run']
#         elif self.anime_atk:
#             self.current_list_image = self.image_lists['atk']
#         try:
#             if self. dir == 'right':
#                 self.image = self.current_list_image[self.frame]
#             else:
#                 self.image = pygame.transform.flip(self.current_list_image[self.frame], True, False)
#         except:
#             self.frame = 0
#
#
#     def draw_hp_bar(self):
#         pygame.draw.rect(sc, self.hp_bar, (0,0, 600 * self.hp / 83,50))







class Player_2(pygame.sprite.Sprite):
    def __init__(self, image_lists):
        pygame.sprite.Sprite.__init__(self)
        self.image_lists = image_lists
        self.image = self.image_lists['idle'][0]
        self.current_list_image = self.image_lists['idle']
        self.rect = self.image.get_rect()
        self.anime_idle = True
        self.anime_run = False
        self.anime_atk = False
        self.frame = 0
        self.timer_anime =0
        self.dir = 'left'
        self.hp = 100
        self.jump_step = -20
        self.jump = False
        self.flag_damage = False
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []
        self.rect.center= (900,380)
        self.hp_bar ='red'
        self.key = pygame.key.get_pressed()
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.timer_attack = 0

    def update(self):
        if self.rect.center[0] - aizen.rect.center[0]<0:
            self.dir = 'left'
        else:
            self.dir ='right'
        self.key = pygame. key.get_pressed()
        self.move()
        self.animation()
        self.attack()
        self.jumps()
        self.draw_hp_bar()
        # if pygame.sprite.spritecollide(self, player_1_group, False):
        #     player_1.hp -= 0.05
        if self.anime_atk and self.flag_damage:
            if len(set(self.mask_list) & set(aizen.mask_list)) >0:
                aizen.hp -= 22
                self.flag_damage = False




        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []
        for i in self.mask_outline:
            self.mask_list.append((i[0] + self.rect.x, i[1] + self.rect.y))
        for point in self.mask_list:
            x = point[0]
            y = point[1]
            # pygame.draw.circle(sc, 'red', (x, y), 3)





    def move(self):
        if self.key[pygame.K_h]:
            self.rect.x -=2
            self.anime_idle = False
            if not self.anime_atk:
                self.anime_run =True
        elif self.key[pygame.K_k]:
            self.rect.x += 2
            self.anime_idle = False
            if not self.anime_atk:
                self.anime_run = True

        else:
            if not self.anime_atk:
                self.anime_idle = True
            self.anime_run = False

    def jumps(self):
        if self.key[pygame.K_u]:
            self.jump =True
        if self.jump:
            if self.jump_step <=20:
                self.rect.y += self.jump_step
                self.jump_step += 1
            else:
                self.jump = False
                self.jump_step = -20

    def attack(self):
        if self.key[pygame.K_i] and not self.anime_atk:
            self.frame = 0
            self.anime_atk = True
            self.anime_idle = False
            self.anime_run = False
            self.flag_damage = True


    def animation(self):
        self.timer_anime += 2
        if self.timer_anime /FPS > 0.1:
            if self.frame == len(self.current_list_image) - 1:
                self.frame = 0
                if self.anime_atk:
                    self.current_list_image = player_1_idle_image
                    self.anime_atk = False
                    self.anime_idle = True
            else:
                self.frame += 1
            self.timer_anime = 0
        if self.anime_idle:
            self.current_list_image = self.image_lists['idle']
        elif self.anime_run:
            self.current_list_image = self.image_lists['run']
        elif self.anime_atk:
            self.current_list_image = self.image_lists['atk']
        try:
            if self. dir == 'left':
                self.image = self.current_list_image[self.frame]
            else:
                self.image = pygame.transform.flip(self.current_list_image[self.frame], True, False)
        except:
            self.frame = 0

    def draw_hp_bar(self):

        pygame.draw.rect(sc, self.hp_bar, (700, 0, 600 * self.hp / 70, 50))



class Aizen(pygame.sprite.Sprite):
    def __init__(self, image_lists):
        pygame.sprite.Sprite.__init__(self)
        self.image_lists = image_lists
        self.image = self.image_lists['idle'][0]
        self.current_list_image = self.image_lists['idle']
        self.rect = self.image.get_rect()
        self.anime_idle = True
        self.anime_run = False
        self.anime_atk = False
        self.anime_atk2 = False
        self.frame = 0
        self.timer_anime =0
        self.dir = 'right'
        self.hp = 100
        self.jump_step = -20
        self.jump = False
        self.flag_damage = False
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []
        self.rect.center= (500,380)
        self.hp_bar ='purple'
        self.key = pygame.key.get_pressed()
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline =self.mask.outline()









    def update(self):
        if self.rect.center[0] - player_2.rect.center[0]<0:
            self.dir = 'right'
        else:
            self.dir ='left'
        self.key = pygame. key.get_pressed()
        self.move()
        self.animation()
        self.attack()
        self.jumps()
        self.draw_hp_bar()
        self.attack2()

        if self.anime_atk and self.flag_damage:
            if len(set(self.mask_list) & set(player_2.mask_list)) >0:
                player_2.hp -= 10
                self.flag_damage = False

        if self.anime_atk2 and self.flag_damage:
            if len(set(self.mask_list) & set(player_2.mask_list)) >0:
                player_2.hp -= 20
                self.flag_damage = False



        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []
        for i in self.mask_outline:
            self.mask_list.append((i[0] + self.rect.x, i[1] + self.rect.y))
        for point in self.mask_list:
            x = point[0]
            y = point[1]




    def move(self):
        if self.key[pygame.K_d]:
            self.rect.x +=2
            self.anime_idle = False
            if not self.anime_atk:
                self.anime_run =True
        elif self.key[pygame.K_a]:
            self.rect.x -= 2
            self.anime_idle = False
            if not self.anime_atk:
                self.anime_run = True

        else:
            if not self.anime_atk and not self.anime_atk2:
                self.anime_idle = True
            self.anime_run = False

    def jumps(self):
        if self.key[pygame.K_SPACE]:
            self.jump =True
        if self.jump:
            if self.jump_step <=20:
                self.rect.y += self.jump_step
                self.jump_step += 1
            else:
                self.jump = False
                self.jump_step = -20

    def attack(self):
        if self.key[pygame.K_e] and not self.anime_atk:
            self.frame = 0
            self.anime_atk = True
            self.anime_atk2 = False
            self.anime_idle = False
            self.anime_run = False
            self.flag_damage = True

    def attack2(self):
        if self.key[pygame.K_q]  and not self.anime_atk2:
            self.frame = 0
            self.anime_atk = False
            self.anime_atk2 = True
            self.anime_idle = False
            self.anime_run = False
            self.flag_damage = True




    def animation(self):
        self.timer_anime += 2
        if self.timer_anime /FPS > 0.1:
            if self.frame == len(self.current_list_image) - 1:
                self.frame = 0
                if self.anime_atk or self.anime_atk2:
                    self.current_list_image = player_1_idle_image
                    self.anime_atk = False
                    self.anime_atk2 = False
                    self.anime_idle = True
            else:
                self.frame += 1
            self.timer_anime = 0
        if self.anime_idle:
            self.current_list_image = self.image_lists['idle']
        elif self.anime_run:
            self.current_list_image = self.image_lists['run']
        elif self.anime_atk:
            self.current_list_image = self.image_lists['atk']
        elif self.anime_atk2:
            self.current_list_image = self.image_lists['atk2']
        try:
            if self. dir == 'right':
                self.image = self.current_list_image[self.frame]
            else:
                self.image = pygame.transform.flip(self.current_list_image[self.frame], True, False)
        except:
            self.frame = 0


    def draw_hp_bar(self):
        pygame.draw.rect(sc, self.hp_bar, (0,0, 600 * self.hp / 83,50))



class FON:
    def __init__(self):
        self.timer = 0
        self.frame = 0
        self.image = fon_image


    def update(self):
        self.timer +=2
        sc.blit(self.image[self.frame], (0,0))
        if self.timer /FPS >0.1:
            if self.frame == len(self.image) - 1:
                self.frame = 0
            else:
                self.frame += 1
            self.timer = 0



def restart():
    global fon,player_1_group, player_2_group, player_1,player_2,button_group,aizen,aizen_group
    fon = FON()
    player_1_group = pygame.sprite.Group()
    player_2_group = pygame.sprite.Group()
    # player_1 = Player_1 ({'idle':player_1_idle_image, 'run':player_1_run_image, 'atk':player_1_attack_image})
    # player_1_group.add(player_1)
    player_2 = Player_2({'idle': player_2_idle_image, 'run': player_2_run_image, 'atk': player_2_attack_image})
    player_2_group.add(player_2)
    aizen = Aizen({'idle': aizen_idle_image, 'run': aizen_run_image, 'atk2': aizen_attack2_image, 'atk': aizen_attack_image})
    aizen_group= pygame.sprite.Group()
    aizen_group.add(aizen)
    button_group = pygame.sprite.Group()





def game():
    sc.fill('grey')
    fon.update()

    player_1_group.update()
    player_1_group.draw(sc)
    aizen_group.update()
    aizen_group.draw(sc)
    player_2_group.update()
    player_2_group.draw(sc)
    pygame.display.update()

restart()

button_start = Button(button_image, (600, 100), 'game', 'start')
button_group.add(button_start)

button_exit =Button(button_image, (600,180), 'end', 'exit')
button_group.add(button_exit)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if lvl =='game':
        game()
    elif lvl == 'menu':
        startMenu()
    elif lvl == 'exit':
        pygame.quit()
        sys.exit()



    clock.tick(FPS)
