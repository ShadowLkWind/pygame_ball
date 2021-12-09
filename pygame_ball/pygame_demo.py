import pygame

# pygame资源初始化
pygame.init()
w = 900  # 宽
h = 600  # 高
# 创建游戏窗口
screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)  # 保存窗口对象 RESIZABLE 可修改窗口大小
image_maple = pygame.image.load("./image/maple.ico")  # 加载图片
image_maple_rect = image_maple.get_rect()  # 获取矩形框
background1 = pygame.image.load("./image/1.png")  # 获取背景图1
background2 = pygame.image.load("./image/2.png")  # 获取背景图2
pygame.mixer.music.load("./music/1.mp3")  # 获取背景音乐
pygame.mixer.music.play(-1, 0)  # 循环播放，从零秒开始
clock = pygame.time.Clock()  # 时间模块
x = 1  # x轴的速度
y = 1  # y轴的速度

key = True  # 循环控制条件
move_key = True  # 移动条件

while key:
    # 事件处理
    for event in pygame.event.get():
        # 退出
        if event.type == pygame.QUIT:
            key = False
            break
        # 按下事件
        if event.type == pygame.KEYDOWN:
            # 按下 ↑键
            if event.key == pygame.K_UP:
                if y >= 0:
                    y += 1
                else:
                    y -= 1
            # 按下 ↓键
            if event.key == pygame.K_DOWN:
                if y > 0:
                    y -= 1
                if y < 0:
                    y += 1
            # 按下 →键
            if event.key == pygame.K_RIGHT:
                if x >= 0:
                    x += 1
                else:
                    x -= 1
            # 按下 ←键
            if event.key == pygame.K_LEFT:
                if x > 0:
                    x -= 1
                if x < 0:
                    x += 1
        # 获取边框
        if event.type == pygame.VIDEORESIZE:
            w, h = event.size
        # 鼠标按下
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 判断左键
            if event.button == 1:
                move_key = False
        # 鼠标松开
        if event.type == pygame.MOUSEBUTTONUP:
            # 判断左键
            if event.button == 1:
                move_key = True
        # 鼠标长按
        if event.type == pygame.MOUSEMOTION:
            # 判断左键
            if event.buttons[0] == 1:
                image_maple_rect = image_maple_rect.move(event.pos[0] - image_maple_rect.left - 64,
                                                         event.pos[1] - image_maple_rect.top - 64)
    # 游戏内部逻辑处理
    # 绘制背景
    screen.blit(background1, (0, 0))
    screen.blit(background2, (750, 0))
    # 点击停止移动，松开继续
    if move_key:
        image_maple_rect = image_maple_rect.move(x, y)
    # 绘制图片
    screen.blit(image_maple, image_maple_rect)
    # 撞墙回弹
    if image_maple_rect.top <= 0:
        if y <= 0:
            y = -y
    if image_maple_rect.bottom >= h:
        if y > 0:
            y = -y
    if image_maple_rect.left <= 0:
        if x <= 0:
            x = -x
    if image_maple_rect.right >= w:
        if x > 0:
            x = -x

    # 更新画面
    pygame.display.update()
    # 速度设置
    clock.tick(666)
# 游戏退出
pygame.quit()
