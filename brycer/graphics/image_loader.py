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
    """
    :param image_dict - dictionary(sequence name: list(full pathnames to each image))
    Multiple images handler for sprites
    """
    def __init__(self, image_dict, *args, **kwargs):
        self._image_dict = dict()  # dictionary of sequence name: list of images
        for sequence, image_list in image_dict.items():
            print(sequence, image_list)
            self._image_dict[sequence] = list()
            for image_path in image_dict[sequence]:
                img = load_image(image_path, -1)
                print(sequence, img)
                self._image_dict[sequence].append(img)

        if 'default' in kwargs:  # _default_seq is starting sequence name
            self._default_seq = kwargs['default']
        else:
            self._default_seq = image_dict.keys()[0]

        self._sequence = self._default_seq  # current sequence name
        self._seq_index = -1  # current index number within sequence (starts at -1 because next() increments to 0)
        self._graphic = None  # current graphic
        self.next()  # initialize to first graphic

    def get_image(self):
        if not self._graphic:
            self.next()
        return self._graphic

    def next(self):
        self._seq_index += 1
        if self._seq_index == len(self._image_dict[self._sequence]):
            self._seq_index = 0
        self._graphic = self._image_dict[self._sequence][self._seq_index]

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, name):
        if name in self._image_dict.keys():
            self._sequence = name
        else:
            raise KeyError(name)
        self._seq_index = -1
        self._graphic = None
        self.next()


class Spritesheet(AbstractImage):

    def __init__(self, *args, **kwargs):
        pass

    def get_image(self):
        pass

    def next(self):
        pass
