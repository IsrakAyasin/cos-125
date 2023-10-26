def snake():
    import pygame
    pygame.init()
    dis=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Snake Game")

    blue=(0,0,255)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red=(255,0,0)

    x1 = 300
    y1 = 300

    x1_change = 0
    y1_change = 0
    clock = pygame.time.Clock() 
    game_over=False
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -5
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 5
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -5
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 5
                    x1_change = 0
        x1+=x1_change
        y1+=y1_change
        dis.fill(blue)
            
        pygame.draw.rect(dis,red,[x1,y1,10,10])
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()
snake()