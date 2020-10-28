import pygame
import random
import math

BACK_ONE = [pygame.image.load('img/back/1.png'),
            pygame.image.load('img/back/2.png'),
            pygame.image.load('img/back/3.png')
            ]
stayRIGHT = [pygame.image.load('img/player/stay/right/1.png'),
             pygame.image.load('img/player/stay/right/2.png'),
             pygame.image.load('img/player/stay/right/3.png'),
             pygame.image.load('img/player/stay/right/4.png'),
             pygame.image.load('img/player/stay/right/5.png'),
             pygame.image.load('img/player/stay/right/6.png'),
             pygame.image.load('img/player/stay/right/7.png'),
             pygame.image.load('img/player/stay/right/8.png'),
             pygame.image.load('img/player/stay/right/9.png'),
             pygame.image.load('img/player/stay/right/10.png')
             ]
stayLEFT = [pygame.image.load('img/player/stay/left/1.png'),
            pygame.image.load('img/player/stay/left/2.png'),
            pygame.image.load('img/player/stay/left/3.png'),
            pygame.image.load('img/player/stay/left/4.png'),
            pygame.image.load('img/player/stay/left/5.png'),
            pygame.image.load('img/player/stay/left/6.png'),
            pygame.image.load('img/player/stay/left/7.png'),
            pygame.image.load('img/player/stay/left/8.png'),
            pygame.image.load('img/player/stay/left/9.png'),
            pygame.image.load('img/player/stay/left/10.png')
            ]
walkRIGHT = [pygame.image.load('img/player/walk/right/1.png'),
             pygame.image.load('img/player/walk/right/2.png'),
             pygame.image.load('img/player/walk/right/3.png'),
             pygame.image.load('img/player/walk/right/4.png'),
             pygame.image.load('img/player/walk/right/5.png'),
             pygame.image.load('img/player/walk/right/6.png'),
             pygame.image.load('img/player/walk/right/7.png'),
             pygame.image.load('img/player/walk/right/8.png'),
             pygame.image.load('img/player/walk/right/9.png'),
             pygame.image.load('img/player/walk/right/10.png')
             ]
walkLEFT = [pygame.image.load('img/player/walk/left/1.png'),
            pygame.image.load('img/player/walk/left/2.png'),
            pygame.image.load('img/player/walk/left/3.png'),
            pygame.image.load('img/player/walk/left/4.png'),
            pygame.image.load('img/player/walk/left/5.png'),
            pygame.image.load('img/player/walk/left/6.png'),
            pygame.image.load('img/player/walk/left/7.png'),
            pygame.image.load('img/player/walk/left/8.png'),
            pygame.image.load('img/player/walk/left/9.png'),
            pygame.image.load('img/player/walk/left/10.png')
            ]
jumpRIGHT = [pygame.image.load('img/player/jump/right/1.png'),
             pygame.image.load('img/player/jump/right/2.png'),
             pygame.image.load('img/player/jump/right/3.png'),
             pygame.image.load('img/player/jump/right/4.png'),
             pygame.image.load('img/player/jump/right/5.png'),
             pygame.image.load('img/player/jump/right/6.png'),
             pygame.image.load('img/player/jump/right/7.png'),
             pygame.image.load('img/player/jump/right/8.png'),
             pygame.image.load('img/player/jump/right/9.png'),
             pygame.image.load('img/player/jump/right/10.png')
             ]
jumpLEFT = [pygame.image.load('img/player/jump/left/1.png'),
            pygame.image.load('img/player/jump/left/2.png'),
            pygame.image.load('img/player/jump/left/3.png'),
            pygame.image.load('img/player/jump/left/4.png'),
            pygame.image.load('img/player/jump/left/5.png'),
            pygame.image.load('img/player/jump/left/6.png'),
            pygame.image.load('img/player/jump/left/7.png'),
            pygame.image.load('img/player/jump/left/8.png'),
            pygame.image.load('img/player/jump/left/9.png'),
            pygame.image.load('img/player/jump/left/10.png')
            ]
