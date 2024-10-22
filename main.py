import pygame

from pygame.time import Clock

from constants import *

def main():

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	(numpass, numfail) = pygame.init()

	print (f"Pygame initialized:")
	print (f"Modules passed: {numpass}")
	print (f"Modules failed: {numfail}")

	# Get a new GUI window
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Get a timer
	clock = Clock()
	delta = 0

	while True:

		# Check for system messages
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		# Fill the screen with the background colour	
		screen_rect = screen.fill(BACKGROUND_COLOUR, None, 0)

		# Refresh the screen
		pygame.display.flip()

		# Limit our FPS and track the delta time in seconds
		delta = clock.tick(60) / 1000

# Ensure we only run when executed directly, not when imported as a module:
if __name__ == "__main__":
	main()
