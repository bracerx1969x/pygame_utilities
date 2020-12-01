import pygame


def load_image(image_path, colorkey=None, return_rect=False):
    try:
        image = pygame.image.load(image_path)
    except pygame.error as message:
        print('Cannot load image:', image_path)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    if return_rect:
        return image, image.get_rect()
    return image


def setup_display(win_width, win_height, caption = None):
    window = pygame.display.set_mode((win_width, win_height))
    if caption:
        pygame.display.set_caption(caption)
    return window, window.get_rect()


def _build_frame_store(image, frame_layout, color_key: pygame.Color = False):
    frame_columns, frame_rows = frame_layout
    image_width, image_height = image.get_size()
    frame_width, frame_height = (image_width // frame_columns, image_height // frame_rows)
    frame_store = list()
    for frame_row in range(frame_rows):
        for frame_col in range(frame_columns):
            frame_surf = pygame.Surface((frame_width, frame_height)).convert_alpha()
            if color_key:
                frame_surf.set_colorkey(color_key)
            frame_surf.blit(image, (0, 0),
                            pygame.Rect(frame_col * frame_width,
                                        frame_row * frame_height,
                                        frame_width,
                                        frame_height))
            frame_store.append(frame_surf.copy())
    return frame_store


def build_spritesheet(image, frame_layout, color_key):
    store = _build_frame_store(image, frame_layout, color_key)
    anim_library = dict()
    anim_library['all'] = [n for n in range(frame_layout[0] * frame_layout[1])]
    return store, anim_library


def draw_cross(surface, crosspoint, line_color, line_width, horizontal=True, vertical=True):
    surface_rect = surface.get_rect()
    point = pygame.math.Vector2(crosspoint)
    if horizontal:
        pygame.draw.line(
                         surface,
                         line_color,
                         (surface_rect.left, point.y),
                         (surface_rect.right, point.y),
                         line_width
                        )
    if vertical:
        pygame.draw.line(
                         surface,
                         line_color,
                         (point.x, surface_rect.top),
                         (point.x, surface_rect.bottom),
                         line_width
                        )
