import pygame

if not pygame.font: print('Error pygame.font not found!')
if not pygame.mixer: print('Error pygame.mixer not found!')


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("GameJam2 - Dungeon")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)
        screen.fill((100, 100, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        pygame.display.flip()


if __name__ == '__main__':
    main()
