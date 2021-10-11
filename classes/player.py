import pygame


class Player:
    def __init__(self):
        print("Ei")
        self.force = 5
        self.elapsed = 0
        self.frame_delay = 8
        self.transform = False
        self.transform_elapsed = 0
        self.debugTransformation = 0

        # Carga de sprites
        self.player_sprites = []
        self.load_sprite_sheet()
        self.current_sprite = 0
        self.player_image = self.player_sprites[self.current_sprite]
        self.player = pygame.transform.scale(self.player_image, (80, 80))

        # Difinir posiciones
        self.player_rect = self.player.get_rect()
        self.player_rect.x = 250
        self.player_rect.y = 400
        self.max_derecha = pygame.display.get_window_size()[0] - self.player.get_size()[0]

    def update(self, screen):
        # COntrolamos que sprite mostrar y cuanto tiempo
        if self.transform:
            self.load_sprite_sheet_transform()
            if self.current_sprite == 3:
                self.transform_elapsed += 1
                # Ejecutamos 4 veces la animacion completa
                if self.transform_elapsed == 32:
                    # Devolvemos a su sprite original
                    self.current_sprite = 0
                    # self.load_sprite_sheet()
                    self.transform_elapsed = 0
                    self.transform = False
                    if self.debugTransformation == 0:
                        self.load_sprite_sheet_rock()
                        self.debugTransformation += 1
                    elif self.debugTransformation == 1:
                        self.load_sprite_sheet_scissor()
                        self.debugTransformation += 1
                    elif self.debugTransformation == 2:
                        self.load_sprite_sheet_paper()
                        self.debugTransformation += 1
                    else:
                        self.load_sprite_sheet()
                        self.debugTransformation = 0




        # Printamos el jugador
        self.draw(screen)

    def draw(self, screen):
        # Controlamos los fps de la animacion
        self.elapsed += 1
        if self.elapsed >= self.frame_delay:
            self.elapsed = 0
            # Cargamos el siguiente sprite
            self.current_sprite += 1
            if self.current_sprite >= len(self.player_sprites):
                self.current_sprite = 0
            self.player_image = self.player_sprites[self.current_sprite]
            self.player = pygame.transform.scale(self.player_image, (80, 80))

        # Mostramos por pantalla
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
            self.player_rect.x -= self.force
        elif key_pressed[pygame.K_RIGHT]:
            self.player_rect.x += self.force
        elif key_pressed[pygame.K_a]:
            self.current_sprite = 0
            self.transform = True

        self.__check_limits()

    def load_sprite_sheet(self):
        self.player_sprites = []
        for i in range(4):
            # Cargamos los sprites de idle
            self.player_sprites.append(
                pygame.image.load(
                    "sprites/idle/"
                    + "idlePlayer"
                    + str(i + 1)
                    + ".png"
                )
            )

    def load_sprite_sheet_transform(self):
        self.player_sprites = []
        for i in range(4):
            # Cargamos los sprites de idle
            self.player_sprites.append(
                pygame.image.load(
                    "sprites/transform/"
                    + "transformPlayer"
                    + str(i + 1)
                    + ".png"
                )
            )

    def load_sprite_sheet_rock(self):
        self.player_sprites = []
        # Cargamos los sprites de idle
        self.player_sprites.append(
            pygame.image.load(
                "sprites/rock/"
                + "rockPlayer"
                + ".png"
            )
        )

    def load_sprite_sheet_paper(self):
        self.player_sprites = []
        # Cargamos los sprites de idle
        self.player_sprites.append(
            pygame.image.load(
                "sprites/paper/"
                + "paperPlayer"
                + ".png"
            )
        )

    def load_sprite_sheet_scissor(self):
        self.player_sprites = []
        # Cargamos los sprites de idle
        self.player_sprites.append(
            pygame.image.load(
                "sprites/scissors/"
                + "scissorPlayer"
                + ".png"
            )
        )
