import pygame

from constants import *
from player import Player

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

	# Instantiate the player
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	# Initiate the game loop
	while True:

		# Check for system messages
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		# Fill the screen with the background colour	
		surface.fill(BACKGROUND_COLOUR, None, 0)

		# Draw the player
		player.update(delta)
		player.draw(surface)

		# Refresh the screen
		pygame.display.flip()

		# Limit our FPS and track the delta time in seconds
		delta = clock.tick(60) / 1000

# Ensure we only run when executed directly, not when imported as a module:
if __name__ == "__main__":
	main()
