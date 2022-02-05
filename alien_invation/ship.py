import pygame as pg

class Ship :
    """管理飞机的类"""

    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #加载飞船图像并获取其外接矩形alien_invation\images\ship.bmp
        self.ship_image = pg.image.load('alien_invation\images\ship.bmp')
        self.ship_rect = self.ship_image.get_rect()

        #对于每艘新飞船，都将其放在屏幕底部中央
        self.ship_rect.midbottom = self.screen_rect.midbottom

        #在飞船的属性x中存储小数值
        self.ship_x = float(self.ship_rect.x)
        self.ship_y = float(self.ship_rect.y)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.ship_x += self.settings.ship_speed
        if self.moving_left and self.ship_rect.left > 0:
            self.ship_x -= self.settings.ship_speed
        if self.moving_up and self.ship_rect.top > 0:
            self.ship_y -= self.settings.ship_speed
        if self.moving_down and self.ship_rect.bottom < self.screen_rect.bottom:
            self.ship_y += self.settings.ship_speed
        self.ship_rect.x = self.ship_x
        self.ship_rect.y = self.ship_y

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.ship_image,self.ship_rect)