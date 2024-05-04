from queue import Full
import pygame
import random

class Ground:
    ground_level = 500

    def __init__(self, win_width):
        self.x, self.y = 0, Ground.ground_level
        self.rect = pygame.Rect(self.x, self.y, win_width, 5)

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), self.rect)


class BestScore:
    _value = 0
    main_score = 0
    def __init__(self):
        pygame.font.init()
        self.x = 330
        self.y = 11
        self.width = 135
        self.height = 40
        self.font = pygame.font.Font(None, 36)  # You can adjust the font size and style here
        self.text = "Best: 0"   # Example text
        self.rendered_text = self.font.render(self.text, True, (255, 255, 255))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        pygame.draw.rect(window, (117, 25, 145), self.rect, 0, 3)
        window.blit(self.rendered_text, (self.x + 10, self.y + 10))  # Adjust text position as needed

    def update(self,value):
        if(value >= self._value):
            self._value = value
            self.rendered_text = self.font.render("best: "+str(value), True, (255, 255, 255))
        else:
            self.rendered_text = self.font.render("best: "+str(self._value), True, (255, 255, 255))
           

        
class Ui:
    _score = 0
    def __init__(self):
        pygame.font.init()
        self.x = 170
        self.y = 11
        self.width = 140
        self.height = 40
        self.font = pygame.font.Font(None, 36)  # You can adjust the font size and style here
        self.text = "Score: 0"   # Example text
        self.rendered_text = self.font.render(self.text, True, (255, 255, 255))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        

    def draw(self, window):
        pygame.draw.rect(window, (117, 25, 145), self.rect, 0, 3)
        window.blit(self.rendered_text, (self.x + 10, self.y + 10))  # Adjust text position as needed  

    def update(self):
        self._score = self._score  + 0.01     
        self.text = "Score: "+str(round(self._score,1) ) 
        self.rendered_text = self.font.render(self.text, True, (255, 255, 255))
        print(self.text)

    def reset(self):
        self._score = 0
        self.rendered_text = self.font.render(self.text, True, (255, 255, 255))

class Pipes:
    width = 15
    opening = 100

    def __init__(self, win_width):
        self.x = win_width
        self.bottom_height = random.randint(10, 300)
        self.top_height = Ground.ground_level - self.bottom_height - self.opening
        self.bottom_rect, self.top_rect = pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0)
        self.passed = False
        self.off_screen = False

    def draw(self, window):
        self.bottom_rect = pygame.Rect(self.x, Ground.ground_level - self.bottom_height, self.width, self.bottom_height)
        pygame.draw.rect(window, (0, 128, 0), self.bottom_rect)

        self.top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
        pygame.draw.rect(window, (0, 128, 0), self.top_rect)

    def update(self):
     
        self.x -= 1
        if self.x + Pipes.width <= 50:
            self.passed = True
        if self.x <= -self.width:
            self.off_screen = True