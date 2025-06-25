# Notes
This is the notes page, here I have recorded each and every step and thought process that has gone through my mind when it comes to learning about how to create this game and learning about Pygame as a whole. Hope this is useful to someone in the future, even if it is just future me.

---

### Introduction
A video game is essentially like a movie in which the frames or images generated is based on the players input

1. Checking the player input -> the event loop
2. Use that information to place the elements or images on screen
Both these steps together creates 1 image

Once this whole process is finished, we get rid of the entire image generated and then doing both steps 1 and 2 again, almost 30 to 60 times a second

2D Games -> Places images on the screen
3D Games -> Places 3D models on the screen

### What does pygame do?
-> we can make movies also in pygame
1. Pygame helps you draw images or helps us display images (Helps create windows, Plays Sounds)
2. Checks for player input like mouse or keyboard units (input() stops the entire code but pygame does not)
3. Other game development tools like collisions, creating text and timers etc

Pygame is not used for actual game development like the other game engines such as Unity or Unreal

Making games in pygame -> solving a ton of problems myself and becoming a good programer -> I can quickly learn new game engines or other tools

Using a game engine -> I learn to use specific tools but does help me grow -> tied to the engine and lose flexibility

Learn pygame to become a good programmer

### Coing Part:

#### This part has the basic set up of our Game Window
1. `pygame.init()`
    - this is really important and neccesaary to run for pygame
    - starts pygame and initiaties the subparts like rendering images and sound and stuff
    - like starting the engine of the car

2. `screen = pygame.display.set_mode((800, 600))`
    - This is to create the screen that the user will see
    - the `.display.set_mode` sets the window and it is followed by the width and the height like `(width,height)`

3. `pygame.display.set_caption("Jumping Snail")`
    - `.set_caption` is to set the title of the window, in this case "Jumping Snail"

4. `while True:`
    - this is used to make sure that the window stays open
    - this is to draw all our elements
    - and to update the display that is shown to the user

5. `pygame.display.updae()`
    - all this is doing is updating the surface that is being shown to the user
    - only call it and dont think about it type beat


6. `for event in pygame.event.get():`
    - Now we are going to make an event to close the loop
    - this is to loop through all the events
    - `pygame.evet.get()` is used to get the events
    - `for event in` part is just used to loop through the events

7. `if event.type == pygame.QUIT:`
    - this checks if the type of the event is `QUIT`
    - this is a constant that is the same as the 'x' button on the window or the cross button used to close the window

8. Most Common Event Types:
    - `QUIT`
    - `ACTIVEEVENT`
    - `KEYDOWN`
    - `KEYUP`
    - `MOUSEMOTION`
    - `MOUSEBUTTONUP`
    - `MOUSEBUTTONDOWN`
    - `JOYAXISMOTION`
    - `JOYBALLMOTION`
    - `JOYHATMOTION`
    - `JOYBUTTONUP`
    - `JOYBUTTONDOWN`
    - `VIDEORESIZE`
    - `VIDEOEXPOSE`
    - `USEREVENT`
    -- (I will explain these later, but these are common according to documentation)


9. When we call `pygame.quit()` it quits the window
    - `pygame.quit()` is the opposite of `pygame.init()`
    - Since the `while` loop is open we find an error since after the `init` is `quitted`, mthe next `pygame,display.update()` won't work
    - this is why we use `exit()` and `from sys import exit`

10. Now we have to determine the framerate of our game
    - the animation speed depends on how fast we are updating the game
    - lets say we have a character who moves 10px to the right every frame:
        - 1 frame per sec -> 10px/s * 1fps -> 10px/second
        - 1 frames per sec -> 10px/s * 100fps -> 1000px/second
        - this defers the speed of the game
        - we have to address this for the game to run consistently
    
    - Ideally run it at 60 fps for the game contantly
        - Create a ceiling and a floor for the frame rate
        - creating the ceiling is easy since we can tell the computer to pause between frames (slow it down)
        - creating the floor is harder since we need to get the computer to run faster than it is (speed it up) (if computer is slower than the computer)
            - to account for the min frame rate, ensure there isnt too much at the same time on the screen

    
    - For all this:
        - create a `clock` object
            - to help with time and frame rate
        - `clock = pygame.time.Clock()` 
            - to control the frame rate
        - when we call it in the while loop: `clock.tick(60)`
            - this tells that the while loop should not run faster than 60 times per second, to ensure that the game does not run too fast
            - this sets the maximum frame rate
