import pygame
pygame.init()
#Розмір вікна
win = pygame.display.set_mode((1000, 512))
#Назва гри
pygame.display.set_caption('Luna')

walkRight = [
    pygame.image.load('image/right1.png'), 
    pygame.image.load('image/right2.png'), 
    pygame.image.load('image/right3.png'), 
    pygame.image.load('image/right4.png'), 
    pygame.image.load('image/right5.png'), 
    pygame.image.load('image/right7.png')]

walkLeft = [
    pygame.image.load('image/left1.png'), 
    pygame.image.load('image/left2.png'), 
    pygame.image.load('image/left3.png'), 
    pygame.image.load('image/left4.png'), 
    pygame.image.load('image/left5.png'), 
    pygame.image.load('image/left6.png')]

clock = pygame.time.Clock()

fon = pygame.image.load('image/fon.jpg')
#профіль героя
playerStand = pygame.image.load('image/im1.png')

x=50
y=430
widht=60
hight=71
speed=10
left = False
right = False
animCount = 0
isJump = False
jumpCount = 10

def drawWindow():
    win.blit(fon,(0, 0))
    global animCount

    #картинка 5 кадрів в сек....картинок 6, отже 5+6=30
    if animCount + 1 >= 30:
        animCount = 0
    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))
    #pygame.draw.rect(win, (13, 175, 184), (x, y, widht, hight))
    pygame.display.update()

run = True
while run:
    clock.tick(30)
    #pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>10:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x<950-widht-10:
        x += speed
        left = False
        right = True
    else:
        right = False
        left = False
        animCount = 0
    if not (isJump):
            #if keys[pygame.K_UP] and y>10:
                #y -= speed
            #if keys[pygame.K_DOWN] and y<560-hight-10:
               #y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2)/2
            else:
                y -= (jumpCount ** 2)/2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    drawWindow()


"""
 Сделал чуть проще:
  if JumpCount >= -10:
   y -= JumpCount * 2
   JumpCount -= 1
при отрицательных значениях куб возвращается назад...
"""

"""   
    win.fill((0,0,0))
    pygame.draw.rect(win, (13, 175, 184), (x, y, widht, hight))
    pygame.display.update()
"""
pygame.quit()
