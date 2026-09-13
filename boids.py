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
        max_force,
    ):
        self.position = pygame.Vector2(x, y)
        
        self.velocity = pygame.Vector2(
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        )
        
        self.wander_force = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        
        self.max_force = max_force
        self.max_speed = max_speed
        self.width = width
        self.height = height
    
    
    def update(self, dt):
        self.velocity += self.acceleration * dt
        
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)
            
        self.position += self.velocity * dt
        
        self.wrap_screen()
        
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
    
    def add_force(self, force):
        self.acceleration += force
        
        if self.acceleration.length() > self.max_force:
            self.acceleration.scale_to_length(self.max_force)
        

    def wander(self):
        self.wander_force += pygame.Vector2(
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        )
        
        if self.wander_force.length() > self.max_force:
            self.wander_force.scale_to_length(self.max_force)
        
        self.add_force(self.wander_force)