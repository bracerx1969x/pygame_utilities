from pygame.math import Vector2
from brycer.math import math_utilities


def calc_vector(magnitude, angle):
    return Vector2(magnitude, 0).rotate(angle)


def truncate(value, limit):
    """
    truncate function for vectors
    """
    return value if value.length() < limit.length() else limit


def at_least(value, floor):
    """
    at least function for vectors
    """
    return value if value.length() > floor.length() else floor


def clamp(value, minimum, maximum):
    """
    Clamp function for vectors
    """
    if minimum.length() < maximum.length():
        smallest = minimum
        largest = maximum
    else:
        smallest = maximum
        largest = minimum
    return truncate(at_least(value, smallest), largest)


def limit_rotation(current, desired, rotation_limit) -> Vector2:
    """
    Limit a vector angle change to within value +/- of rotatin_limit
    """
    magnitude, angle = current.as_polar()
    print(angle)
    return calc_vector(magnitude, math_utilities.clamp(angle + desired, angle - rotation_limit, angle + rotation_limit))


def compass(angle):
    return angle - 90 if angle > 90 else (angle + 270) % 360
    # return (270 - angle) % 360


def to_polar(angle):
    # convert compass bearing to polar angle
    return (angle - 270) if angle > 90 else (angle + 90)


if __name__ == '__main__':
    print()
    v1 = Vector2()
    print(to_polar(0))
