import pygame
from config import WIDTH, HEIGHT, BLACK, FPS, RADIUS, MERCURY_RADIUS, MERCURY_SCALE, MERCURY_CHARS, SCALE, WHITE
from camera import zoom_camera, move_camera
from renderer import render_sphere
from physics import calculate_mercury_position
from symbols import ASCII_CHARS, MERCURY_CHARS

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Celestica: ASCII Space")
clock = pygame.time.Clock()

# Keys state
keys = {
    "zoom_in": False,
    "zoom_out": False,
    "move_up": False,
    "move_down": False,
    "move_left": False,
    "move_right": False,
}

def main():
    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    keys["move_up"] = True
                elif event.key == pygame.K_s:
                    keys["move_down"] = True
                elif event.key == pygame.K_a:
                    keys["move_left"] = True
                elif event.key == pygame.K_d:
                    keys["move_right"] = True
                elif event.key == pygame.K_UP:
                    keys["zoom_in"] = True
                elif event.key == pygame.K_DOWN:
                    keys["zoom_out"] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    keys["move_up"] = False
                elif event.key == pygame.K_s:
                    keys["move_down"] = False
                elif event.key == pygame.K_a:
                    keys["move_left"] = False
                elif event.key == pygame.K_d:
                    keys["move_right"] = False
                elif event.key == pygame.K_UP:
                    keys["zoom_in"] = False
                elif event.key == pygame.K_DOWN:
                    keys["zoom_out"] = False

        # Adjust zoom and panning
        if keys["zoom_in"]:
            zoom_camera(0.01)
        if keys["zoom_out"]:
            zoom_camera(-0.01)
        if keys["move_up"]:
            move_camera(0, 10)
        if keys["move_down"]:
            move_camera(0, -10)
        if keys["move_left"]:
            move_camera(10, 0)
        if keys["move_right"]:
            move_camera(-10, 0)

        # Render the Sun with appropriate ASCII_CHARS and steps
        render_sphere(
            screen,
            RADIUS,
            offset_x=0,
            offset_y=0,
            offset_z=0,
            chars=ASCII_CHARS,  # Ensure correct character set is used
            scale=SCALE,
            step_theta=10,  # Adjust steps for better detail
            step_phi=10,
            full_sphere=False,
        )


        # Calculate Mercury's position
        mercury_x, mercury_y = calculate_mercury_position()

        # Render Mercury
        render_sphere(
            screen,
            MERCURY_RADIUS,
            mercury_x,
            mercury_y,
            0,
            MERCURY_CHARS,
            MERCURY_SCALE,
            step_theta=450,
            step_phi=5,
            full_sphere=True,
        )

        # Refresh screen
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
