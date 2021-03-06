import pygame as pg 
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船发射子弹的类"""

    def __init__(self,ai_game):
        """在飞船当前位置创建一个子弹对象"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        

        #在（0,0）处创建一个表示子弹的矩形，再设置正确的位置 
        self.bullet_rect = pg.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.bullet_rect.midtop = ai_game.ship.ship_rect.midtop

        #储存用小数表示的子弹位置
        self.bullet_y = float(self.bullet_rect.y)

    def update(self):
        """向上移动子弹"""

        #更新表示子弹位置的小数值
        self.bullet_y -= self.settings.bullet_speed
        #更新显示子弹的rect的位置
        self.bullet_rect.y = self.bullet_y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pg.draw.rect(self.screen, self.color, self.bullet_rect)



