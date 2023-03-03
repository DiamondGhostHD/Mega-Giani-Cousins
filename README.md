# Mega-Giani-Cousins

Player Class:

-in method "__init__":
    -the original image is loaded from the files
    -the original image is resized to fit well on screen
    -the new image is saved in the variable "image_player"
    -it's size in saved in the variable "player_size"
    -x and y positions are given for the player

-in method "flip":
    -the original images is faced to the right => it needs to be flipped when walking to the left

-in method "gravity"
    -gravity is added to the player
    -it restricts the player from falling out of the world



Brick Class: 

-in method "__init__":
    -the original image is loaded from the files
    -the original image is resized to fit well on screen
    -the new image is saved in the variable "image_brick"
    -it's size in saved in the variable "brick_size"
    -x and y positions are given for the brick


In the "while running" loop:

-the backround image is moved from left to right (or vice versa) --> to create the illusion that the player is moving
-the keys are detected when pressed
-the images are drawn on screen
-the game is closed when the "X" button from the windows is pressed

