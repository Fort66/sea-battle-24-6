from ursina import *

from classes.class_SeaPlane import SeaPlane


sea_plane = SeaPlane()


if __name__ == "__main__":
    window.vsync = False
    app = Ursina()



    def update():
        pass


    ambient_lights = AmbientLight(color=color.white)

    EditorCamera()

    app.run()
