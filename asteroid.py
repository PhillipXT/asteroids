import pygame

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, surface):
		pygame.draw.circle(surface, ASTEROID_COLOUR, self.position, self.radius, 2)

	def update(self, delta):
		self.position += self.velocity * delta
