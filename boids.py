import pygame
import random

class Boid:
    def __init__(
        self,
        x,
        y,
        max_speed,
        width,
        height,         
    ):
        self.position = pygame.Vector2(x, y)
        
        self.velocity = pygame.Vector2(
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        )
        
        self.acceleration = pygame.Vector2(0, 0)
        
        self.max_speed = max_speed
        self.width = width
        self.height = height
    
    
    def update(self, dt):
        self.velocity += self.acceleration * dt
        
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)
            
        self.position += self.velocity * dt
        
        self.acceleration *= 0
        
        
    def wrap_screen(self):
        if self.position.x > self.width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = self.width
        if self.position.y > self.height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = self.height
            

        