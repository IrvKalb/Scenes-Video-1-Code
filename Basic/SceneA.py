# This is Scene A
import pygame
import pygwidgets
import pyghelpers
from Constants import *

class SceneA(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        self.messageField = pygwidgets.DisplayText(self.window, (25, 25), 'This is the A Scene ',
                                     fontSize=48, textColor=WHITE, width=610, justified='center')
        self.gotoBButton = pygwidgets.TextButton(self.window, (250, 250), 'Go to B')
        self.gotoCButton = pygwidgets.TextButton(self.window, (400, 250), 'Go to C')

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.gotoBButton.handleEvent(event):
                self.goToScene(SCENE_B)
            if self.gotoCButton.handleEvent(event):
                self.goToScene(SCENE_C)

    def draw(self):
        self.window.fill(RED)
        self.messageField.draw()
        self.gotoBButton.draw()
        self.gotoCButton.draw()
