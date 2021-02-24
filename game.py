import pygame

(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption("Simple PyGame")
running = True
x=60
y=60

try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.draw.rect(screen, (0,128,255), pygame.Rect(x, y, 60, 60))   

        pygame.display.flip()             
    pygame.quit()

except SystemExit:
    pygame.quit()                    