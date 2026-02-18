from ursina import Entity, Vec3, mouse

from icecream import ic

class Ship(Entity):
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
                ic(self.world_position)

            if key == 'left mouse up':
                self.is_selected = False
                self.following_mouse = False
                ic(self.world_position)

            if key == 'right mouse down':
                if self.is_selected:
                    self.rotation += Vec3(0, 90, 0)

    def update(self):
        if self.following_mouse:
            self.position = Vec3(mouse.world_point[0], 0, mouse.world_point[2])
