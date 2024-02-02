# This is Scene B
import pygame
import pygwidgets
import pyghelpers
from Constants import *

class SceneB(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        self.messageField = pygwidgets.DisplayText(self.window, (25, 25), 'This is the B Scene',
                                     fontSize=48, textColor=WHITE, width=610, justified='center')
        self.gotoAButton = pygwidgets.TextButton(self.window, (100, 250), 'Go to A')
        self.gotoCButton = pygwidgets.TextButton(self.window, (400, 250), 'Go to C')

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.gotoAButton.handleEvent(event):
                self.goToScene(SCENE_A)
            if self.gotoCButton.handleEvent(event):
                self.goToScene(SCENE_C)

    def draw(self):
        self.window.fill(GREEN)
        self.messageField.draw()
        self.gotoAButton.draw()
        self.gotoCButton.draw()
