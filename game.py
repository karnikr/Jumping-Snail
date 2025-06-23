import pygame

pygame.init() #initiazes pygame 

#Create the display surface - the window the user will see
screen = pygame.display.set_mode((800, 600)) #width, height
pygame.display.set_caption("Jumping Snail") #title of the window

while True:      #This is to run the game forever
    
    # To draw all our elements
    # To update everything
    pygame.display.updae() #updates the display surface