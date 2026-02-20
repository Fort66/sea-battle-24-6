from ursina import Entity, Vec3, mouse

from .class_ShipsCreater import ShipsCreater

ships_creater = ShipsCreater()

class ShipsMenu(Entity):
    """
Кравцов Никита:
добавил передачу сетки в ShipsCreater,
чтобы новые корабли создавались с доступом к полю.
"""
    def __init__(
        self,
        water=None,
        model=None,
        texture=None,
        scale=1,
        position=Vec3(0, 0, 0),
        rotation=Vec3(0, 0, 0),
        ship_counter=0,
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
        self.ship_counter = ship_counter
        self.deck_amount = deck_amount

    def input(self, key):
        if key == 'left mouse down':
            if mouse.hovered_entity == self:
                self.ship_counter -= 1

                ships_creater.model = self.model.name
                ships_creater.texture = self.texture
                ships_creater.count_deck = self.deck_amount
                ships_creater.scale = self.scale
                ships_creater.create_ship_command = True
                ships_creater.water = self.water

        if self.ship_counter <= 0:
            self.visible = False


