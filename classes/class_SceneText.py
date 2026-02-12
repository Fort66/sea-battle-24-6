from ursina import Text, color

class SceneText(Text):
    # def __init__(self, text, rotation=(0, 0, 0), position=(0, 0, 0), **kwargs):
    def __init__(self, **kwargs):
        # super().__init__(
        #     text=text,
        #     color=color.white,
        #     scale=2,
        #     position=(-.75, 0, 0),
        #     rotation=(0, 0, 0)
        # )

        super().__init__(
            **kwargs
        )
