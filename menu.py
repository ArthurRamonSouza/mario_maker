import pygame
from settings import *
from pygame.image import load as load


class Menu:

    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.create_data()
        self.create_buttons()
    
    def create_data(self):
        self.menu_surfaces = {}
        for key, value in EDITOR_DATA.items():
            if value['menu']:
                if not value['menu'] in self.menu_surfaces:
                    self.menu_surfaces[value['menu']] = [(key, load(value['menu_surf']))]
                else:
                    self.menu_surfaces[value['menu']].append((key, load(value['menu_surf'])))
        print(self.menu_surfaces)

    def create_buttons(self):
        
        # menu are general
        size = 180
        margin = 6
        top_left = (WINDOW_WIDTH - size - margin, WINDOW_HEIGHT - size - margin)
        self.rect = pygame.Rect(top_left, (size, size))

        # button areas
        generic_button_rect = pygame.Rect(self.rect.topleft, (self.rect.width / 2, self.rect.height / 2))
        button_margin = 5
        self.tile_button_rect = generic_button_rect.copy().inflate(-button_margin, -button_margin)
        self.coin_button_rect = generic_button_rect.move(self.rect.width / 2, 0).inflate(-button_margin, -button_margin)
        self.palm_button_rect = generic_button_rect.move(0, self.rect.height / 2).inflate(-button_margin, -button_margin)
        self.enemy_button_rect = generic_button_rect.move(self.rect.width / 2, self.rect.height / 2).inflate(-button_margin, -button_margin)

    def display(self):
        pygame.draw.rect(self.display_surface, 'red', self.rect)
        pygame.draw.rect(self.display_surface, 'green', self.tile_button_rect)
        pygame.draw.rect(self.display_surface, 'blue', self.coin_button_rect)
        pygame.draw.rect(self.display_surface, 'yellow', self.palm_button_rect)
        pygame.draw.rect(self.display_surface, 'brown', self.enemy_button_rect)
        

class Button(pygame.sprite.Sprite):
    def __init__(self, rect, group, items, items_alt = None):
        super().__init__(group)
        self.image = pygame.Surface(rect.size)
        self.rect = rect

        # itens
        self.items = {'main': items, 'alt': items_alt}
        self.idex = 0
        self.main_active = True