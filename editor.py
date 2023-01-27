import pygame, sys
from settings import *
from pygame.math import Vector2 as vector
from pygame.mouse import get_pressed as mouse_buttons
from pygame.mouse import get_pos as mouse_position
from menu import Menu


class Editor:
    def __init__(self):
        # main setup
        self.display_surface = pygame.display.get_surface()
        self.canvas_data = {} # a dictionary

        # navigation
        self.origin = vector()
        self.pan_active = False
        self.pan_offset = vector()

        # support line
        self.support_line_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.support_line_surface.set_alpha(30)
        # removes the green fill
        self.support_line_surface.set_colorkey('green')

        # selection
        self.selection_index = 2
        self.last_selected_cell = None

        # menu
        self.menu =  Menu()
        
    def get_current_cell(self):
        distance_to_origin = vector(mouse_position() - self.origin)
        
        if distance_to_origin.x > 0:
            col = int(distance_to_origin.x / TILE_SIZE)
        else:
            col = int(distance_to_origin.x / TILE_SIZE) -1

        if distance_to_origin.y > 0:
            row = int(distance_to_origin.y / TILE_SIZE)
        else:
            row = int(distance_to_origin.y / TILE_SIZE) -1

        return col, row

    # input
    def event_loop(self):
        # event loop
        # close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()   
            self.pan_input(event)
            self.selection_hotkeys(event)
            self.menu_click(event)
            self.canvas_add()

    def pan_input(self, event):

        # middle mouse button pressed or released
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_buttons()[1]:
            self.pan_active = True
            self.pan_offset = vector(mouse_position()) - self.origin

        if not mouse_buttons()[1]:
            self.pan_active = False
    
        # panning update
        if self.pan_active:
            self.origin = vector(mouse_position()) - self.pan_offset

        # mouse wheel
        if event.type == pygame.MOUSEWHEEL:
            if pygame.key.get_pressed()[pygame.K_LCTRL]:
                self.origin.y -= (event.y * 50)
            else:
                self.origin.x -= (event.y * 50)

    def selection_hotkeys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.selection_index += 1
            if event.key == pygame.K_LEFT:
                self.selection_index -= 1
            # self.selection_index must be minor than 18, and 2 must be greather than this number
            self.selection_index = max(2, min(self.selection_index, 18))
        
    def menu_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.menu.rect.collidepoint(mouse_position()):
            self.selection_index = self.menu.click(mouse_position(), mouse_buttons())

    def canvas_add(self):
        if mouse_buttons()[0] and not self.menu.rect.collidepoint(mouse_position()):
            current_cell = self.get_current_cell()

            if current_cell != self.last_selected_cell:

                if current_cell in self.canvas_data:
                    self.canvas_data[current_cell].add_id(self.selection_index)
                else:

                    self.canvas_data[current_cell] = CanvasTile(self.selection_index)
            #print(self.canvas_data)

    # drawing the grid
    def draw_tile_lines(self):
        cols = (WINDOW_WIDTH // TILE_SIZE)
        rows = (WINDOW_HEIGHT // TILE_SIZE)
    
        origin_offset = vector(
            x = self.origin.x - int(self.origin.x / TILE_SIZE) * TILE_SIZE,
            y = self.origin.y - int(self.origin.y / TILE_SIZE) * TILE_SIZE)

        self.support_line_surface.fill('green')

        for col in range(cols +1):
            x = origin_offset.x + (col * TILE_SIZE)
            pygame.draw.line(self.support_line_surface, LINE_COLOR, (x,0), (x,WINDOW_HEIGHT))

        for row in range(rows +1):
            y = origin_offset.y + (row * TILE_SIZE)
            pygame.draw.line(self.support_line_surface, LINE_COLOR, (0,y), (WINDOW_WIDTH, y))

        self.display_surface.blit(self.support_line_surface,(0,0))

    def draw_levels(self):
        for cell_pos, tile in self.canvas_data.items():
            pos = self.origin + vector(cell_pos) * TILE_SIZE

            # terrain
            if tile.has_terrain:
                test_surf = pygame.Surface((TILE_SIZE, TILE_SIZE))
                test_surf.fill('brown')
                self.display_surface.blit(test_surf, pos)

            # water
            if tile.has_water:
                test_surf = pygame.Surface((TILE_SIZE, TILE_SIZE))
                test_surf.fill('blue')
                self.display_surface.blit(test_surf, pos)

            # coins
            if tile.coin:
                test_surf = pygame.Surface((TILE_SIZE, TILE_SIZE))
                match tile.coin:
                    case 4:
                        test_surf.fill('yellow')
                    case 5:
                        test_surf.fill('grey')
                    case 6:
                        test_surf.fill('red')
                self.display_surface.blit(test_surf, pos)

            # enemies
            if tile.enemy:
                test_surf = pygame.Surface((TILE_SIZE, TILE_SIZE))
                match tile.enemy:
                    case 7:
                        test_surf.fill('black')
                    case 8:
                        test_surf.fill('black')
                    case 9:
                        test_surf.fill('black')
                    case 10:
                        test_surf.fill('black')
                self.display_surface.blit(test_surf, pos)

    def run(self, dt):
        self.event_loop()

        # drawing
        self.display_surface.fill('gray')
        self.draw_levels()
        self.draw_tile_lines()
        pygame.draw.circle(self.display_surface, 'red', self.origin, 10)
        self.menu.display(self.selection_index)

class CanvasTile:
    def __init__(self, tile_id):
         
        # terrain
        self.has_terrain = False
        self.terrain_neighbors = []

        # water
        self.has_water = False
        self.water_on_top = False

        # coin
        self.coin = None

        # enemy
        self.enemy = None

        # objects
        self.objects = []

        self.add_id(tile_id)

    def add_id(self, tile_id):
        option = {key: value['style'] for key, value in EDITOR_DATA.items()}
        match option[tile_id]:
            case 'terrain': self.has_terrain = True
            case 'water': self.has_water = True
            case 'coin': self.coin = tile_id
            case 'enemy': self.enemy = tile_id
            