import pygame
import time


class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, front_img, back_img):
        super().__init__()
        self.front_img = front_img
        self.back_img = back_img
        self.image = self.front_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, keys):
        if keys[pygame.K_w]:
            self.image = self.back_img
            self.rect.y -= 2
        if keys[pygame.K_a]:
            self.image = self.front_img
            self.rect.x -= 2
        if keys[pygame.K_s]:
            self.rect.y += 2
        if keys[pygame.K_d]:
            self.rect.x += 2


pygame.init()

screen = pygame.display.set_mode((1080, 900))
pygame.display.set_caption("Pixel Tales")

# loading the sprite


def load_sprite(location, scale: list):
    sprite = pygame.image.load(location).convert_alpha()
    sprite = pygame.transform.scale(sprite,
                                    int(sprite.get_width() * scale[0]),
                                    int(sprite.get_height() * scale[1]))


jake_front = load_sprite(
    '../Documents/Github/pixel-tales/render32/v4/jake-front', (2, 2))
jake_back = load_sprite(
    '../Documents/Github/pixel-tales/render32/v4/jake-back', (2, 2))


#  create a sprite gorup
all_sprites = pygame.sprite.Group()


jake_sprite = MySprite(32, 32, front_img=jake_front, back_img=jake_back)
all_sprites.add(jake_sprite)

jake_sprite.rect.centerx = screen.get_rect().centerx
jake_sprite.rect.centery = screen.get_rect().centery


while True:
    time.sleep(1/100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    screen.fill((8, 3, 0))

    all_sprites.update(keys)
    all_sprites.draw(screen)

    pygame.display.flip()
