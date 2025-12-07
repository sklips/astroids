from circleshape import CircleShape
# noinspection PyUnresolvedReferences
import pygame
import random

from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity*dt

    def split(self):

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            first_velocity = self.velocity.rotate(angle)
            second_velocity = self.velocity.rotate(angle*-1)
            smaller_radius = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position[0],self.position[1],smaller_radius)
            second_asteroid = Asteroid(self.position[0], self.position[1], smaller_radius)
            first_asteroid.velocity = first_velocity
            second_asteroid.velocity = second_velocity

