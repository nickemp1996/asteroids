# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	Player.containers = (updatables, drawables)
	player1 = Player(x, y)
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		updatables.update(dt)
		#player1.update(dt)

		screen.fill("black")
		for drawable in drawables:
			drawable.draw(screen)
		#player1.draw(screen)
		pygame.display.flip()
		
		# limit the framerate to 60 FPS
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()