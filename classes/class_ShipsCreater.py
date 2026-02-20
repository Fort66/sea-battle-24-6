# import aspose.threed as a3d
# scene = a3d.Scene.from_file("model.glb")
# scene.save("model.obj")

from ursina import Vec3

from .class_Ship import Ship


class ShipsCreater:
    """
Кравцов Никита:
изменил создание корабля — теперь передаю ссылку на игровую сетку (water),
чтобы корабль мог привязываться к клеткам.
"""
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.create_ship_command = False
        self.count_deck = 0
        self.model = None
        self.texture = None
        self.scale = None
        self.ships = []
        self.water = None

    def update(self):
        if self.create_ship_command:
            self.ships.append(
                Ship(
                    model=self.model,
                    texture=self.texture,
                    scale=self.scale,
                    position=Vec3(0, 0, 0),
                    rotation=Vec3(90, 90, 0),
                    deck_amount=self.count_deck,
                    water=self.water,
                )
            )
            self.create_ship_command = False
            self.count_deck = 0
            self.model = None
            self.texture = None
