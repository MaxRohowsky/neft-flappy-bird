import pygame
import components
win_hieth = 620
win_width = 540
window  = pygame.display.set_mode((win_width,win_hieth))
ground = components.Ground(win_width)
pipes = []
score = components.Ui()
best_score = components.BestScore()