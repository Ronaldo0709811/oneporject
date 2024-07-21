import pygame
import sys

# 初始化 Pygame
pygame.init()

# 定义常量和颜色
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (30, 30, 30)  # 深色背景

# 设置窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dark Background Game")

# 定义小球的类
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # 红色小球
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5

    def update(self):
        # 移动小球
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # 碰撞检测
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# 创建游戏对象
ball = Ball()
all_sprites = pygame.sprite.Group()
all_sprites.add(ball)

# 游戏循环
running = True
while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新游戏状态
    all_sprites.update()

    # 绘制游戏界面
    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)

    # 更新屏幕显示
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(60)

# 退出游戏
pygame.quit()
sys.exit()
