import pygame
import time

# setup
WIN_WIDTH = 1024
WIN_HEIGHT = 600
ENEMY_WIDTH = 60
ENEMY_HEIGHT = 60
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization
pygame.init()

# load image (background, enemy, buttons, hp)
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
enemy_image = pygame.transform.scale(pygame.image.load("images/enemy.png"), (ENEMY_WIDTH, ENEMY_HEIGHT))
continue_image = pygame.transform.scale(pygame.image.load("images/continue.png"), (BTN_WIDTH, BTN_HEIGHT))
muse_image = pygame.transform.scale(pygame.image.load("images/muse.png"), (BTN_WIDTH, BTN_HEIGHT))
pause_image = pygame.transform.scale(pygame.image.load("images/pause.png"), (BTN_WIDTH, BTN_HEIGHT))
sound_image = pygame.transform.scale(pygame.image.load("images/sound.png"), (BTN_WIDTH, BTN_HEIGHT))
hp_image = pygame.transform.scale(pygame.image.load("images/hp.png"), (HP_WIDTH, HP_HEIGHT))
hp_gray_image = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (HP_WIDTH, HP_HEIGHT))

# clock
clock = pygame.time.Clock()

# time
start = time.time()

# set the title
pygame.display.set_caption("My first game")


class Game:
    def __init__(self):
        # window
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        # hp
        self.hp = 7
        self.max_hp = 10
        pass

    def game_run(self):
        # game loop
        run = True
        while run:
            clock.tick(FPS)

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # draw background
            self.window.blit(background_image, (0, 0))

            # draw enemy and health bar
            self.window.blit(enemy_image, (15, 250))
            pygame.draw.rect(self.window, RED, [25, 245, 50, 5])

            # draw menu (and buttons)
            pygame.draw.rect(self.window, BLACK, [0, 0, WIN_WIDTH, 80])
            self.window.blit(muse_image, (700, 0))
            self.window.blit(sound_image, (780, 0))
            self.window.blit(continue_image, (860, 0))
            self.window.blit(pause_image, (940, 0))

            # draw hp
            for i in range(5):
                self.window.blit(hp_image, (415 + i * 40, 0))
            for i in range(2):
                self.window.blit(hp_image, (415 + i * 40, 40))
            for i in range(2, 5):
                self.window.blit(hp_gray_image, (415 + i * 40, 40))

            # draw time
            end = time.time()
            time_str = f' {int(end - start) // 60}:{int(end - start) % 60:02} '
            font = pygame.font.SysFont('arial', 28)
            text_surface = font.render(time_str, True, WHITE, BLACK)
            self.window.blit(text_surface, (0, 570))

            pygame.display.update()


if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()



