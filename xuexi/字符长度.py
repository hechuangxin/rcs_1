# investment = 10000
# interest_rate = 0.0201
#
# for _ in range(30):
#     investment += investment * interest_rate
#
# print(f"回款金额: {investment:.2f} 元")

import pygame
import random

# 初始化游戏
pygame.init()

# 设置窗口尺寸
window_width = 480
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("飞机大战")

# 加载背景图像
background_img = pygame.image.load("background.jpg").convert()

# 加载飞机图像
player_img = pygame.image.load("player.png").convert()
player_rect = player_img.get_rect()
player_rect.topleft = (window_width / 2, window_height - player_rect.height)

# 加载敌机图像
enemy_img = pygame.image.load("enemy.png").convert()

# 游戏循环
running = True
clock = pygame.time.Clock()

# 创建敌机精灵组
enemies = pygame.sprite.Group()

# 创建敌机类
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0, window_width - self.rect.width), -self.rect.height)
        self.speed = random.randint(2, 4)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > window_height:
            self.kill()

# 游戏主循环
while running:
    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 绘制背景
    window.blit(background_img, (0, 0))

    # 移动玩家飞机
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    # 碰撞检测
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > window_width:
        player_rect.right = window_width
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > window_height:
        player_rect.bottom = window_height

    # 绘制玩家飞机
    window.blit(player_img, player_rect)

    # 生成敌机
    if random.randint(1, 50) == 1:
        enemy = Enemy()
        enemies.add(enemy)

    # 更新敌机位置
    enemies.update()

    # 绘制敌机
    enemies.draw(window)

    # 更新窗口显示
    pygame.display.update()

    # 控制帧率
    clock.tick(60)

# 退出游戏
pygame.quit()
