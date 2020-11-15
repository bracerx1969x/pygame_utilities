import pygame


def load_sound(sound_path):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()

    try:
        sound = pygame.mixer.Sound(sound_path)
    except pygame.error as message:
        print('Cannot load sound:', sound_path)
        raise SystemExit(message)
    return sound
