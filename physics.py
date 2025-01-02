import math
from config import MERCURY_DISTANCE, MERCURY_SPEED

# Initial Mercury angle
mercury_angle = 0

def calculate_mercury_position():
    """ Calculate Mercury's current position in its orbit """
    global mercury_angle
    mercury_x = MERCURY_DISTANCE * math.cos(mercury_angle)
    mercury_y = MERCURY_DISTANCE * math.sin(mercury_angle)
    mercury_angle += MERCURY_SPEED
    return mercury_x, mercury_y
