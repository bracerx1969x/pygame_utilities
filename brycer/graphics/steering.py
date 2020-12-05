import pygame
from abc import ABC
from pygame.math import Vector2
from brycer.math import vector_utilities as bry_vector


class Steering(ABC):

    def steer(self, position: Vector2, velocity: Vector2, *args, **kwargs) -> Vector2:
        pass


class Nothing(Steering):

    def steer(self, position: Vector2, velocity: Vector2, *args, **kwargs) -> Vector2:
        return Vector2(0)


class Seek(Steering):

    def steer(self, position: Vector2, velocity: Vector2, *args, **kwargs) -> Vector2:
        pass


class Accelerate(Steering):

    def steer(self, position: Vector2, velocity: Vector2, *args, **kwargs) -> Vector2:
        direction = bry_vector.compass(velocity.as_polar()[1])
        if kwargs['power']:
            return bry_vector.calc_vector(kwargs['power'], 90 - direction)


class Testing:

    def __init__(self):
        pass

    def parameters(self, *args, **kwargs):

        if 'power' in kwargs:
            print('"power" keyword used is', kwargs['power'])

        if 'super' in kwargs:
            print('"super" keyword used is:', kwargs['super'])


if __name__ == '__main__':

    test1 = Testing()
    test1.parameters(10, 5, apple="red", power="batman", super="batman")
