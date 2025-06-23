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

Now we are going to make an event to close the loop
6. `for event in pygame.event.get():`
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

### Now for Displaying the images
