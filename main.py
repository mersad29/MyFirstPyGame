# Example file showing a circle moving on screen
import pygame
from random import randint
import random
import math

# pygame setup
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

class Character():
    def __init__(self):
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


    def draw(self):
        pygame.draw.circle(screen, "white", self.pos, 40)
        self.speed = 300 * dt

    def update(self, keys):
        if self.pos.y > 50:
            self.speed = 0

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.speed = 800 * dt
        else:
            self.speed = 300 * dt
        if keys[pygame.K_LEFT]:
            self.pos.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.pos.x += self.speed
        if keys[pygame.K_UP]:
            self.pos.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.pos.y += self.speed

class Enemy():
    def __init__(self):
        rand_x= int(randint(1,6))
        rand_y= int(randint(1,6))
        self.pos = pygame.Vector2(screen.get_width() / rand_x, screen.get_height() / rand_y)
    def draw(self):
        pygame.draw.circle(screen, "red", self.pos, 20)
        self.speed = 600 * dt

    def update(self):
            # Move the object randomly
            width = 1280
            height = 720
            direction = random.choice(['up', 'down', 'left', 'right'])
            if direction == 'up':
                self.pos.y -= self.speed
            elif direction == 'down':
                self.pos.y += self.speed
            elif direction == 'left':
                self.pos.x -= self.speed
            elif direction == 'right':
                self.pos.x += self.speed
            # If the object goes off the screen, wrap it around
            if self.pos.x > width:
                self.pos.x = 0
            elif self.pos.x < 0:
                self.pos.x = width
            elif self.pos.y < 0:
                self.pos.y = height
            elif self.pos.y > height:
                self.pos.y = 0


        # Add a slower speed when the shift key is held down

player = Character()
enemy = Enemy()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    player.draw()
    keys = pygame.key.get_pressed()
    player.update(keys)
    enemy.draw()
    enemy.update()
    # flip() the display to put your work on screen
    pygame.display.flip()

    # Check for collisions
    distance = math.sqrt((player.pos.x - player.pos.x)**2 + (player.pos.y - player.pos.y)**2)
    if distance == 5:
        running = False

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()