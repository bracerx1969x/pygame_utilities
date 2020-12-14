import os
import pygame

from colors_utilities import *
from pygame_graphics import *
from image_loader import *


def draw_nothing(size, colorkey):
    width, height = size
    surface = pygame.Surface((width, height))
    surface.fill(BLACK)
    surface_rect = pygame.rect.Rect(5, 5, width - 10, height - 10)
    surface_rect.center = (width // 2, height // 2)
    surface.fill(BLACK)
    pygame.draw.rect(surface, RED, surface_rect, 2)
    surface.set_colorkey(colorkey)
    return surface


class ImageFactory:
    """
    Factory class that creates images for use in sprites.
    The current version only implements single image and drawn images.
    Future versions will also implement spritesheets and multiple image.
    """
    DRAWN = "drawn"
    IMAGE = "single"
    SPRITESHEET = "spritesheet"
    MULTI_IMAGE = "multiple"

    @classmethod
    def get_handler(cls, img_type, *args, **kwargs):
        if img_type == ImageFactory.IMAGE:
            return SingleImage(*args, **kwargs)
        elif img_type == ImageFactory.DRAWN:
            return DrawnImage(*args, **kwargs)
        elif img_type == ImageFactory.SPRITESHEET:
            return Spritesheet(*args, **kwargs)
        elif img_type == ImageFactory.MULTI_IMAGE:
            return MultiImage(*args, **kwargs)
        else:
            raise ValueError(img_type)

    @classmethod
    def _single_image(cls, *args, **kwargs):
        """
        :param path - pathname to file for graphic
        :param colorkey - pygame color key
        :return Surface containing loaded image
        Creates a surface from a single image for use with sprites.
        """
        if 'return_rect' in kwargs:
            # removes return_rect keyword, just in case to prevent issue with load image
            kwargs.pop("return_rect")
        return load_image(*args, **kwargs)

    @classmethod
    def _drawn_image(cls, *args, **kwargs):
        """
        :param drawn_image - method that draws the image and returns a pygame.Surface
        :param colorkey - pygame color key
        :return Surface containing drawn image
        Creates a surface using a draw method for use with sprites.
        """
        try:
            draw_method = kwargs.pop("draw_method", '')
        except KeyError:
            raise ValueError('Missing "draw_method" method')

        return draw_method(*args, **kwargs)

    @classmethod
    def _spritesheet(cls, *args, **kwargs):
        return "spritesheet image"

    @classmethod
    def _multi_image(cls, *args, **kwargs):
        return "multiple images"


if __name__ == '__main__':
    print("testing")
    pygame.init()
    WIN_WIDTH, WIN_HEIGHT = (800, 600)
    win_display, win_rect = setup_display(WIN_WIDTH, WIN_HEIGHT, "Graphic Maker test")
    image_folder = os.path.join(os.path.normpath("C:/Users/robkw/coding/steering_tests"), "img")
    sm_asteroid_img = os.path.join(image_folder, "asteroid_med.png")

    # Examples of code that will be moved to ImprovedSprite class to make it accept various image types for sprites
    single = ImageFactory.get_handler(
                                      ImageFactory.IMAGE,
                                      image_path=sm_asteroid_img,
                                      colorkey=BLACK)
    single_image1 = single.get_image()
    single_image = pygame.transform.rotate(single_image1, -135)
    single_rect = single_image.get_rect()
    single_rect.move_ip(290, 250)

    drawn = ImageFactory.get_handler(
                                     ImageFactory.DRAWN,
                                     draw_method = draw_nothing,
                                     size=(50, 50),
                                     colorkey=-1)
    drawn_image1 = drawn.get_image()
    drawn_image = pygame.transform.rotate(drawn_image1, 75)
    drawn_rect = drawn_image.get_rect()
    drawn_rect.move_ip(600, 20)

    """
    Idea for how Multiple Images and Spritesheets will work:
    # print(ImageFactory.get_handler(ImageFactory.MULTI_IMAGE, 
                                     frame_dict={'name': (frame_path),...}, default=default_frame))
    # print(ImageFactory.get_handler(ImageFactory.SPRITESHEET, 
                                     path="spritesheet image filepath", 
                                     size=(cols, rows),
                                     colorkey="transparent color"
                                     frame_dict={'name': (set of frames),...}, default=default_frame))
    """
    clock = pygame.time.Clock()
    running = True
    angle = 0
    tock = 0
    while running:
        clock.tick(60)
        tock += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if tock % 1 == 0:
            tock = 0
            angle = (angle + 1) % 360

            single_pos = single_rect.center
            single_image = pygame.transform.rotate(single_image1, angle + 75)
            single_rect = single_image.get_rect(center = single_pos)

            drawn_pos = drawn_rect.center
            drawn_image = pygame.transform.rotate(drawn_image1, 360 - 2 * angle - 135)
            drawn_rect = drawn_image.get_rect(center = drawn_pos)

        win_display.fill(BLACK)
        win_display.blit(single_image, single_rect)
        win_display.blit(drawn_image, drawn_rect)
        pygame.display.update()

    pygame.quit()
