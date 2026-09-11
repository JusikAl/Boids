import pygame 
import random

from pygame import Vector2
from boids import Boid


pygame.init()
screen = pygame.display.set_mode((800, 800))
running = True
clock = pygame.time.Clock()

ran_timer = random.uniform(0.5, 5)

boid = Boid(400, 400, 200, 800, 800)
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    dt = clock.tick(60)/1000
    
    screen.fill("white")
    
    boid.update(dt)
    
    angle = boid.velocity.angle_to(pygame.Vector2(1, 0))
    
    triangle_points = [
        boid.position + pygame.Vector2(0, -25).rotate(-angle),
        boid.position + pygame.Vector2(-20, 25).rotate(-angle),
        boid.position + pygame.Vector2(20, 25).rotate(-angle)
    ]
    
    ran_timer -= dt
    if ran_timer <= 0:
        boid.acceleration += pygame.Vector2(random.randint(-1, 1), random.randint(-1, 1))
        ran_timer = random.uniform(0.5, 5)
    
    pygame.Vector2(0, -25).rotate(angle)
    
    pygame.draw.polygon(screen, 'red', triangle_points, width=5)
        
    pygame.display.flip()
    
    
    
pygame.quit()