---

#### Now for Displaying the images
- Surfaces
    - To draw any kind of image we need a Surface
    - Display Surface
        - The player will see whatever was displayed on the display surface
        - To display anything on the display surface, we need regular surfaces
    - Regular Surface
        - Essentially a single image (something imported, rendered or created, plain color)
        - Needs to be put on the display surface to be visible
    
    - Think of it like the Display surface is the Final Canvas to be presented and the Regular surface is like a posted note or a sticker or photo to be posted on the final canvas

    - The display surface must be unique and always visible
    - the regular surface can be multiple and must be connected to the display surface to be seen

- Coding to create the surfaces
    - `pygame.Surface((w,h))` : is the code to create a surface
    - `screen.blit(surface,position)` : is the code to put one surface on another
        - blit stands for 'block image transfer'
            - fancy way of saying, we want one image on top of another image
            - to draw anything
        - 'surface' is the surface we want to place
        - 'position' is the position of the surface, like `(x,y)`
        - `screen.blit(test_surface,(0,0))` draws the surface on the screen at position (0,0)
        - the origin point is on the top left
            - to go to the right, we need to increase x
            - to go down we need to increase y
            - (0,0) is (x,y)
    
    - Plain Colour : to add the surface that is only a plain color
        - the surfaces are initially empty and plain black
        - to add color we use: `.fill()` command
            - `test_surface.fill('red')` : fills the surface with red color
        - this is added in the top left since that point is (0,0)
        - `test_surface  = pygame.Surface((100, 200))` : create a surface to draw on
        - `test_surface.fill('red')`

    - Background Image:
        - to add the image in the background:
            - `test_surface = pygame.image.load('grpahics/Sky.png')`
            - this will deposit the image
        - this uses the same `blit()` command and stuff also
    
    - Surface with Text
        - To create text we must first:
            - 1. create an image of the text
            - 2. place it on the surface
        - Steps:
            - 1. Create a font that stores the style and font size
            - 2. Use the font info to write the text on the surface
            - 3. Blit the text on the surface

11. To create the Background :
    - `sky_surface = pygame.image.load('Jumping-Snail/graphics/Sky.png')`
        - this is to create the sky
    - `ground_surface = pygame.image.load('Jumping-Snail/graphics/ground.png')`
        - this is to create the ground
    
    - `screen.blit(sky_surface,(0,0))`
        - this is to draw the sky on the screen
    - `screen.blit(ground_surface,(0,300))`
        - this is to draw the ground on the screen
    
12. To Add text on the surface:
    - `test_font = pygame.font.Font(font type, font size)` is added on top, 'None' uses the default pygame font
    - then we create a new surface for the text: `text_surface = test_font.render(text, antialias, color)`, this is used with render().
        - the text: What will be written
        - Antialias: Are we going to smooth the edges of the text
            - make it true when working with anything else
            - make it false when working with pixel art
            - in this case it is false
    - `text_surface = test_font.render('My game', False, 'Green')`
        - this displays 'My game' in the default font, green color with the sides not smooth. This is an example
    
    - Add the specific Font:
        - Download the font in ttf and put it in the `test_font = pygame.font.Font(font type, font size)` font type area
        - Like this: `test_font = pygame.font.Font('Jumping-Snail/font/Pixeltype.ttf', 50)`
    
    - Draw the text on the surface: `screen.blit(text_surface,(400,50))`


---

#### Animations
- Currently, the image looks static and the images are in the same position
- Since we always place the images in the same position and the image is updated 60 times per second, it remains static to us.
- If we update the position of each of the surfaces, we would get a moving image.
- Animating each surface just means changing the position slightly on each frame
- Use `screen.blit()` and instead of one constant position, use a variable which is continuously updated.

