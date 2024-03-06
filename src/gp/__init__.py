from . import color as _color
from . import motion as _motion

__all__ = [
    "color",
    "motion",
]


def _init_color() -> _color.GpColor:
    global color
    color = _color.GpColor()  # TODO: set cached pins
    return color


def _init_motion() -> _motion.GpMotion:
    global motion
    motion = _motion.GpMotion()  # TODO: set cached pin
    return motion


color: _color.GpColor = _init_color()
motion: _motion.GpMotion = _init_motion()
