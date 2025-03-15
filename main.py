
import pygame
import os
import sys
import random
WIDTH= 1400
HEIGHT = 600
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
from load import *


class Player_1(pygame.sprite.Sprite):
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
        self.dir = 'right'
        self.hp = 100
        self.jump_step = -20
        self.jump = False
        self.flag_damage = False
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []
        self.rect.center= (200,380)
        self.hp_bar ='blue'
        self.key = pygame.key.get_pressed()

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
            if not self.anime_atk:
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
            if self. dir == 'right':
                self.image = self.current_list_image[self.frame]
            else:
                self.image = pygame.transform.flip(self.current_list_image[self.frame], True, False)
        except:
            self.frame = 0


    def draw_hp_bar(self):
        pygame.draw.rect(sc, self.hp_bar, (0,0, 600 * self.hp / 100,50))




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
        self.rect.center= (400,380)
        self.hp_bar ='red'
        self.key = pygame.key.get_pressed()

    def update(self):
        if self.rect.center[0] - player_1.rect.center[0]<0:
            self.dir = 'left'
        else:
            self.dir ='right'
        self.key = pygame. key.get_pressed()
        self.move()
        self.animation()
        self.attack()
        self.jumps()
        self.draw_hp_bar()


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
        pygame.draw.rect(sc, self.hp_bar, (0, 0, 600 * self.hp / 200, 50))



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
    global fon,player_1_group, player_2_group, player_1,player_2
    fon = FON()
    player_1_group = pygame.sprite.Group()
    player_2_group = pygame.sprite.Group()
    player_1 = Player_1 ({'idle':player_1_idle_image, 'run':player_1_run_image, 'atk':player_1_attack_image})
    player_1_group.add(player_1)
    player_2 = Player_2({'idle': player_2_idle_image, 'run': player_2_run_image, 'atk': player_2_attack_image})
    player_2_group.add(player_2)





def game():
    sc.fill('grey')
    fon.update()

    player_1_group.update()
    player_1_group.draw(sc)
    player_2_group.update()
    player_2_group.draw(sc)
    pygame.display.update()
    # player_1.update()
    # player_1.draw(sc)
    # player_2.update()
    # player_2.draw(sc)

restart()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game()


    clock.tick(FPS)
