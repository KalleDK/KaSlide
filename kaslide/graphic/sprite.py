from pyglet import sprite


class Sprite(sprite.Sprite):
    def __init__(self,
                 img, x=0, y=0, scale=1,
                 blend_src=sprite.GL_SRC_ALPHA,
                 blend_dest=sprite.GL_ONE_MINUS_SRC_ALPHA,
                 batch=None,
                 group=None,
                 usage='dynamic',
                 subpixel=False):
        super().__init__(img, x, y, blend_src, blend_dest, batch, group, usage, subpixel)
        self.scale = scale
