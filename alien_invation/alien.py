import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #加载外星人图像并设置其rect属性
        self.image = pg.image.load('alien_invation\\images\\alien.bmp')
        self.rect = self.image.get_rect()

        #每个外心人初始都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #储存外星人的精确水平位置
        self.x = float(self.rect.x)

    def update(self):
        """向右移动外星人"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x
