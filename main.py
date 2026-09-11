import pygame 
import sys
from boids import Boid


pygame.init()
screen = pygame.display.set_mode((800, 800))
running = True
clock = pygame.time.Clock()

boid = Boid(400, 400, 200, 800, 800)
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("white")
    
    dt = clock.tick(60)/1000
    boid.update(dt)
    
    triangle_points = [
        boid.position + pygame.Vector2(0, +25),
        boid.position + pygame.Vector2(+20, -25),
        boid.position + pygame.Vector2(-20, -25)
    ]
    
    pygame.draw.polygon(screen, 'red', triangle_points, width=5)
        
    pygame.display.flip()
        
pygame.quit()
            
sys.exit()