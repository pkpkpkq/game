import pygame
pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("数字大战") 
f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf',50)
text = f.render("数字大战",True,(255,0,0),(0,0,0))
#获得显示对象的rect区域坐标
textRect =text.get_rect()
# 设置显示对象居中
textRect.center = (500,200)
# 将准备好的文本信息，绘制到主屏幕 Screen 上。
screen.blit(text,textRect)
#创建图像,并优化显示
start = pygame.Surface((100,50),flags=pygame.HWSURFACE)
arms = pygame.Surface((100,50),flags=pygame.HWSURFACE)
player = pygame.image.load("player.png").convert()  
#填充颜色
start.fill(color='red')
arms.fill(color='green')
#将图像绘制到屏幕
screen.blit(start, (300, 300))
screen.blit(arms, (600, 300))
screen.blit(player, (400, 100))
while True:
    # 循环获取事件，监听事件状态
    for event in pygame.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段
        if event.type == pygame.QUIT:
            #卸载所有模块
            pygame.quit()

    pygame.display.flip() #更新屏幕内容