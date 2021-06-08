import pygame
import os,sys
from pyscope import Pyscope


p = Pyscope()
input(p)

worldx = 1080
worldy = 1080
fps = 60
ani = 4
clock = pygame.time.Clock()
os.environ['SDL_VIDEODRIVER']='libx11-dev'
pygame.init()
world = pygame.display.set_mode([worldx,worldy])

#setup
backdrop = pygame.image.load(os.path.join('img','JiigoRavinev250px.jpg'))
backdropbox = world.get_rect()


def main():
	# pygame.display.init()
	# pygame.display.get_init()
	pygame.display.Info()
	input('chck')
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				try:
					sys.exit()
				finally:
					sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == ord('q'):
					pygame.quit()
				try:
					sys.exit()
				finally:
					sys.exit()

if __name__ == "__main__":
	main()