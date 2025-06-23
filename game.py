import pygame
from sys import exit

pygame.init() #initiazes pygame 

#Create the display surface - the window the user will see
screen = pygame.display.set_mode((800, 425)) #width, height
pygame.display.set_caption("Jumping Snail") #title of the window

clock = pygame.time.Clock() #to control the frame rate
test_font = pygame.font.Font('Jumping-Snail/font/Pixeltype.ttf', 50) #Pixel font with size 50


sky_surface = pygame.image.load('Jumping-Snail/graphics/Sky.png').convert()
ground_surface = pygame.image.load('Jumping-Snail/graphics/ground.png').convert()

text_surface = test_font.render('JUMPING SNAIL', False, 'Red')
snail_surface = pygame.image.load('Jumping-Snail/graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

player_surface = pygame.image.load('Jumping-Snail/graphics/Player/player_walk_1.png').convert_alpha()

while True:      #This is to run the game forever
    # To draw all our elements
    # To update everything

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   #Quits the game if the window is closed
            exit()  # Exits the game if the window is closed

    screen.blit(sky_surface,(0,0)) #draws the sky surface on the screen at position (0,0)
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    
    snail_x_pos -= 4 #moves the snail to the left by 4 pixels each frame
    if snail_x_pos < -100:
        snail_x_pos = 800 #resets the snail position to 800 if it goes off the screen
    
    screen.blit(snail_surface,(snail_x_pos,265)) #draws the snail surface on the screen at position (500,250)
    screen.blit(player_surface,(80,200))

    pygame.display.update() #updates the display surface
    clock.tick(60) #limits the frame rate to 60 FPS

