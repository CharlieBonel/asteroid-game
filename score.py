import pygame

class Score():
    def __init__(self):
        self.total = 0

    def add_score(self):
        self.total += 1

    def create_score(self):
        font = pygame.font.SysFont("Arial", 18, bold=True, italic=False)
        text_surface = pygame.font.Font.render(font, f"Score: {self.total}", True, (255, 255, 255))
        return text_surface