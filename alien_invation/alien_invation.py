
from turtle import right

from matplotlib.style import available
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

import sys
import pygame as pg


class AlienInvation:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pg.init()  #初始化背景设置

        self.settings = Settings()

        #全屏模式
        if self.settings.full_screnn_mode :
            self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height

        self.screen = pg.display.set_mode(
            (self.settings.screen_width,self.settings.screen_heigh)
            )

        pg.display.set_caption("Alien Invation")

        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()
        self.alien = pg.sprite.Group()

        self._create_fleet()
    

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_alien()
            self._update_screen()

            

    def _check_events(self):
        # 监视键盘和鼠标事件
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    #退出游戏
                    sys.exit()
            elif event.type == pg.KEYDOWN:
                #监测按下KEY
                if event.key == pg.K_q:
                    #退出游戏
                    sys.exit()
                elif event.key == pg.K_d:
                    #向右移动飞船
                    self.ship.moving_right = True
                elif event.key == pg.K_a:
                    #向左移动飞船
                    self.ship.moving_left = True
                elif event.key == pg.K_w:
                    #向上移动飞船
                    self.ship.moving_up = True
                elif event.key == pg.K_s:
                    #向下移动飞船
                    self.ship.moving_down = True
                elif event.key == pg.K_SPACE:
                    #发射子弹
                    self._fire_bullet()

            elif event.type == pg.KEYUP:
                #监测松开KEY
                if event.key == pg.K_d:
                    #停止向右移动飞船
                    self.ship.moving_right = False
                elif event.key == pg.K_a:
                    #停止向左移动飞船
                    self.ship.moving_left = False
                elif event.key == pg.K_w:
                    #停止向上移动飞船
                    self.ship.moving_up = False
                elif event.key == pg.K_s:
                    #停止向下移动飞船
                    self.ship.moving_down = False
            
                
    
    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        if len(self.bullets) < self.settings.bullets_num_max:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
                        
    def _update_bullets(self):
        """更新子弹并删除消失的子弹"""
        # 更新子弹位置
        self.bullets.update()

        #删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.bullet_rect.bottom <= 0:
                 self.bullets.remove(bullet)
        # print(len(self.bullets))

    def _update_screen(self):
         """更新屏幕上的图像，并切换到新屏幕"""
         self.screen.fill(self.settings.bg_color)
         self.ship.update()
         self.ship.blitme()
         for bullet in self.bullets.sprites():
             bullet.draw_bullet()
         self.alien.draw(self.screen)
         
        
         #让最近绘制的屏幕可见
         pg.display.flip()

    def _create_fleet(self):
        """创建外星人群"""

        #创建一个外星人并计算一行可容纳多少个外星人
        #外星人的间距为外星人的宽度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        #计算屏幕可容纳多少行外星人
        ship_height = self.ship.ship_rect.height
        available_space_y = (self.settings.screen_heigh - 
                                    (3 * alien_height) - ship_height )
        number_rows = available_space_y // ( 2 * alien_height)

        #创建外星人群
        for number_row in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,number_row)


    def _create_alien(self,alien_number,row_number):
        #创建一个外星人并将加入当前行
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.alien.add(alien)

    def _update_alien(self):
        """更新外星人群中所有外星人的位置"""
        self.alien.update()
    
    def  _check_fleet_edge(self):
        """有外星人到达边缘时采取相应措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """外星人整体下移，并改变平移方向"""
        for alien in self.alien.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
                

if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvation()
    ai.run_game()

