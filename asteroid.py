import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, surface):
		pygame.draw.circle(surface, ASTEROID_COLOUR, self.position, self.radius, 2)

	def update(self, delta):
		self.position += self.velocity * delta

	def split(self):
		
		self.kill()
		
		if self.radius > ASTEROID_MIN_RADIUS:
			angle = random.uniform(20, 50)
			v1 = self.velocity.rotate(angle)
			v2 = self.velocity.rotate(-angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS

			shard_one = Asteroid(self.position.x, self.position.y, new_radius)
			shard_one.velocity = v1 * 1.2

			shard_two = Asteroid(self.position.x, self.position.y, new_radius)
			shard_two.velocity = v2 * 1.2