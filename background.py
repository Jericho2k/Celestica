import pygame
import random
from config import WIDTH, HEIGHT, WHITE

# Наборы символов
REGULAR_STAR_SYMBOLS = ["*", ".", "'", "@"]  # Обычные символы
EMOJI_STAR_SYMBOLS = ["✨", "🌟"]  # Эмодзи

# Настраиваем шрифт для звездного фона
STAR_FONT = pygame.font.SysFont("Segoe UI Emoji", 8)  # Меньший шрифт для звезд

def generate_stars(num_stars=300, use_probability=True, num_emoji_stars=10):
    """Генерирует список случайных звезд."""
    stars = []

    if use_probability:
        # Вариант 1: Используем вероятность для эмодзи-звезд
        for _ in range(num_stars):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            # 5% вероятность для эмодзи, 95% для обычных символов
            if random.random() < 0.05:
                char = random.choice(EMOJI_STAR_SYMBOLS)
            else:
                char = random.choice(REGULAR_STAR_SYMBOLS)
            stars.append((x, y, char))
    else:
        # Вариант 2: Фиксированное количество эмодзи-звезд
        # Добавляем фиксированное число эмодзи-звезд
        for _ in range(num_emoji_stars):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            char = random.choice(EMOJI_STAR_SYMBOLS)
            stars.append((x, y, char))
        # Добавляем остальные обычные звезды
        for _ in range(num_stars - num_emoji_stars):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            char = random.choice(REGULAR_STAR_SYMBOLS)
            stars.append((x, y, char))

    return stars

def render_stars(screen, stars):
    """Отображает звезды на экране."""
    for x, y, char in stars:
        text_surface = STAR_FONT.render(char, True, WHITE)
        screen.blit(text_surface, (x, y))
