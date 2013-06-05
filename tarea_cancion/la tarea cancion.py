import os
import sys
import pygame.mixer
import pygame.cdrom
pygame.mixer.init(44100, -16, 2, 4036)
reload(sys)
sys.setdefaultencoding('utf8')
pygame.mixer.music.load('../apoyate.mp3')
pygame.mixer.music.play()
