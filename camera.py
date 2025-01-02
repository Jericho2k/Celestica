# camera.py
from config import WIDTH, HEIGHT, Z_OFFSET, SCALE

# Initial camera settings
zoom = 1.0
x_offset = 0
y_offset = 0

def project_3d_to_2d(x, y, z, scale=SCALE):
    """Projects 3D coordinates to 2D plane."""
    scale = (scale * zoom) / (Z_OFFSET + z)
    px = int(WIDTH / 2 + scale * x + x_offset)
    py = int(HEIGHT / 2 - scale * y + y_offset)
    return px, py, scale

def move_camera(dx, dy):
    """Move the camera by adjusting offsets."""
    global x_offset, y_offset
    x_offset += dx
    y_offset += dy

def zoom_camera(delta_zoom):
    """Zoom the camera in or out."""
    global zoom
    zoom += delta_zoom
    if zoom < 0.1:  # Prevent zooming too far out
        zoom = 0.1
