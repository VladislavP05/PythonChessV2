import sys

sys.path.insert(0, "./src")

import pygame

import src.cInput as cInput
import src.cUniversal as cUniversal
import src.cGui as cGui

def main():
    
    pygame.init()

    cUniversal.programData.init_screen()

    pygame.display.set_caption("ChessV2")

    cGui.init_gui()

    while True:

        cInput.handle_events()
        cGui.objManager.render_objects()
        pygame.display.flip()
        cUniversal.programData.screen.fill((20, 20, 20, 255))
        pass



if __name__ == "__main__":
    main()
