import pygame


class Player:
    def __init__(self):
        self.force = 5
        self.orientation = 0

        # Carga de sprites
        self.spriteNameOrientation = [
            "front/Player-Sprite-000",
            # "sided/left/Player-Sprite-Sideway-000",
            # "sided/right/Player-Sprite-Sideway-000",
        ]
        self.player_sprites = [[] for i in range(3)]
        self.load_sprite_sheet()
        self.current_sprite = 0
        self.player_image = self.player_sprites[self.orientation][self.current_sprite]
        self.player = pygame.transform.scale(self.player_image, (80, 80))

        # Difinir posiciones
        self.player_rect = self.player.get_rect()
        self.player_rect.x = 250
        self.player_rect.y = 400
        self.max_derecha = pygame.display.get_window_size()[0] - self.player.get_size()[0]

    def draw(self, screen):
        self.current_sprite += 1
        if self.current_sprite >= len(self.player_sprites[self.orientation]):
            self.current_sprite = 0
        self.player_image = self.player_sprites[self.orientation][self.current_sprite]
        self.player = pygame.transform.scale(self.player_image, (80, 80))

        screen.blit(self.player, self.player_rect)

    def __check_limits(self):
        """
        Controlamos que no se pase del ux
        """
        if self.player_rect.x > self.max_derecha:
            self.player_rect.x = self.max_derecha
        elif self.player_rect.x < 0:
            self.player_rect.x = 0

    def movement(self, key_pressed):
        """
        Nos movemos de izquierda a derecha
        :param key_pressed: pygame.key.get_pressed()
        """
        if key_pressed[pygame.K_LEFT]:
            self.orientation = 1
            self.player_rect.x -= self.force
        elif key_pressed[pygame.K_RIGHT]:
            self.orientation = 2
            self.player_rect.x += self.force
        else:
            self.orientation = 0
        self.__check_limits()

    def load_sprite_sheet(self):
        for j in range(3):
            for i in range(4):
                # Cargamos los sprites de frente y de lado
                self.player_sprites[j].append(
                    pygame.image.load(
                        "sprites/Player/"
                        + self.spriteNameOrientation[j]
                        + str(i + 1)
                        + ".png"
                    )
                )

