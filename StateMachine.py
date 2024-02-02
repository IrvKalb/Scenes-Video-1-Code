# State Machine approach to Scenes

import pygame

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

STATE_A = 'State A'
STATE_B = 'State B'
STATE_C = 'State C'

state = STATE_A  # set the starting state

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Handle events for the current state
        if state == STATE_A:
            # Code for handling events in STATE_A
        elif state == STATE_B:
            # Code for handling events in STATE_B
        elif state == STATE_C:
            # Code for handling events in STATE_C

    # Allow the current state to update itself
    if state == STATE_A:
        # Code for handling updates in STATE_A
    elif state == STATE_B:
        # Code for handling updates in STATE_B
    elif state == STATE_C:
        # Code for handling updates in STATE_C

    # Draw everything in the current state
    if state == STATE_A:
        # Code for handling drawing in STATE_A
    elif state == STATE_B:
        # Code for handling drawing in STATE_B
    elif state == STATE_C:
        # Code for handling drawing in STATE_C

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
