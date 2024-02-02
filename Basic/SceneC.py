# This is Scene C
import pygame
import pygwidgets
import pyghelpers
from Constants import *

class SceneC(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        self.messageField = pygwidgets.DisplayText(self.window, (25, 25), 'This is the C Scene',
                                     fontSize=48, textColor=WHITE, width=610, justified='center')
        self.gotoAButton = pygwidgets.TextButton(self.window, (100, 250), 'Go to A')
        self.gotoBButton = pygwidgets.TextButton(self.window, (250, 250), 'Go to B')
        self.circleX = 0
        self.CIRCLE_Y = 350

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.gotoAButton.handleEvent(event):
                self.goToScene(SCENE_A)
            if self.gotoBButton.handleEvent(event):
                self.goToScene(SCENE_B)

    # This is called in every frame
    # Move the circle to the right, and wrap if needed
    def update(self):
        self.circleX = self.circleX + 5
        if self.circleX > WINDOW_WIDTH:  # wrap to the left side
            self.circleX = 0

    def draw(self):
        self.window.fill(BLUE)
        self.messageField.draw()
        self.gotoAButton.draw()
        self.gotoBButton.draw()
        pygame.draw.circle(self.window, WHITE, (self.circleX, self.CIRCLE_Y), 20, 0)

