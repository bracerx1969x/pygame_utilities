from pygame.math import Vector2
"""
Collection of utility functions that operate on the pygame Vector2 object
(If these were all built into the Vector2 object, it would make pygame coding easier.)
"""


def calc_vector(magnitude: [int, float], angle: [int, float]) -> Vector2:
    """
    :param magnitude - length of the new vector
    :param angle (in polar coordinates) of the new vector
    :return pygame.math.Vector2 object
    Creates a vector object with the given magnitude and angle
    """
    return Vector2(magnitude, 0).rotate(angle)


def truncate(value: Vector2, maximum: [int, float]) -> Vector2:
    """
    :param value - vector to be truncated
    :param maximum - vector length limit
    :return pygame.math.Vector2 object
    Returns a vector object that is limited a given length.
    Vector will inherit the angle of the given value vector.
    """
    if value.length() > maximum:
        value.scale_to_length(maximum)
    return value


def at_least(value: Vector2, minimum: [int, float]) -> Vector2:
    """
    :param value - vector to be truncated
    :param minimum - vector minimum length
    :return pygame.math.Vector2 object
    Returns a vector object that has at least the given length.
    Vector will inherit the angle of the given value vector.
    """
    if value.length() < minimum:
        value.scale_to_length(minimum)
    return value


def clamp(value: Vector2, minimum: [int, float], maximum: [int, float]) -> Vector2:
    """
    :param value - vector to be truncated
    :param minimum - vector minimum length
    :param maximum - vector maximum length
    :return pygame.math.Vector2 object
    Returns a vector object that is between the minimum and maximum lengths.
    Vector will inherit the angle of the given value vector.
    """
    if minimum < maximum:
        smallest, largest = minimum, maximum
    else:
        smallest, largest = maximum, minimum
    return truncate(at_least(value, smallest), largest)


def compass(angle) -> float:
    """
    :param angle - angle in polar degrees to convert to heading
    :return Returns the counter-clockwise heading angle.
    Useful for inputting into the pygame.image.transform function to get
    the image pointing in the correct direction.
    """
    return angle - 90 if angle > 90 else (angle + 270) % 360


def as_heading(vector) -> float:
    """
    :param vector
    :return pygame.math.Vector2 object
    Returns the counter-clockwise heading angle of the given vector.
    Useful for inputting into the pygame.image.transform function to get
    the image pointing in the same direction as the vector.
    """
    return (Vector2(0, 1).angle_to(vector) + 360) % 360


def to_polar(angle):
    """
    :param angle - angle in counter-clockwise compass degrees
    :return Returns the polar angle.
    """
    return (angle - 270) if angle > 90 else (angle + 90)


def as_integer(vector: Vector2):
    """
    :param vector - vector to convert
    :return Returns a rounded integer version of the vector.
    """
    _x, _y = vector.xy
    return Vector2((int(round(_x, 0)), int(round(_y, 0))))


if __name__ == '__main__':
    # testing
    print()
