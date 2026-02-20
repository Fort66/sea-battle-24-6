from ursina import Entity, Vec3, mouse

from icecream import ic

class Ship(Entity):
    """
Кравцов Никита:
добавил привязку корабля к ближайшей клетке сетки,
чтобы при перетаскивании он "прилипал" к центру клетки (изменил метод update и добавил метод get_clossest_cell)
"""
    def __init__(
        self,
        water=None,
        model=None,
        texture=None,
        scale=1,
        position=Vec3(0, 0, 0),
        rotation=Vec3(0, 0, 0),
        deck_amount=0,
        **kwargs
        ):

        super().__init__(
            model=model,
            texture=texture,
            scale=scale,
            position=position,
            rotation=rotation,
            collider='box',
            **kwargs
        )

        self.water = water
        self.model = model
        self.texture = texture
        self.scale = scale
        self.position = position
        self.rotation = rotation
        self.deck_amount = deck_amount
        self.following_mouse = False

        self.is_grabbed = True
        self.is_selected = False

    def input(self, key):
        if self.is_grabbed:
            if key == 'left mouse down' and mouse.hovered_entity == self:
                self.is_selected = True
                self.following_mouse = True

            if key == 'left mouse up':
                self.is_selected = False
                self.following_mouse = False

            if key == 'right mouse down':
                if self.is_selected:
                    self.rotation += Vec3(0, 90, 0)

    def update(self):
        if self.following_mouse and mouse.world_point:
            mouse_pos = Vec3(mouse.world_point[0], 0, mouse.world_point[2])

            snapped_position = self.get_closest_cell(mouse_pos)
            if snapped_position is not None:
                self.position = snapped_position

    def get_closest_cell(self, world_pos):
        if not self.water:
            return None

        closest_pos = None
        min_dist = float('inf')

        for (col, row), cell_data in self.water.map_position_cells.items():
            cell_pos = cell_data[0]  # Vec3 центра клетки
            dist = (world_pos - cell_pos).length()

            if dist < min_dist:
                min_dist = dist
                closest_pos = cell_pos

        return closest_pos
