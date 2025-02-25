import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	dt = 0

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatables, drawables)
	Asteroid.containers = (asteroids, updatables, drawables)
	AsteroidField.containers = updatables
	Shot.containers = (shots, updatables, drawables)

	player1 = Player(x, y)
	asteroid_field = AsteroidField()

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		updatables.update(dt)

		for asteroid in asteroids:
			if asteroid.collision_detection(player1):
				print("Game Over!")	
				exit()	

			for shot in shots:
				if asteroid.collision_detection(shot):
					asteroid.split()
					shot.kill()

		screen.fill("black")
		for obj in drawables:
			obj.draw(screen)
		
		pygame.display.flip()
		
		# limit the framerate to 60 FPS
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()