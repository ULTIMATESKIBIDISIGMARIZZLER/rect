import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
screen.fill(white)

class Rectangle():
    def __init__(self, color, pos, width, height, border_width=0):
        self.color = color
        self.pos = pos
        self.width = width
        self.height = height
        self.border_width = border_width
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (*self.pos, self.width, self.height), self.border_width)

    def grow(self, grew):
        self.width += grew
        self.height += grew
        pygame.draw.rect(self.screen, self.color, (*self.pos, self.width, self.height), self.border_width)

position = (200, 200)
width = 80
height = 60
border_width = 2

pygame.draw.rect(screen, red, (*position, width, height), border_width)
pygame.display.update()

blueRectangle = Rectangle(blue, position, width + 40, height + 30)
redRectangle = Rectangle(red, position, width + 20, height + 15)
yellowRectangle = Rectangle(yellow, position, width, height, 5)
greenRectangle = Rectangle(green, position, width, height, 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            blueRectangle.draw()
            redRectangle.draw()
            yellowRectangle.draw()
            greenRectangle.draw()
            pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONUP:
            blueRectangle.grow(3)
            redRectangle.grow(3)
            yellowRectangle.grow(3)
            greenRectangle.grow(3)
            pygame.display.update()
