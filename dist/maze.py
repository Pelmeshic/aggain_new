#создай игру "Лабиринт"! 
import pygame
# import mixer

pygame.mixer.init()
pygame.init()

clock = pygame.time.Clock()
color_wall = (0, 172, 107)
finish = False
loop = True
HEIGHT = 700
WIDTH = 500
backgorund = pygame.transform.scale(
    pygame.image.load('background_1.jpg'),
    (HEIGHT, WIDTH)
)

screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('labyrinth')


pygame.mixer.music.load('pelmeshki.mp3')

pygame.mixer.music.play(-1)

pygame.font.init()
font = pygame.font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))


class Wall(pygame.sprite.Sprite):
    def __init__(
        self,
        color: tuple,
        wall_x: int,
        wall_y: int,
        wall_width: int,
        wall_height: int,
        screen: pygame.Surface,
    ):
        super().__init__()
        self.color = color
        self.width = wall_width
        self.height = wall_height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color_wall)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.screen = screen

    def draw_wall(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, player_x, player_y, speed):
        super().__init__()
        self.image  = pygame.transform.scale(pygame.image.load(image), (65, 65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, image, player_x, player_y, speed):
        super().__init__(image, player_x, player_y, speed)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= 5

        if keys[pygame.K_DOWN] and self.rect.y < 435:
            self.rect.y += 5
            
        if keys[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= 5

        if keys[pygame.K_RIGHT] and self.rect.x < 640:
            self.rect.x += 5

class Enemy(GameSprite):
    def __init__(self, image, player_x, player_y, speed):
        super().__init__(image, player_x, player_y, speed)
        self.right = True

    def update(self):
        if self.rect.x >= 530 and not self.right:
            self.rect.x -= self.speed
            if self.rect.x <= 530:
                self.right = True

        elif self.rect.x <= 650 and self.right:
            self.rect.x += self.speed
            if self.rect.x >= 650:
                self.right = False

hero = Player('hero.png', 100, 100, 10)

villain = Enemy('cyborg.png', 500, 300, 2)

treasure = GameSprite('treasure.png', 525, 400, 0)


wall_1 = Wall( color_wall , 200, 0, 25, 420, screen)
wall_2 = Wall( color_wall , 290, 100, 25, 420, screen)
wall_3 = Wall( color_wall , 380, 0, 25, 420, screen)
wall_4 = Wall( color_wall , 470, 100, 25, 420, screen)
wall_5 = Wall( color_wall , 490, 300, 50, 50, screen)

while loop:
    clock.tick(60)
    screen.blit(backgorund, (0,0))

    if (
        pygame.sprite.collide_rect(hero, villain)
        # or pygame.sprite.collide_rect(hero, wall_1)
        # or pygame.sprite.collide_rect(hero, wall_2)
        # or pygame.sprite.collide_rect(hero, wall_3)
        # or pygame.sprite.collide_rect(hero, wall_4)
        # or pygame.sprite.collide_rect(hero, wall_5)
    ):
        finish = True
        screen.blit(lose, (200,200))
    if pygame.sprite.collide_rect(hero, treasure):
        finish = True
        screen.blit(win, (200, 200))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    if finish != True:
        hero.update()
        villain.update()
        treasure.update()
        screen.blit(backgorund, (0,0))

        hero.reset()
        villain.reset()
        treasure.reset()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()


    pygame.display.update()