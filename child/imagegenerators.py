from imagekit import ImageSpec, register
from pilkit.processors import ResizeToFill


class Thumbnail(ImageSpec):
    processors = [ResizeToFill(100, 100)]
    format = 'JPEG'
    options = {'quality': 80}

register.generator('child:thumbnail', Thumbnail)