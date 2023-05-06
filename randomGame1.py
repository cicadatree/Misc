import pygame

white = (255, 255, 255)


class Menu:
    def __init__(self, game):
        self.font = pygame.font.Font(None, 36)
        self.option1 = pygame.image.load('C:/Users/brend/python projects/Misc/Sprites/Option.png').convert_alpha()
        self.option2 = pygame.image.load('C:/Users/brend/python projects/Misc/Sprites/Option.png').convert_alpha()
        self.option3 = pygame.image.load('C:/Users/brend/python projects/Misc/Sprites/Option.png').convert_alpha()
        self.menu_surface = pygame.Surface((game.screen_width, game.screen_height), pygame.SRCALPHA, 32)


class Player:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.speed = 0.5  # You can now set a speed less than 1
        self.width = 32
        self.height = 32
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 0, 0))  # Fill the square with red color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)


class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.menu = Menu(self)
        self.game_state = "menu"
        self.player = Player(self.screen_width // 2, self.screen_height // 2)

    def start_game(self):
        print("Starting a new game")
        self.player = Player(self.screen_width // 2, self.screen_height // 2)
        # game logic goes here
        
    def draw_menu(self):
        self.menu.menu_surface.blit(self.menu.option1, (25, 10))
        self.menu.menu_surface.blit(self.menu.option2, (25, 100))
        self.menu.menu_surface.blit(self.menu.option3, (25, 190))

        self.option1_rect = self.menu.option1.get_rect(topleft=(25, 10))
        self.option2_rect = self.menu.option2.get_rect(topleft=(25, 100))
        self.option3_rect = self.menu.option3.get_rect(topleft=(25, 190))        

        self.screen.blit(self.menu.menu_surface, (0, 0))

    def update_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.move(-1, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move(1, 0)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player.move(0, -1)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.player.move(0, 1)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if self.option1_rect.collidepoint(pos):
                    self.game_state = "playing"
                    self.start_game()
                    print("Option 1 clicked!")
                elif self.option2_rect.collidepoint(pos):
                    print("Option 2 clicked!")
                elif self.option3_rect.collidepoint(pos):
                    print("Option 3 clicked!")
        return True


game = Game()

# game loop
def gameloop():
    running = True
    while running:
        if game.game_state == "menu":
            game.screen.fill((255, 255, 255))
            game.draw_menu()
        elif game.game_state == "playing":
            game.screen.fill((0, 0, 255)) # this is a placcholder; changes background to indicate that a new game has started.
            game.player.draw(game.screen)
            game.update_movement()

        running = game.check_event()
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    gameloop()


# Menu Sprite Attribution: Image by upklyak on Freepik (https://www.freepik.com/free-vector/cartoon-set-wood-paper-game-ui-boards_38591358.htm#query=game%20menu%20button&position=12&from_view=keyword&track=robertav1_2_sidr)