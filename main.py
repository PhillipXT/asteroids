import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	(numpass, numfail) = pygame.init()

	print (f"Pygame initialized:")
	print (f"Modules passed: {numpass}")
	print (f"Modules failed: {numfail}")

	# Get a new GUI window and set it as the drawing surface
	surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Get a timer and set a delta time variable
	clock = pygame.time.Clock()
	delta = 0

	# Create the groups we'll need
	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	# Assign objects to groups
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, shots)

	# Instantiate game objects
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	# Initiate the game loop
	while True:

		# Check for system messages
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		# Fill the screen with the background colour	
		surface.fill(BACKGROUND_COLOUR, None, 0)

		# Update game objects
		for u in updatable:
			u.update(delta)

		# Check for collision with an asteroid
		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game over!")
				return

		# Check for shot hitting an asteroid
		for asteroid in asteroids:
			for shot in shots:
				if shot.collision(asteroid):
					asteroid.split()
					shot.kill()

		# Draw game objects
		for d in drawable:
			d.draw(surface)

		# Refresh the screen
		pygame.display.flip()

		# Limit our FPS and track the delta time in seconds
		delta = clock.tick(60) / 1000

# Ensure we only run when executed directly, not when imported as a module:
if __name__ == "__main__":
	main()
