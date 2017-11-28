import pyglet
import kaslide
import random
from pathlib import Path
from kaslide.projector.slide import SlideNormal
from itertools import accumulate

event_path = Path('.', 'Slideshow', 'Events')

image_suffixes = ['.png', '.jpg']


def create_event_slide(text, path: Path):
    return SlideNormal(filename=path, text=text)


def create_event_slides(path: Path):
    name = path.name
    event_slides = [SlideNormal(str(x), text=name)
                    for x in path.iterdir()
                    if x.is_file()
                    and x.suffix.lower()
                    in image_suffixes
                    ]
    random.shuffle(event_slides)
    return event_slides


def get_n_random(n, event_libs):
    distribution = list(accumulate([len(x) for x in event_libs]))
    choosen_event = random.randint(1, distribution[-1])

    i = 0
    while choosen_event > distribution[i]:
        i = i + 1

    if len(event_libs[i]) > n:
        result = event_libs[i][:n]
        event_libs[i] = event_libs[i][n:]
    else:
        result = event_libs[i]
        del event_libs[i]
    return result


def create_event_collection_slides(path: Path):
    event_libs = [create_event_slides(x) for x in path.iterdir() if x.is_dir()]

    shuffled_events = []

    while event_libs:
        shuffled_events.extend(get_n_random(10, event_libs))

    return shuffled_events


slides = create_event_collection_slides(event_path)

wheel = kaslide.projector.SlideWheel(slides)

default_img = pyglet.image.SolidColorImagePattern().create_image(800, 600)

uut = kaslide.create_slideshow(fullscreen=False, debug=False, wheel=wheel)
uut.start()
