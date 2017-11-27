from pathlib import Path
from kaslide.projector.slide import SlideNormal

event_path = Path('.', 'Slideshow', 'Events', 'Reklamer')


def create_event_slide(text, path: Path):
    return SlideNormal(filename=path, text=text)


def create_event_slides(path: Path):
    name = path.name
    return [SlideNormal(str(x), text=name) for x in path.iterdir() if x.is_file()]

print(create_event_slides(event_path))


