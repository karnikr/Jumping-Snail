# Jumping-Snail
This is an introductory game to learn pygame

I am using this repo to help me grow as a programmer and develop more projects


## Notes
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

Now we are going to make an event to close the loop