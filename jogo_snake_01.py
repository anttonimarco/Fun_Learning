import pygame

pygame.init()

janela = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Game Python')

janela_on = True

while janela_on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_on = False

pygame.quit()
