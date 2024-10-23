import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):

	def __init__(self, x, y, radius):
		
		if hasattr(self, "containers"):
			super().__init__(self.containers)
		else:
			super().__init__()

		self.position = pygame.Vector2(x, y)
		self.velocity = pygame.Vector2(0, 0)
		self.radius = radius

	# Subclasses must override
	def draw(self, surface):
		pass

	# Subclasses must override
	def update(self, delta):
		pass