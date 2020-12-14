import os
import pygame
from abc import ABC, abstractmethod

from pygame_graphics import load_image


class AbstractImage(ABC):

    @abstractmethod
    def get_image(self):
        pass

    @abstractmethod
    def next(self):
        pass


class SingleImage(AbstractImage):

    def __init__(self, image_path, colorkey=None, *args, **kwargs):
        """
        :param path - pathname to file for graphic
        :param colorkey - pygame color key
        Creates a surface from a single image for use with sprites.
        """
        if 'return_rect' in kwargs:
            # removes return_rect keyword, just in case to prevent issue with load image
            kwargs.pop("return_rect")
        self._graphic = load_image(image_path, colorkey)

    def get_image(self):
        return self._graphic

    def next(self):
        return self._graphic


class DrawnImage(AbstractImage):
    """
    :param drawn_image - method that draws the image and returns a pygame.Surface
    :param colorkey - pygame color key
    :return Surface containing drawn image
    Creates a surface using a draw method for use with sprites.
    """
    def __init__(self, draw_method, *args, **kwargs):

        self._draw_method = draw_method
        self._graphic = None
        self.next(*args, **kwargs)

    def get_image(self):
        return self._graphic

    def next(self, *args, **kwargs):
        self._graphic = self._draw_method(*args, **kwargs)


class MultiImage(AbstractImage):

    def __init__(self, *args, **kwargs):
        pass

    def get_image(self):
        pass

    def next(self):
        pass


class Spritesheet(AbstractImage):

    def __init__(self, *args, **kwargs):
        pass

    def get_image(self):
        pass

    def next(self):
        pass
