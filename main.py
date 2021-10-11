import os

from classes.game import Game
from classes.player import Player
# from classes.ball import Ball
# from classes.blocks import Blocks

import pygame

if __name__ == '__main__':
    game = Game()
    player = Player()

    game.flip()
    x = 250
    y = 250
    while game.playing:
        # Controlamos si se pulsa cerrar
        game.trigger_quit_game()

        # Controlamos la tecla pulsada
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_DOWN]:
            game.pause = True

        # Si el juego esta pausado lo reiniciamos
        if game.pause:
            if pressed[pygame.K_UP]:
                game = Game()
                player = Player()
                x = 250
                y = 250

        # Iniciamos el latido
        if not game.pause:
            game.start_hearthbeat()

        # Obtenemos la tecla pulsada y movemos el jugador
        player.movement(pressed)

        if not game.pause:
            # Renderizamos el jugador
            player.draw(game.screen)

        # Finalizamos el latido
        if not game.pause:
            game.end_hearthbeat()

    game.quit_game()
