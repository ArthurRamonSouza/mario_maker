# general setup
TILE_SIZE = 64
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
ANIMATION_SPEED = 8

# editor graphics

EDITOR_DATA = {
	0: {'style': 'player', 'type': 'object', 'menu': None, 'menu_surf': None, 'preview': None, 'graphics': 'C:/Users/arthu/python/graphics/player/idle_right'},
	1: {'style': 'sky',    'type': 'object', 'menu': None, 'menu_surf': None, 'preview': None, 'graphics': None},
	
	2: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/land.png',  'preview': 'C:/Users/arthu/python/graphics/preview/land.png',  'graphics': None},
	3: {'style': 'water',   'type': 'tile', 'menu': 'terrain', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/water.png', 'preview': 'C:/Users/arthu/python/graphics/preview/water.png', 'graphics': 'C:/Users/arthu/python/graphics/terrain/water/animation'},
	
	4: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/gold.png',    'preview': 'C:/Users/arthu/python/graphics/preview/gold.png',    'graphics': 'C:/Users/arthu/python/graphics/items/gold'},
	5: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/silver.png',  'preview': 'C:/Users/arthu/python/graphics/preview/silver.png',  'graphics': 'C:/Users/arthu/python/graphics/items/silver'},
	6: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/diamond.png', 'preview': 'C:/Users/arthu/python/graphics/preview/diamond.png', 'graphics': 'C:/Users/arthu/python/graphics/items/diamond'},

	7:  {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/spikes.png',      'preview': 'C:/Users/arthu/python/graphics/preview/spikes.png',      'graphics': 'C:/Users/arthu/python/graphics/enemies/spikes'},
	8:  {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/tooth.png',       'preview': 'C:/Users/arthu/python/graphics/preview/tooth.png',       'graphics': 'C:/Users/arthu/python/graphics/enemies/tooth/idle'},
	9:  {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/shell_left.png',  'preview': 'C:/Users/arthu/python/graphics/preview/shell_left.png',  'graphics': 'C:/Users/arthu/python/graphics/enemies/shell_left/idle'},
	10: {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/shell_right.png', 'preview': 'C:/Users/arthu/python/graphics/preview/shell_right.png', 'graphics': 'C:/Users/arthu/python/graphics/enemies/shell_right/idle'},
	
	11: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/small_fg.png', 'preview': 'C:/Users/arthu/python/graphics/preview/small_fg.png', 'graphics': 'C:/Users/arthu/python/graphics/terrain/palm/small_fg'},
	12: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/large_fg.png', 'preview': 'C:/Users/arthu/python/graphics/preview/large_fg.png', 'graphics': 'C:/Users/arthu/python/graphics/terrain/palm/large_fg'},
	13: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/left_fg.png',  'preview': 'C:/Users/arthu/python/graphics/preview/left_fg.png',  'graphics': 'C:/Users/arthu/python/graphics/terrain/palm/left_fg'},
	14: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/right_fg.png', 'preview': 'C:/Users/arthu/python/graphics/preview/right_fg.png', 'graphics': 'C:/Users/arthu/python/graphics/terrain/palm/right_fg'},

	15: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/small_bg.png', 'preview': 'C:/Users/arthu/python/graphics/preview/small_bg.png', 'graphics': 'C:/Users/arthu/python/graphics/terrain/palm/small_bg'},
	16: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/large_bg.png', 'preview': 'C:/Users/arthu/python/graphics/preview/large_bg.png', 'graphics': 'C:/Users/arthu/python/graphics/terrain/palm/large_bg'},
	17: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/left_bg.png',  'preview': 'C:/Users/arthu/python/graphics/preview/left_bg.png',  'graphics': 'C:/Users/arthu/python/graphics/terrain/palm/left_bg'},
	18: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': 'C:/Users/arthu/python/graphics/menu/right_bg.png', 'preview': 'C:/Users/arthu/python/graphics/preview/right_bg.png', 'graphics': 'C:/Users/arthu/python/graphics/terrain/palm/right_bg'},
}

NEIGHBOR_DIRECTIONS = {
	'A': (0,-1),
	'B': (1,-1),
	'C': (1,0),
	'D': (1,1),
	'E': (0,1),
	'F': (-1,1),
	'G': (-1,0),
	'H': (-1,-1)
}

LEVEL_LAYERS = {
	'clouds': 1,
	'ocean': 2,
	'bg': 3,
	'water': 4,
	'main': 5
}

# colors 
SKY_COLOR = '#ddc6a1'
SEA_COLOR = '#92a9ce'
HORIZON_COLOR = '#f5f1de'
HORIZON_TOP_COLOR = '#d1aa9d'
LINE_COLOR = 'black'