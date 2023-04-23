import pygame
import time


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, front, back):
        super().__init__()
        self.front = front
        self.back = back
        self.image = self.front  # starts with front facing image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, keys):
        if keys[pygame.K_w]:
            self.image = self.back
            self.rect.y -= 2
        if keys[pygame.K_s]:
            self.image = self.front
            self.rect.y += 2
        if keys[pygame.K_a]:
            self.rect.x -= 2
        if keys[pygame.K_d]:
            self.rect.x += 2


pygame.init()

screen = pygame.display.set_mode((1080, 900))
pygame.display.set_caption("Pixel Tales")


def load_sprite(dir, sx, sy):
    sprite = pygame.image.load(dir).convert_alpha()
    sprite = pygame.transform.scale(sprite,
                                    (int(sprite.get_width() * sx),
                                     int(sprite.get_height() * sy)))
    return sprite


jake_front = load_sprite('32x-files/render32/v4/jake-front.png', 3, 3)
jake_back = load_sprite('32x-files/render32/v4/jake-back.png', 3, 3)

jake_sprite = Sprite(32, 32, jake_front, jake_back)

all_sprites = pygame.sprite.Group()
all_sprites.add(jake_sprite)

jake_sprite.rect.centerx = screen.get_rect().centerx
jake_sprite.rect.centery = screen.get_rect().centery

while True:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    all_sprites.update(keys)

    screen.fill((8, 3, 0))

    all_sprites.draw(screen)

    pygame.display.flip()
