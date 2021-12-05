import pygame

pygame.init()
pygame.display.set_caption("DirectionKey")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((400,300))
background = 240,240,240
#Key Image
Right = pygame.image.load('RIGHT.png')
Right = pygame.transform.scale(Right,(100,100))

Left = pygame.image.load('LEFT.png')
Left = pygame.transform.scale(Left,(100,100))

Up = pygame.image.load('UP.png')
Up = pygame.transform.scale(Up,(100,100))


Down = pygame.image.load('DOWN.png')
Down = pygame.transform.scale(Down,(100,100))

Red = pygame.image.load('RED.png')
Red = pygame.transform.scale(Red,(100,100))

Right_2 = pygame.image.load('RIGHT.png')
Right_2 = pygame.transform.scale(Right_2,(100,100))

Left_2 = pygame.image.load('LEFT.png')
Left_2 = pygame.transform.scale(Left,(100,100))

Up_2 = pygame.image.load('Up.png')
Up_2 = pygame.transform.scale(Up_2,(100,100))

Down_2 = pygame.image.load('DOWN.png')
Down_2 = pygame.transform.scale(Down_2,(100,100))

Run = True
while Run:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        Run = False
                        pygame.quit()
                # 키 이벤트 
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                                Left = Red
                        if event.key == pygame.K_RIGHT:
                                Right = Red
                        if event.key == pygame.K_DOWN:
                                Down = Red
                        if event.key == pygame.K_UP:
                                Up = Red
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                                Left = Left_2
                        if event.key == pygame.K_RIGHT:
                                Right = Right_2
                        if event.key == pygame.K_DOWN:
                                Down = Down_2
                        if event.key == pygame.K_UP:
                                Up = Up_2
        # Image 생성
        screen.fill((background))
        screen.blit(Right,[270,140])
        screen.blit(Left,[30,140])
        screen.blit(Up,[150,30])
        screen.blit(Down,[150,140])
        
        pygame.display.update()