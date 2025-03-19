import pygame
import cUniversal
from enum import Enum

# Enumeration of the different mouse buttons
class MouseButtons(Enum):

    BUTTON_NONE = 0
    BUTTON_LEFT = 1
    BUTTON_SCROLL = 2
    BUTTON_RIGHT = 3

# Enumeration of the mouse events
class MouseEventTypes(Enum):

    EVENT_NONE = 0
    EVENT_DOWN = 1
    EVENT_UP = 2

mouseDragging = False
mouseButton = MouseButtons.BUTTON_NONE
mouseEvent = MouseEventTypes.EVENT_NONE

def get_button(mouseButton):

    for button in MouseButtons:

        if button.value == mouseButton:

            return button

    return MouseButtons.BUTTON_NONE

def handle_events():

    global mouseCords
    global mouseEvent
    global mouseButton
    global mouseDragging

    mouseCords = pygame.mouse.get_pos()
    
    for event in pygame.event.get():

        match event.type:

            # Quit events
            case pygame.QUIT:

                cUniversal.game_exit()
            
            # Keyboard input (mostly not needed)
            case pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    cUniversal.game_exit()

            # Mouse down events used for setting up mouse dragging
            case pygame.MOUSEBUTTONDOWN:

                mouseCords = event.pos
                mouseButton = get_button(event.button)
                mouseEvent = MouseEventTypes.EVENT_DOWN

                print(f"Mouse Down: {mouseCords}, button: {mouseButton.value}")
                # If the right mouse button is pressed immedietly send a mouse up event so you can't drag with it
                if (mouseButton == pygame.BUTTON_RIGHT):
                    mouseDragging = False
                    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONUP,
                                                        {"pos": mouseCords,
                                                        "button": pygame.BUTTON_RIGHT,
                                                        "touch": False}))
                    continue

                mouseDragging = True

            # Mouse up events used for actully doing stuff
            case pygame.MOUSEBUTTONUP:
                print(f"Mouse Up: {mouseCords}")

                mouseCords = event.pos
                mouseButton = get_button(event.button)
                mouseEvent = MouseEventTypes.EVENT_UP
                mouseDragging = False