import pygame
'''
This holds all the code to make text boxes and text input to function.
I already had to rewrite this script twice. It's pretty do without proper planning. I guess I should start doing that
from now on.
'''


class TextBox:
    def __init__(self, x, y, width, height, bgColor, txtColor, fontSize):

        # Establishes the list for all text lines
        self.lines = []
        # The current line that is ready for input.
        self.currentLine = 0

        # Sets textbox and color
        self.textBox = pygame.Rect(x, y, width, height)
        self.boxColor = bgColor

        # Creates a line of text
        self.lines.append(self.Text(x, y, fontSize, txtColor))
        # Gets the line that was previously created
        self.firstLine = self.lines[0]
        self.lineHeight = self.firstLine.height

        # Gets the maximum number of lines that could fit in the textbox using a simple math.
        # It's Text Box Height divided by line height. Then it rounds the result into a whole number
        self.maxLines = int(height / self.lineHeight)
        print(f"Lines: {self.maxLines}")

        # Whether the instance is selected or not.
        self.selected = False

        # Calls a method that creates empty lines
        self.setupLines(x, y, fontSize, txtColor, self.maxLines, self.lineHeight)

    def update(self, surface, mousePos):

        # Checks if the Left Mouse button is clicked
        if pygame.mouse.get_pressed()[0]:
            # If true, then check if the mouse is hovering over textbox
            if self.textBox.collidepoint(mousePos):
                self.selected = True
            else:
                self.selected = False

        # Draws everything
        self.draw(surface)

    def textInput(self, key, unicode):
        # Gets the current line for edit.
        line = self.lines[self.currentLine]

        # This checks for certain key presses using a match case to make it more readable.
        # Also found out that I could use "return" statements to end the method process all together.
        # So that means if key press is detected, it will simply not run the last line of code in the method.
        match key:
            case pygame.K_BACKSPACE:  # Backspace Key
                # This deletes characters when backspace is pressed, or return to previous line if the current line is
                # empty.
                if line.currentText == "":
                    self.moveLine(-1)
                    return
                else:
                    line.currentText = line.currentText[:-1]
                    return
            case pygame.K_RETURN:  # Enter Key
                # This goes to the next line if the current line isn't the last one.
                self.moveLine(1)
                return
            case pygame.K_UP:  # Up Key
                # Goes to previous line
                self.moveLine(-1)
            case pygame.K_DOWN:  # Down Key
                self.moveLine(1)

        # Calls the line's updateLine method.
        line.updateLine(unicode)

        # Line character limit.
        # Checks if the line's length + 10 is greater than or equal to the textbox's width.
        if line.length + 10 >= self.textBox.width:
            print("You have reached the charactor limit.")
            # If true, deletes a character from line.
            line.currentText = line.currentText[:-1]

    def draw(self, surface):
        # Draws textbox and text
        pygame.draw.rect(surface, self.boxColor, self.textBox)

        # Draws every line
        for line in self.lines:
            # The line will simply not draw if it's empty.
            if line.currentText != "":

                # Updates line text to reflect line.currentText
                line.text = line.font.render(line.currentText, True, line.textColor)

                surface.blit(line.text, line.rect.topleft)

    # Sets up empty lines for text input.
    def setupLines(self, x, y, fontSize, textColor, maxLines, txtHeight):
        # Store y into local variable
        spawnY = y
        # For loop that runs a number of times
        for line in range(maxLines - 1):
            # Increments spawnY by txtHeight
            spawnY += txtHeight
            # Creates empty line.
            self.lines.append(self.Text(x, spawnY, fontSize, textColor))

    # Handles changing selected lines
    def moveLine(self, direction):
        # -1 = previous line, 1 = next line

        if direction == -1:
            # Goes to previous line as long as current line isn't the first on the list.
            if self.currentLine != 0:
                # If true, decrement currentLine by 1
                self.currentLine -= 1
                return
            else:
                return

        if direction == 1:
            # Goes to next line as long as current line isn't the last on the list.
            if self.currentLine == len(self.lines) - 1:
                return
            else:
                # If not true increment currentLine by 1
                self.currentLine += 1
                return

    # Nested class for the Text. I thought each new instance of Textbox will also have their own version of this class.
    # I was wrong, and I had to rewrite some code to support multiple textboxes.
    class Text:
        def __init__(self, x, y, fontSize, txtColor):
            # Basic font.
            self.font = pygame.font.Font(None, fontSize)

            # The text the line is going to display, starts off empty.
            self.currentText = ""

            # Gets text color
            self.textColor = txtColor

            # Sets up line and rect
            self.text = self.font.render(self.currentText, True, txtColor)
            self.rect = self.text.get_rect()
            self.rect.topleft = x, y

            # The length of text line
            self.length = 0

            # Gets text height
            self.height = self.text.get_height()

        # When called, it will add to currentText.
        def updateLine(self, unicode):
            self.currentText += unicode

            # Gets the line's length from self.text
            self.length = self.text.get_width()
