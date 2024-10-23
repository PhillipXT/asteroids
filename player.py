import pygame

from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):

	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.cooldown = 0

	def triangle(self):
		
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right

		return [a, b, c]
	
	def draw(self, surface):
		pygame.draw.polygon(surface, PLAYER_COLOUR, self.triangle(), 2)

	def rotate(self, delta):
		self.rotation += PLAYER_TURN_SPEED * delta

	def move(self, delta):
		vector = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += vector * PLAYER_SPEED * delta

	def shoot(self):
		if self.cooldown <= 0:
			shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
			vector = pygame.Vector2(0, 1).rotate(self.rotation)
			shot.velocity = vector * SHOT_SPEED
			self.cooldown = SHOT_INTERVAL

	def update(self, delta):
		keys = pygame.key.get_pressed()
		self.cooldown -= delta

		if keys[pygame.K_a]:
			self.rotate(-delta)

		if keys[pygame.K_d]:
			self.rotate(delta)

		if keys[pygame.K_w]:
			self.move(delta)

		if keys[pygame.K_s]:
			self.move(-delta)

		if keys[pygame.K_SPACE]:
			self.shoot()