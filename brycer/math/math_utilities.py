def normalize(value, minimum, maximum):
    smallest, largest = min(minimum, maximum), max(minimum, maximum)
    return (value - smallest) / (largest - smallest)


def lerp(normalized, minimum, maximum):
    smallest, largest = min(minimum, maximum), max(minimum, maximum)
    return (largest - smallest) * normalized + smallest


def map_value(value, source_min, source_max, dest_min, dest_max):
    return lerp(normalize(value, source_min, source_max), dest_min, dest_max)


def truncate(value, limit):
    return min(value, limit)


def at_least(value, floor):
    return max(value, floor)


def clamp(value, minimum, maximum):
    smallest, largest = min(minimum, maximum), max(minimum, maximum)
    return truncate(at_least(value, smallest), largest)


def wrap(value, minimum, maximum):
    smallest, largest = min(minimum, maximum), max(minimum, maximum)
    if value < smallest:
        return largest
    if value > largest:
        return smallest
    return value


def scale_value(value, scale_factor):
    return value * scale_factor
