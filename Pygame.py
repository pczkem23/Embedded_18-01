import pygame

width = 320
height = 240
radius = 20
blank = 0

pygame.init()
window = pygame.display.set_mode ((width, height))
window.fill (pygame.Color(255,255,255))

while True:
    pygame.draw.circle(window,
                        pygame.Color(255,0,0),
                      (width/2, height/2),
                      radius,blank)
    pygame.display.update()
