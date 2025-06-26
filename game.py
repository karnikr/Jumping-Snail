import pygame
from sys import exit

pygame.init() #initiazes pygame 

#Create the display surface - the window the user will see
screen = pygame.display.set_mode((800, 425)) #width, height
pygame.display.set_caption("Jumping Snail") #title of the window

clock = pygame.time.Clock() #to control the frame rate
test_font = pygame.font.Font('Jumping-Snail/font/Pixeltype.ttf', 50) #Pixel font with size 50

#Background surfaces
sky_surface = pygame.image.load('Jumping-Snail/graphics/Sky.png').convert()
ground_surface = pygame.image.load('Jumping-Snail/graphics/ground.png').convert()

#Text
title_surface = test_font.render('JUMPING SNAIL', False, 'Red')
title_rect = title_surface.get_rect(center=(400,50)) #rect for the title surface, using center to position it in the middle of the screen
score_surface = test_font.render('SCORE:', False, 'Blue') #rendering the score text
score_rect = score_surface.get_rect(topleft=(50, 50)) #rect for the score surface

# Snail
snail_surface = pygame.image.load('Jumping-Snail/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(600,300)) #rect for the snail surface, using bottomright to change it up

#Player
player_surface = pygame.image.load('Jumping-Snail/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300)) #rect for the player surface

#Gravity
player_gravity = 0 #initial gravity value

while True:      #This is to run the game forever
    # To draw all our elements
    # To update everything

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   #Quits the game if the window is closed
            exit()  # Exits the game if the window is closed

        if event.type == pygame.MOUSEBUTTONDOWN: #checks if the mouse button is pressed
           if player_rect.collidepoint(event.pos) and player_rect.bottom >=300: #checks if the mouse position is within the player rectangle and if the player is on the floor
                player_gravity = -20 #sets the player gravity to -20 to make the player jump
        
        #Player Movement with event loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >=300: #checks if the space key is pressed and if the player is on the floor
                print('Jump!') #prints 'Jump!' if the space key is pressed
                player_gravity = -20 #sets the player gravity to -20 to make the player jump
   

    screen.blit(sky_surface,(0,0)) #draws the sky surface on the screen at position (0,0)
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen, 'Pink', title_rect) 
    pygame.draw.rect(screen, 'Pink', title_rect, 6, 20) #Margin around the title surface, 6 pixels thick, with rounded corners of radius 20
    
    screen.blit(title_surface,title_rect)
    
    pygame.draw.rect(screen,'Green', score_rect,6, 20) #draws a green rectangle around the score surface
    screen.blit(score_surface, score_rect) #draws the score surface on the screen at the score rect position
    
    snail_rect.x -= 4 #moves the any point of the snail rectangle to the left by 4 pixels each frame
    if snail_rect.right <= 0: #checks if the right point of the snail rectangle is less than or equal to 0
        snail_rect.left = 800 #resets the snail rectangle left position to 800 if it goes off the screen
    
    screen.blit(snail_surface,snail_rect) 
    
    # player_rect.left += 1 #moves the player rect to the right by 1 pixel each frame
    #Player
    player_gravity += 1 #increases the gravity value by 1 each frame
    player_rect.y += player_gravity #moves the player rectangle down by the gravity value each
    if player_rect.bottom >= 300:
        player_rect.bottom = 300 #sets the player rectangle bottom to 300 if it goes below 300 (ground level)
    screen.blit(player_surface,player_rect) #draws the player surface on the screen at the player rect position


    #Player Movement
    # Using pygame.key.get_pressed() to check the state of the keys
   # keys = pygame.key.get_pressed() #gets the state of all the keys
    #if keys[pygame.K_SPACE]: #checks if the space key is pressed
    #    player_rect.y -= 5 #moves the player rectangle up by 5 pixels
    #else:
    #    player_rect.y += 5 #moves the player rectangle down by 5 pixels if the space key is not pressed
        

    if player_rect.colliderect(snail_rect):
        print('Game Over')
        pygame.quit()
        exit()
   
    # mouse_pos = pygame.mouse.get_pos() #gets the mouse position
    #if player_rect.collidepoint(mouse_pos): #checks if the mouse position is within the player rectangle
    #    print(pygame.mouse.get_pressed()) #prints the mouse button pressed state


    pygame.display.update() #updates the display surface
    clock.tick(60) #limits the frame rate to 60 FPS