starSPRITE = [pygame.image.load('img/star/1.png'),
              pygame.image.load('img/star/2.png'),
              pygame.image.load('img/star/3.png'),
              pygame.image.load('img/star/4.png'),
              pygame.image.load('img/star/5.png'),
              pygame.image.load('img/star/6.png'),
              pygame.image.load('img/star/7.png'),
              pygame.image.load('img/star/8.png'),
              pygame.image.load('img/star/9.png'),
              pygame.image.load('img/star/10.png')
              ]
policeRIGHT = [pygame.image.load('img/police/right/1.png'),
               pygame.image.load('img/police/right/2.png'),
               pygame.image.load('img/police/right/3.png'),
               pygame.image.load('img/police/right/4.png'),
               pygame.image.load('img/police/right/5.png'),
               pygame.image.load('img/police/right/6.png'),
               pygame.image.load('img/police/right/7.png')
               ]
GameOver = pygame.image.load("img/GameOwer.png")
OverBack = pygame.image.load("img/back/bg.jpg")


class Police:
    inviz = True
    lifeCount = 0
    lifeRange = 0
    animCount = 0
    palit = False

    def __init__(self, SPRITE, X, Y, POSITION):
        self.Pos_x = X
        self.Pos_y = Y
        self.Position = POSITION
        self.SPRITE = SPRITE

    def inviz_out(self):
        if self.inviz:
            if self.animCount < 6:
                self.animCount += 0.5
            if self.Pos_y > 160:
                self.Pos_y -= 10
            elif self.Pos_y == 160:
                self.palit = True
                self.lifeRange = random.randint(40, 120)
                if self.lifeCount < self.lifeRange:
                    self.lifeCount += 1
                elif self.lifeCount == self.lifeRange:
                    self.inviz = False
                    self.lifeCount = 0
                    self.lifeRange = 0

    def inviz_in(self):
        if not self.inviz:
            if self.animCount > 0:
                self.animCount -= 0.5
            if self.Pos_y < 300:
                self.Pos_y += 10
            elif self.Pos_y == 300:
                self.palit = False
                self.lifeRange = random.randint(60, 140)
                if self.lifeCount < self.lifeRange:
                    self.lifeCount += 1
                elif self.lifeCount == self.lifeRange:
                    self.inviz = True
                    self.lifeCount = 0
                    self.lifeRange = 0

    def draw(self, screen):
        self.inviz_in()
        self.inviz_out()
        screen.blit(self.SPRITE[math.trunc(self.animCount)], (self.Pos_x, self.Pos_y))


