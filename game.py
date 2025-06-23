import pygame
from sys import exit

pygame.init() #initiazes pygame 

#Create the display surface - the window the user will see
screen = pygame.display.set_mode((800, 600)) #width, height
pygame.display.set_caption("Jumping Snail") #title of the window
clock = pygame.time.Clock() #to control the frame rate


while True:      #This is to run the game forever
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   #Quits the game if the window is closed
            exit()  # Exits the game if the window is closed
    # To draw all our elements
    # To update everything
    pygame.display.update() #updates the display surface
    clock.tick(60) #limits the frame rate to 60 FPS

