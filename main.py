from ursina import *
from ursina.prefabs.grid_editor import GridEditor  

editor = GridEditor(size=(10, 10), palette=(' ', '#'))  
matrix = editor.grid  # this is a 2D list matrix

from string import ascii_letters

from classes.class_SeaPlane import SeaPlane
from classes.class_GridOverlay import GridOverlay
from classes.class_LowerGrid import LowerGrid
from classes.class_SceneText import SceneText


from icecream import ic

sea_plane = SeaPlane()
grid_overlay = GridOverlay()
lower_grid = LowerGrid()


ic(matrix)


str_lettet_list = [ascii_letters[i] for i in range(10)]
# ic(str_lettet_list)


leters = [SceneText(
    text=symbol,
    rotation=(30, 30, 0),
    position=(-.75, 0, 0),
    scale=2
    ) for symbol in str_lettet_list]


if __name__ == "__main__":
    window.vsync = False
    app = Ursina()



    def update():
        pass


    ambient_lights = AmbientLight(color=color.white)

    # EditorCamera()
    camera.position = Vec3(0, 15, -20)
    camera.rotation = Vec3(30, 0, 0)

    app.run()

# a b c d e f g h i j