# Three Scenes Demo Main

# This is a demo of a typical main program using the Scene Manager.
# It should start by defining the size of your window, initializing pygame and creating the window.
# Next, you  create an instance of each of your scenes.
# Then build a dictionary of all the scenes, which would look like:
#    {<scene1Key:<scene1Instance>, <scene2key>:<scene2Instance>, ... <sceneNInstance>]
# The first scene in the dictionary will be used as the starting scene.
# The ordering of the other scenes does not matter.
# Using that scenesDict, and a frames per second, you instantiate the SceneMgr object
# Finally, you tell the SceneMgr object to run.
# The SceneMgr takes over, runs the main loop, and handles navigation and
#    communication between scenes.

# 1 - Import packages
import pygame
import pyghelpers
import Constants
from SceneA import *
from SceneB import *
from SceneC import *

# 2 - Define constants
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Instantiate all scenes and store them in a dictionary (as of pyghelpers 1.1)
scenesDict = {SCENE_A: SceneA(window),
                    SCENE_B: SceneB(window),
                    SCENE_C: SceneC(window)}

# Create the Scene Manager, passing in the scenes list, and the FPS
oSceneMgr = pyghelpers.SceneMgr(scenesDict, FRAMES_PER_SECOND)

# Tell the Scene Manager to start running
oSceneMgr.run()