- Now we are going to draw the snail enemy and make him go from right to left to show that the snail is moving:
    - First, making the snail object: `snail_surface = pygame.image.load('Jumping-Snail/graphics/snail/snail1.png')`
    - Then draw it on the surface: `screen.blit(snail_surface,(600,265))` : this means, 600 pixels from the left and 265 from the top
- Now the snail is Static since the snail is always in the same position

- In order to chage this:
    - Create another variable for the 'x' position which is 600
        - `snail_x_pos = 600`
        - and this changes to: `screen.blit(snail_surface,(snail_x_pos,265))`
        - if we run this, nothing will change, since it is the same
    
    - Now, since it is a while loop, we can change the `snail_x_pos` variable, since the while loop will be running until the game is closed correct.
        - So what we do now is add an incremenet or decrement
            - increment to move the snail from left to right
            - decremenet to move the snail from right to left
        
        - Since in this case we want to show that the runner is running toward the snail, we must move it from right to left and hence decrement the value of `snail_x_pos` by any amount to get the snail to 'move'

        - This is what we get: `snail_x_pos -= 4 #moves the snail to the left by 4 pixels each frame`

    - This will allow the snail to leave the screen and never be seen again

    - Now for the snail to be seen again:
        - After it crosses a certain point in the screen, reset the position to 800, which is bigger than the size of the window, so it will seem like the snail has re-appeared and is looping
        - The snail's width is 100 pixels, so once the snail completely crosses the screen, the position of the screen will become -100 or lesser, then we change the position back to 800 and go again.
    - This will be the code: 
        - `snail_x_pos -= 4` 
        - `if snail_x_pos < -100: snail_x_pos = 800`

- Big Note:
    - Everytime we update the surface, i.e., the while loop is being updated, we are essentially re-drawing all the images again on top of the previous frame and not getting rid of it really.
    - You want to draw a proper background so that it goes well.


---

#### Coverting the Background
- We convert the background image to something that pygame can work with more easily.
- We do this by adding `.covert()` when we are declairing the images used.
- convert() is used to optimize the image for faster rendering
    - `sky_surface = pygame.image.load('Jumping-Snail/graphics/Sky.png').convert()`
    - `ground_surface = pygame.image.load('Jumping-Snail/graphics/ground.png').convert()`
- covert_alpha() is used to optimize as well but it removes the white and black stuff behind the image
    - `snail_surface = pygame.image.load('Jumping-Snail/graphics/snail/snail1.png').convert_alpha()`

- This is important and good practice to make sure that the rendering is done as smoothly as possible.

---

#### Rectangles
The core functions of rectangles are:

1. Help placing surfaces precisely and efficiently
2. Detect basic Collisions

Futhermore: 

1. Placing the surface precisely:
    - We only place the top left currently, so ideally we want to get a point in the bottom of the snail to be more precise

    - To do this:
        - Separate the images in 2 steps:
            - image information is placed on the surface 
            - Placement via the rectangle: position is on the rectangle
            - this uses the sprite class
            - split the image into 2 variables and control it together
    
    - How does the rectangle work?
        -  The points on the rectangle that we can work with are:
            - Either as a tuple (x,y):
                - topleft
                - midtop
                - topright
                - midleft
                - center
                - midright
                - bottomleft
                - midbottom
                - bottomright
            - Or individual positions like left or right:
                - top
                - left
                - center_x, center_y
                - right
                - bottom
            - If we move any individual points on the rectangle then we move all the other points, they all stay relative to each other
            - There is also size, width and height
            - We can use rectangle to place a surface anywhere in the rectangle.

    - Drawing the player:
        - To initialize the player: `player_surface = pygame.image.load('Jumping-Snail/graphics/Player/player_walk_1.png').convert_aplha()`
        - To draw the player: `screen.blit(player_surface,(80,200))`

        - Now we have noticed that there is a gap between the player and the ground image, so we need to create a rectangle:
            - `player_rect = pygame.Rect(left, top, width, height)` is one way, but in this we must give it the exact dimensions of the image or thing we have to make the rectangle around. So we need to have another that gets the exact size of the surface
            - `player_rect = player_surface.get_rect()`: the `.get_rect()` takes the surface and draws a rectangle around it.
                - we can also specify the exact position where we want to place it by putting the position and the cordinates like: `player_rect = player_surface.get_rect(topleft = (80,200))`, this will make sure that the topleft of the rectangle is placed the position at 80 x and 200 y
                - once we do that then we change the code a bit from : `screen.blit(player_surface,(80,200))` to `screen.blit(player_surface,player_rect)` which essentially draws the player surface on the screen at the player rect position
                - now when we change `topleft` to `midleft`, we see the change:
                `player_rect = player_surface.get_rect(midleft = (80,200))`, this will make sure that the midleft of the rectangle is placed the position at 80 x and 200 y
                    - essentially, this changes the position of the point of the rectangle that is specified and goes from there.
                    - normally we place the top left point, instead we are using different points
                
        - In order to move the player, we can just use the left point of the rectangle and increment it by 1 to move the player from left to right:
            - ` player_rect.left += 1 #moves the player rect to the right by 1 pixel each frame`
        
        - Same thing for the snail:
            - `snail_rect = snail_surface.get_rect(bottomright=(600,300)) #rect for the snail surface`

            - `snail_rect.x -= 4 #moves the any point of the snail rectangle to the left by 4 pixels each frame`
            - `if snail_rect.right <= 0: #checks if the right point of the snail rectangle is less than or equal to 0`
                - `snail_rect.left = 800 #resets the snail rectangle left point to 800 if it goes off the screen`
            - `screen.blit(snail_surface,snail_rect)`
    
