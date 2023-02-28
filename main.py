import pygame
from text import TextBox

running = True

# Window and Canvas setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CANVAS = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Text Input")

# Program Clock
CLOCK = pygame.time.Clock()
FPS = 60

# Colors
black = 0, 0, 0
white = 255, 255, 255

# Class instances
textbox1 = TextBox(
    x=25, y=100,
    width=200, height=300,
    bgColor=white, txtColor=black,
    fontSize=24
)

textbox2 = TextBox(
    x=275, y=100,
    width=200, height=300,
    bgColor=white, txtColor=black,
    fontSize=24
)

# Main Loop
while running:
    # Ticks the clock
    CLOCK.tick(FPS)
    # Refreshes the screen.
    CANVAS.fill(black)

    # Displays FPS
    pygame.display.set_caption(f"Text Input | FPS: {int(CLOCK.get_fps())}")

    # Gets position of mouse.
    mousePos = pygame.mouse.get_pos()

    # Checks for events.
    for event in pygame.event.get():
        # Allow the player to quit the game.
        if event.type == pygame.QUIT:
            print("Goodbye!")
            running = False
        # Checks for player input
        if event.type == pygame.KEYDOWN:
            # Calls method that deals with text input as soon as the program detects a key being pressed.
            # Uses event.key and unicode.
            # These will only run if their selected variable is true.
            if textbox1.selected is True:
                textbox1.textInput(event.key, event.unicode)
            if textbox2.selected is True:
                textbox2.textInput(event.key, event.unicode)

    # Update class instances
    textbox1.update(CANVAS, mousePos)
    textbox2.update(CANVAS, mousePos)

    # Updates the screen to reflect changes.
    SCREEN.blit(CANVAS, (0, 0))
    pygame.display.flip()
