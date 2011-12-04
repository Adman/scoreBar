import pygame, random, os, sys
from datetime import time
from pygame.locals import *
from pygame.colordict import THECOLORS





pygame.init()
info = pygame.display.Info()
desktop_size = (info.current_w, info.current_h)

scrsize = width,height = 600,400
#os.environ['SDL_VIDEO_WINDOW_POS'] = '10, 25'
os.environ['SDL_VIDEO_CENTERED'] = '1'

fullscreen = False
#self.fullscreen = not self.fullscreen


resolution = pygame.display.list_modes()[0]
video_flags = (not fullscreen and RESIZABLE)
screen = pygame.display.set_mode(resolution, video_flags)

class Computer():
    def __init__(self, screen):
        self.skoreH = 0
        self.skoreR = 0
        self.screen = screen

        self.w = 643
        self.h = 126
        self.surface = pygame.Surface((self.w, self.h))
        self.surface.fill((0,0,0))
        time = pygame.time.Clock()

        font_path = "digital-7.ttf"

        fontSize = 180
        fontSizeClock = 150
        # initialize font

        self.reportFont = pygame.font.SysFont("Courier", fontSize, True, False)
        self.reportFont2 = pygame.font.Font(font_path, fontSizeClock)

        self.on = False #wheter the stopwatch is running or not
        self.a = 0 # milliseconds from start
        start_tick = 0

        
    def run(self):
        done = False
        while not done:
            self.screen.fill((0,0,0))
            self.surface.fill((0,0,0))

            mods = pygame.key.get_mods()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type== VIDEORESIZE:
                    ss = [event.w,event.h]
                    self.screen=pygame.display.set_mode((ss),pygame.RESIZABLE)
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.skoreR += 1
                        self.on = False
                    elif event.key == K_w:
                        self.skoreH += 1
                        self.on = False
                    elif event.key == K_DOWN:
                        self.skoreR -= 1
                    elif event.key == K_s:
                        self.skoreH -= 1

                    if event.key == K_r:
                        self.a = 0
                        self.on = False

                    if mods & KMOD_SHIFT and event.key == K_r:
                        self.skoreH = 0
                        self.skoreR = 0
                        
                    
                    if event.key == K_SPACE:
                        if not self.on:
                            # starting the timer, so set the tick count reference to the current tick count
                            # plus the last tick count
                            start_tick = pygame.time.get_ticks() - self.a

                        # swap value
                        self.on = not self.on

            if self.on:
                # get the amount of ticks(milliseconds) that passed from the start
                self.a = (pygame.time.get_ticks() - start_tick)

            t = time((self.a / 1000) / 3600, ((self.a / 1000) / 60 % 60), (self.a / 1000) % 60)
            h_o_s = str(self.a)[-3:][:2] # hundredth of a second
            t_string = ','.join((t.strftime("%H:%M:%S"), h_o_s))
            tempsurface = self.reportFont2.render(t_string, True, THECOLORS["white"])

            self.print_time(tempsurface)
            self.print_skore(self.skoreH, self.skoreR)

            pygame.display.flip()
            pygame.time.wait(100)
            
            


    def print_skore(self, skoreH, skoreR):
        #texts
        robotText = 'Robot'
        humanText = 'Human'
        skoreHuman = '%d' % skoreH
        skoreRobot = '%d' % skoreR
        dvojbText = ':'

        # render text to font
        skoreHBlit = self.reportFont.render(skoreHuman, True, (255, 255, 255))
        skoreRBlit = self.reportFont.render(skoreRobot, True, (255, 255, 255))
        humanBlit = self.reportFont.render(humanText, True, (255, 255, 255))
        robotBlit = self.reportFont.render(robotText, True, (255, 255, 255))
        dvojbBlit = self.reportFont.render(dvojbText, True, (255, 255, 255))

        widthH = humanBlit.get_width() / 2
        widthR = robotBlit.get_width() / 2 
        
        # get size of screen
        wherex = self.screen.get_size()[0]
        wherey = self.screen.get_size()[1]
        
        #rozdelit na polky
        rozdelx = wherex / 2
        rozdely = wherey / 2

        # blits titles
        self.screen.blit(humanBlit, (rozdelx - (rozdelx / 2) - widthH, wherey / 10 - 30))
        self.screen.blit(robotBlit, (rozdelx + (rozdelx / 2) - widthR, wherey / 10 - 30))
        #-------------------------------------------------------------
        # skore
        rozdelx2 = wherex / 2 / 2
        rozdely2 = wherey / 2 / 2

        widthSH = skoreHBlit.get_width() / 2
        heightSH = skoreHBlit.get_height() / 2
        widthSR = skoreRBlit.get_width() / 2
        heightSR = skoreRBlit.get_height() / 2

        widthDvojb = dvojbBlit.get_width() / 2

        # vzorce pre skore
        x = rozdelx2 - widthSH
        y = rozdely2
        x2 = rozdelx + (rozdelx / 2) - widthSR
        y2 = rozdely2 

        x3 = rozdelx - widthDvojb
        y3 = rozdely2
        
        # blit skore
        self.screen.blit(skoreHBlit, (x , y))
        self.screen.blit(skoreRBlit, (x2, y2))
        self.screen.blit(dvojbBlit, (x3, y3))

    def print_time(self, cas):
        wherex = self.screen.get_size()[0]
        wherey = self.screen.get_size()[1]
        
        #rozdelit na polky
        rozdelx = wherex / 2
        rozdely = wherey / 2

        x5 = rozdelx - self.surface.get_width() /2
        y5 = rozdely + (rozdely / 2) - self.surface.get_height() /2

        self.surface.blit(cas, (0,0))
        self.screen.blit(self.surface, (x5, y5))
        
        

       

m=Computer(screen)
m.run()
