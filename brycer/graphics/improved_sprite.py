from abc import abstractmethod
import pygame
from pygame.math import Vector2
from brycer.math import vector_utilities


class ImprovedSprite(pygame.sprite.DirtySprite):

    DEFAULT = "default"

    def __init__(self, position, bearing: int):
        super(ImprovedSprite, self).__init__()
        # inherited attributes from DirtySprite
        self.dirty = 1
        self.visible = 1
        self.blendmode = 0
        # image dictionary & graphic variables
        self._img_dict = dict()
        self._graphic = self.image = pygame.Surface((0, 0))

        # position and movement variables
        self._position = Vector2(position)
        self._bearing = bearing
        self._rotation_offset = Vector2(0)
        self._adjusted_center = Vector2(0)
        self._velocity = Vector2(0)

    def add_image(self, name=DEFAULT, img_surface: pygame.Surface = None, rotate_point = None):
        self._img_dict[name] = (img_surface.convert_alpha(), rotate_point)

    def set_image(self, name=DEFAULT):
        if self._img_dict[name]:
            self._graphic = self._img_dict[name][0]
        else:
            self._graphic = (self._img_dict[ImprovedSprite.DEFAULT])
        self._rotation_offset = Vector2(self._img_dict[name][1])

    @abstractmethod
    def move(self):
        pass

    def rotate(self, angle):
        self._bearing = (self._bearing + angle) % 360

    def redraw(self):
        self.image = pygame.transform.rotate(self._graphic, self._bearing)
        self._adjusted_center = self._rotation_offset.rotate(vector_utilities.to_polar(360 - self._bearing))
        self.rect = self.image.get_rect(center = (self._position - self._adjusted_center))
        self.dirty = 1

    @abstractmethod
    def update(self, *args, **kwargs) -> None:
        pass
