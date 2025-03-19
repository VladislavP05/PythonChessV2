import pygame
from abc import ABC, abstractmethod

import src.cUniversal as cUniversal
import src.cInput as cInput

class ObjectManager():

    def __init__(self):

        self.objStatic = []
        self.objDynamic = []
        self.objNum = 0
        self.objSelected = 0

    def render_objects(self):

        self.check_mouse()

        objs = self.objStatic.copy()
        objs.extend(self.objDynamic)

        for obj in objs:
            obj.render(cUniversal.programData.screen)

    def check_mouse(self):

        # If there isn't a selected object, search through all dynamic objects to find if there is one
        if self.objSelected == 0:

            for obj in self.objDynamic:

                if obj.is_pos_inside(cInput.mouseCords):
                    obj.set_selected()
                    self.objSelected = obj
                    break

        # If there is a selected object, check if it still is selected, deselecting it if it isn't
        else:
            if not self.objSelected.is_pos_inside(cInput.mouseCords):
                self.objSelected.reset_selected()
                self.objSelected = 0
                return

        # Check if a mouse button was clicked and if there is a selected object.
        # The object should further check which button was pressed and the type of event and act as needed
        if cInput.mouseButton.value != 0 and self.objSelected != 0:
                    self.objSelected.act(self.objSelected)
                    cInput.mouseButton = cInput.MouseButtons.BUTTON_NONE
            

class Object(ABC):

    def __init__(self, position: tuple, size: tuple):

        self.objPos = position
        self.objSize = size
        self.objBoundries = pygame.Rect(position[0], position[1], size[0], size[1])
        self.enabled = 1
    
    def get_opposite_corner(self):

        return (self.objPos[0] + self.objSize[0], self.objPos[1] + self.objSize[1])

    @abstractmethod
    def render(self):
        pass

        

class Button(Object):

    def __init__(self, position: tuple, size: tuple, text: str, textColor: tuple, backgroundColor: tuple, actFunc):

        super().__init__(position, size)

        self.text = text
        self.textCol = textColor
        self.constTextCol = textColor
        self.backCol = backgroundColor
        self.constBackCol = backgroundColor
        self.act = actFunc
        
        self.selected = False
        self.clickCol = (0, 0, 0, 255)

        self.surface = pygame.Surface((self.objPos[0], self.objPos[1]), pygame.SRCALPHA)


        objManager.objDynamic.append(self)
    
    def is_pos_inside(self, pos:tuple):

        return self.objBoundries.collidepoint(pos)

    def render(self, surface: pygame.Surface):

        pygame.draw.rect(surface, self.backCol, self.objBoundries, 0)

    def set_selected(self):

        if (self.selected):
            return
        
        self.selected = True
        self.backCol = get_hover_color(self.backCol)

    def reset_selected(self):

        if (not self.selected):
            return
        
        self.selected = False
        self.backCol = self.constBackCol

    

class Text(Object):

    def __init__(self, position: tuple, size: tuple, text: str, textColor:tuple, backgroundColor: tuple):
        super().__init__(position, size)

        self.text = text
        self.textCol = textColor
        self.backCol = backgroundColor

        objManager.objStatic.append(self)

objManager = ObjectManager()

def get_hover_color(color: tuple):
    
    high = 0

    for value in color[:3]:
        high = value if value > high else high

    return (high, high, high, 255)


def act_test(self):
    if cInput.mouseEvent.value == cInput.MouseEventTypes.EVENT_UP.value:
        self.backCol = (0, 0, 0, 255)
        self.selected = False
        print("test")

def init_gui():

    Button((1000, 700), (250, 75), "aaaaa", (0, 0, 0, 255), (50, 50, 255, 255), act_test)
    Button((1000, 800), (250, 75), "aaaaa", (0, 0, 0, 255), (50, 255, 50, 255), act_test)

    pass
    