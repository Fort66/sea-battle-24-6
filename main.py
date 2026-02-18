from ursina import *

from classes.class_ShipsCreater import ShipsCreater

from classes.create_objects import (
    my_water_area,
    my_grid_overlay,
    my_lower_grid,
    my_coordinates,
    enemy_water_area,
    enemy_grid_overlay,
    enemy_lower_grid,
    enemy_coordinates,
    nav_button
    )

from icecream import ic

ships_creater = ShipsCreater()

if __name__ == "__main__":
    window.vsync = False
    app = Ursina()


    ambient_lights = AmbientLight(color=color.white)

    camera.position = Vec3(0, 15, -22)
    camera.rotation = Vec3(35, 0, 0)

    def update():
        ships_creater.update()

        if nav_button.change_camera_position:
            if camera.position > enemy_water_area.position:
                camera.position -= Vec3(20, 0, 0) * time.dt
        else:
            if camera.position < my_water_area.position:
                camera.position += Vec3(20, 0, 0) * time.dt

    # EditorCamera()

    app.run()

# a b c d e f g h i j