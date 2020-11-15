import pygame
import math_utilities


def calc_vector(magnitude, angle):
    vector = pygame.math.Vector2(magnitude, 0)
    vector.rotate_ip(angle)
    return vector


def truncate(value, limit):
    return value if value.length() < limit.length() else limit


def limit_rotation(value, limit) -> pygame.math.Vector2:
    """
    Limit a vector change to within value +/- limit change
    """
    magnitude, angle = value.as_polar()
    # make all angles positive for ease of check, then clamp angle between min & max
    angle += 360
    angle = math_utilities.clamp(angle, angle - limit, angle + limit) - 360
    return calc_vector(magnitude, angle)


def compass(angle):
    # return angle - 90 if angle > 90 else (angle + 270) % 360
    return (270 - angle ) % 360

def polar(angle):
    # return polar angle
    return


if __name__ == '__main__':
    print(compass(90))
