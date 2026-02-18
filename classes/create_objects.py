from ursina import Vec3, color

from .class_SeaPlane import SeaPlane
from .class_GridOverlay import GridOverlay
from .class_CoordinateText import CoordinateText
from .class_NavButton import NavButton
from .class_ShipsMenu import ShipsMenu



my_water_area = SeaPlane()
my_grid_overlay = GridOverlay(10, 10, position=Vec3(0, .002, 0))
my_lower_grid = GridOverlay(12, 12, color=color.rgba(0, 0, 0, 0), position=Vec3(0, -.002, 0))

my_coordinates = CoordinateText(my_lower_grid)


enemy_water_area = SeaPlane(position=Vec3(-18, 0, 0))
enemy_grid_overlay = GridOverlay(10, 10, position=Vec3(-18, .002, 0))
enemy_lower_grid = GridOverlay(12, 12, color=color.rgba(0, 0, 0, 0), position=Vec3(-18, -.002, 0))

enemy_coordinates = CoordinateText(enemy_lower_grid)

nav_button = NavButton(position=(-1, .4, 0))

four_deck_menu = ShipsMenu(
    model='assets/models/newport/newport.glb',
    scale=.011,
    position=Vec3(8, .2, 5),
    rotation=Vec3(90, 90, 0),
    ship_counter=1,
    deck_amount=4
)

three_deck_menu = ShipsMenu(
    model='assets/models/newport/newport.glb',
    scale=.011,
    position=Vec3(8, .2, 5),
    rotation=Vec3(90, 90, 0),
    ship_counter=1,
    deck_amount=4
)

two_deck_menu = ShipsMenu(
    model='assets/models/newport/newport.glb',
    scale=.011,
    position=Vec3(8, .2, 5),
    rotation=Vec3(90, 90, 0),
    ship_counter=1,
    deck_amount=4
)

one_deck_menu = ShipsMenu(
    model='assets/models/newport/newport.glb',
    scale=.011,
    position=Vec3(8, .2, 5),
    rotation=Vec3(90, 90, 0),
    ship_counter=1,
    deck_amount=4
)