2. Dectecting Collisions:
    - to check if my one rectangle is colliding with another
        - `rect1.colliderect(rect2)` : becomes `player_rect.colliderect(snail_rect)` in this case
            - returns 0 if no collision
            - returns 1 if collision
        - pygame checks every single collision and tells us if there is one, the collision triggers multiple times
            - in this game, we will end it with one collision happens
            - if there is a health bar or something like that:
                - make sure you have a single collision and then some invincibility frame
        - this one is a basic kind of collision
    
    - `rect1.collidepoint((x,y))`
        - another way to check for a collision
        - checks if one point collides with the rectangle
        - if you want to click with a mouse on something, this is important
        - this checks if the position (x,y) is in the rectangle rect1 or not
            - how to get those position points of the mouse:
                - `pygame.mouse`
                    - gives us mouse position or the buttons being pressed and the visibility etc.
                    - `mouse_pos = pygame.mouse.get_pos() #gets the mouse position`
                    - `if player_rect.collidepoint(mouse_pos): #checks if the mouse position is within the player rectangle`
                        -  ` print('Player clicked on the person!')`
                    - also: `print(pygame.mouse.get_pressed()) #prints the mouse button pressed state` (right, middle, left) buttons
            - also : `if event.type == pygame.MOUSEMOTION:`
                -   `print(event.pos) #prints the mouse position when the mouse is moved`
                - this shows the position of the mouse on the game
            - also : `if event.type == pygame.MOUSEBUTTONDOWN:` checks if the mouse button is pressed
            - also: `if event.type == pygame.MOUSEBUTTONUP:` checks if the mouse is release after being pressed

        - to check if the player rectangle is colliding with the mouse as an event:
            - `if event.type == pygame.MOUSEMOTION:`
                -   `if player_rect.collidepoint(event.pos): #checks if the mouse position is within the player rectangle`
                    - `print('Mouse is over the player!')`

                - event loop to see where the position is
                    -   get mousemotion, position

3. Drawing backgrounds:
    - Using the `pygame.draw` and then specifying the shape like `.rect()` or `.circle()` we can draw things on the screen
        - it takes multiple arguments being: (surface,colour,rectangle) being the basic ones and then mutliple after like width, border radius, etc
        - eg: `pygame.draw.rect(screen, 'Pink', title_rect) #draws a pink rectangle around the title surface`
        - `screen.blit(title_surface,title_rect)`
        - eg: `pygame.draw.rect(screen,'Green', score_rect) #draws a green rectangle around the score surface`
        - `screen.blit(score_surface, score_rect) #draws the score surface on the screen at the score rect position`
    - You can draw different shapes based on what you want pretty much