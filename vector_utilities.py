from pygame.math import Vector2
import math_utilities


def calc_vector(magnitude, angle):
    return Vector2(magnitude, 0).rotate(angle)


def truncate(value, limit):
    return value if value.length() < limit.length() else limit


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


def polar(angle):
    # return polar angle
    return


if __name__ == '__main__':
    v1_angle = 50
    v1 = calc_vector(10, v1_angle)
    v2 = limit_rotation(v1, 10, 7)
    print(v2.as_polar()[1])
    print(calc_vector(1, 57).as_polar()[1])
    v3 = Vector2((1, 0))
    v3.rotate_ip(57)
    print(v3.as_polar()[1])
    print()
    for i in range(-180, 190, 10):
        print(i, compass(i))