class Star:
    Pos_x = 0
    Pos_y = 0
    animCount = 0
    moveCount = 20
    life = 0
    borntime = 0
    hiden = True

    def __init__(self):
        pass

    def born(self):
        self.borntime += 1
        if self.borntime == 120:
            self.Pos_x = random.randint(10, 1085)
            self.Pos_y = random.randint(290, 500)
            self.hiden = False
            self.life = 0

    def hide(self):
        self.life += 1
        if self.life == 240:
            self.hiden = True
            self.borntime = 0

    def move(self):
        if self.moveCount > -20:
            if self.moveCount > 0:
                self.Pos_y -= 1
            else:
                self.Pos_y += 1
            self.moveCount -= 1
        else:
            self.moveCount = 20

    def draw(self, screen):
        if self.hiden:
            self.born()
        self.move()
        self.hide()
        if not self.hiden:
            screen.blit(starSPRITE[self.animCount // 4], (self.Pos_x, self.Pos_y))
            self.animCount += 1
            if self.animCount + 1 == 40:
                self.animCount = 0


class Player:
    Pos_x = 550
    Pos_y = 350
    speed = 10
    right = True
    left = False
    stay = True
    animCount = 0
    isJump = False
    jumpCount = 10
    palevo = False

    def __init__(self):
        pass

    def collect(self, STAR):
        Radius = 100
        if (STAR.Pos_x - self.Pos_x) ** 2 + (STAR.Pos_y - self.Pos_y) ** 2 <= Radius * Radius:
            self.palevo = True
            STAR.hiden = True

    def walk(self, key):
        if key[pygame.K_a] and self.Pos_x > 5:
            self.right = False
            self.left = True
            self.stay = False
            self.Pos_x -= self.speed
        if key[pygame.K_d] and self.Pos_x < 1095:
            self.right = True
            self.left = False
            self.stay = False
            self.Pos_x += self.speed
        if key[pygame.K_SPACE]:
            self.animCount = 0
            self.isJump = True
        if not self.isJump:
            if key[pygame.K_w] and self.Pos_y > 270:
                self.stay = False
                self.Pos_y -= self.speed
            if key[pygame.K_s] and self.Pos_y < 484:
                self.stay = False
                self.Pos_y += self.speed

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                if self.jumpCount > 0:
                    self.Pos_y -= (self.jumpCount ** 2) / 4
                    self.animCount += 1
                elif self.jumpCount < 0:
                    self.Pos_y += (self.jumpCount ** 2) / 4
                    self.animCount += 1
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

    def move(self, keys):
        lastPos_x = self.Pos_x
        lastPos_y = self.Pos_y
        self.walk(keys)
        self.jump()
        if (lastPos_x == self.Pos_x) and (lastPos_y == self.Pos_y):
            player.stay = True

    def draw(self, screen):
        if not self.isJump:
            if self.stay:
                if self.right:
                    screen.blit(stayRIGHT[self.animCount // 2], (self.Pos_x, self.Pos_y))
                    self.animCount += 1
                elif self.left:
                    screen.blit(stayLEFT[self.animCount // 2], (self.Pos_x, self.Pos_y))
                    self.animCount += 1
            else:
                if self.right:
                    screen.blit(walkRIGHT[self.animCount // 2], (self.Pos_x, self.Pos_y))
                    self.animCount += 1
                elif self.left:
                    screen.blit(walkLEFT[self.animCount // 2], (self.Pos_x, self.Pos_y))
                    self.animCount += 1
        else:
            if self.right:
                screen.blit(jumpRIGHT[self.animCount // 2], (self.Pos_x, self.Pos_y))

            elif self.left:
                screen.blit(jumpLEFT[self.animCount // 2], (self.Pos_x, self.Pos_y))

        if self.animCount + 1 == 20:
            self.animCount = 0


class Level:
    Over = False
    animCount = 0

    def __init__(self, LIST, PLAYER, STAR, POLICE_ONE):
        self.BackGroundImage1 = LIST[0]
        self.BackGroundImage2 = LIST[1]
        self.BackGroundImage3 = LIST[2]
        self.PLAYER = PLAYER
        self.STAR = STAR
        self.POLICE_ONE = POLICE_ONE

    def draw(self, screen):
        if not self.Over:
            screen.blit(self.BackGroundImage1, (0, 0))
            self.POLICE_ONE.draw(screen)
            screen.blit(self.BackGroundImage2, (0, 0))
            self.STAR.draw(screen)
            self.PLAYER.draw(screen)
            screen.blit(self.BackGroundImage3, (0, 0))
        else:
            screen.blit(OverBack, (0, 0))
            screen.blit(stayRIGHT[self.animCount // 4], (550, 350))
            screen.blit(GameOver, (185, 90))
            self.animCount += 1
            if self.animCount + 1 == 40:
                self.animCount = 0



class DrawWindow:
    WIDTH = 0
    HEIGHT = 0
    FPS = 0

    def __init__(self, W, H, F):
        self.WIDTH = W
        self.HEIGHT = H
        self.FPS = F

    def draw(self, lvl):
        pygame.init()
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Game")
        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(self.FPS)
            events = pygame.event.get()
            keys = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pressed()

            if mouse[2]:
                lvl.PLAYER.collect(lvl.STAR)
            if lvl.PLAYER.palevo and lvl.POLICE_ONE.palit:
                lvl.Over = True
            if lvl.STAR.hiden:
                lvl.PLAYER.palevo = False

            lvl.PLAYER.move(keys)
            lvl.draw(screen)

            for event in events:
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()

        pygame.quit()


Game = DrawWindow(1200, 630, 240)
police_one = Police(policeRIGHT, 1050, 300, "right")
player = Player()
star = Star()
lvl1 = Level(BACK_ONE, player, star, police_one)
Game.draw(lvl1)
