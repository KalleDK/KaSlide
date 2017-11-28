import pyglet
import kaslide
import random
from pathlib import Path
from itertools import accumulate


class EventSlide(kaslide.projector.SlideFromFile):
    pass


class CommercialSlide(kaslide.projector.SlideFromFile):
    pass


def load_setting(path: Path):
    return {
        'commercials': {
            'path': Path(path, 'Slideshow', 'Reklamer'),
            'timeout': 6,
            'ratio': 7
        },

        'events': {
            'path': Path(path, 'Slideshow', 'Events'),
            'timeout': 4,
            'group_size': 10
        },

        'suffixes': ['.png', '.jpg'],

        'default': {
            'text': '',
            'image': {
                'path': Path(path, 'default.png')
            },
            'display': {
                'width': 800,
                'height': 600,
                'fullscreen': False,
                'resizable': True
            }
        },

        'debug': False
    }


def choose_random_list(list_collection):
    # Make sure that lists with many items get spread
    distribution = list(accumulate([len(x) for x in list_collection]))

    # Choose random number based on total number of items
    nr = random.randint(1, distribution[-1])

    # Return the event index
    i = 0
    while nr > distribution[i]:
        i = i + 1

    return i


def get_n_items_from_single_list(n, list_collection):
    i = choose_random_list(list_collection)

    # Slicing selects n or less if there is not enough
    items = list_collection[i][:n]

    # Removing the selected items
    list_collection[i] = list_collection[i][n:]

    return items


def create_slides_from_single_event(path: Path, valid_suffixes):
    name = path.name
    event_slides = [EventSlide(x, text=name)
                    for x in path.iterdir()
                    if x.is_file()
                    and x.suffix.lower()
                    in valid_suffixes
                    ]
    random.shuffle(event_slides)
    return event_slides


def create_event_slides(path: Path, valid_suffixes, group_size):
    event_collection = [create_slides_from_single_event(x, valid_suffixes) for x in path.iterdir() if x.is_dir()]

    merged_events = []

    while any(slides for slides in event_collection):
        merged_events.extend(get_n_items_from_single_list(group_size, event_collection))

    return merged_events


def create_commercials_slides(path: Path, valid_suffixes):
    commercial_slides = [CommercialSlide(path=x, text="")
                         for x in path.iterdir()
                         if x.is_file()
                         and x.suffix.lower()
                         in valid_suffixes
                         ]

    return commercial_slides


def merge_slides(event_slides, commercial_slides, ratio):
    merged_slides = []
    shuffled_commercials = []

    while event_slides:
        if not shuffled_commercials:
            shuffled_commercials = commercial_slides
            random.shuffle(shuffled_commercials)
        merged_slides.extend(event_slides[:ratio])
        event_slides = event_slides[ratio:]
        merged_slides.extend(shuffled_commercials[:1])
        shuffled_commercials = shuffled_commercials[1:]

    return merged_slides


def create_projector_wheel(event_path, commercial_path, valid_suffixes, group_size, ratio):
    # Getting all slides from events
    event_slides = create_event_slides(event_path, valid_suffixes, group_size)

    # Getting all slides from commercials
    commercial_slides = create_commercials_slides(commercial_path, valid_suffixes)

    # Merges slides with the given ratio - one commercial per ratio events
    slides = merge_slides(event_slides, commercial_slides, ratio)

    # Create the wheel
    wheel = kaslide.create_wheel(slides)

    return wheel


def create_plane(width, height):
    return kaslide.create_plane(width=width, height=height)


def create_projector(settings):
    default_image = kaslide.graphic.Image(
        path=settings['default']['image']['path']
    )

    wheel = create_projector_wheel(
        event_path=settings['events']['path'],
        commercial_path=settings['commercials']['path'],
        valid_suffixes=settings['suffixes'],
        group_size=settings['events']['group_size'],
        ratio=settings['commercials']['ratio']
    )

    plane = create_plane(
        width=settings['default']['display']['width'],
        height=settings['default']['display']['height']
    )

    return kaslide.create_projector(
        default_image=default_image,
        default_text=settings['default']['text'],
        fullscreen=settings['default']['display']['fullscreen'],
        resizable=settings['default']['display']['resizable'],
        debug=settings['debug'],
        wheel=wheel,
        plane=plane
    )


class Slideshow:
    def __init__(self, settings):
        CommercialSlide.timeout = settings['commercials']['timeout']
        EventSlide.timeout = settings['events']['timeout']
        self.projector = create_projector(settings)

    def start(self):
        self.projector.start()
        pyglet.app.run()


def zoom_to_plane(sprite, plane):
    scale = max(plane.width / sprite.image.width, plane.height / sprite.image.height)

    x = (plane.width - (sprite.image.width * scale)) / 2
    y = (plane.height - (sprite.image.height * scale)) / 2

    sprite.update(x=x, y=y, scale=scale)
    return True


app = Slideshow(settings=load_setting(Path('.')))
#app.projector.display._picture.push_handlers(on_sprite_resize=zoom_to_plane)
app.start()
