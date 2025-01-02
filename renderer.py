import pygame
import math
from config import WIDTH, HEIGHT, FONT, WHITE
from camera import project_3d_to_2d

def render_sphere(
    screen, radius, offset_x=0, offset_y=0, offset_z=0, chars=".", scale=200, step_theta=10, step_phi=10, full_sphere=True
):
    """ Render a sphere using ASCII characters """
    output = []
    z_buffer = [[-float('inf')] * WIDTH for _ in range(HEIGHT)]

    theta_range = range(0, 628, step_theta) if full_sphere else range(0, 314, step_theta)

    for theta in theta_range:
        for phi in range(0, 628, step_phi):
            x = radius * math.sin(theta / 100) * math.cos(phi / 100) + offset_x
            y = radius * math.sin(theta / 100) * math.sin(phi / 100) + offset_y
            z = radius * math.cos(theta / 100) + offset_z

            if z > 0:
                px, py, depth = project_3d_to_2d(x, y, z, scale)

                if 0 <= px < WIDTH and 0 <= py < HEIGHT:
                    # Calculate luminance index
                    luminance_index = int(((depth - 0.5) / 2) * len(chars))
                    luminance_index = max(0, min(len(chars) - 1, luminance_index))
                    char = chars[luminance_index]
                    if depth > z_buffer[py][px]:
                        z_buffer[py][px] = depth
                        output.append((px, py, char))

    for px, py, char in output:
        text_surface = FONT.render(char, True, WHITE)
        screen.blit(text_surface, (px, py))
