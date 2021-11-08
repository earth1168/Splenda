import pygame
from typing import Tuple

class Slider():
    def __init__(self, 
                position: Tuple[int, int], 
                size: Tuple[int, int],
                btn_size: Tuple[int, int],
                value, 
                max,
                min):
        self.screen = pygame.display.get_surface()  #Get background surface
        self.position = position    # slider position
        self.size = size    #slide size (width,height)
        self.hit = False    #Hit when mouse move the button
        self.btn_size = btn_size    #Button size
        self.value = value  #Start value of the slide
        self.max = max  #maximum value
        self.min = min #minimum value

        #Slider background
        pygame.draw.rect(self.screen,'White', [self.position[0],self.position[1],self.size[0],self.size[1]],3)

        #Botton surface
        pygame.draw.circle(self.screen,'Orange', self.position,self.btn_size,0)

    def update(self):
        pygame.draw.rect(self.screen, (150, 150, 150), self.sliderRect)

        if pygame.font:
            self.textDisp = self.font.render(str(self.value), 1, (50, 50, 50))

        self.textRect = self.textDisp.get_rect(centerx = self.sliderRect.x + self.sliderRect.w/2, centery = self.sliderRect.y + 11)
        self.screen.blit(self.textDisp, self.textRect)

    def onSlider(self, pos):
        x, y = pos
        if x >= self.sliderRect.x and x <= (self.sliderRect.x + self.sliderRect.w) and y >= self.sliderRect.y and y <= (self.sliderRect.y + 20):
            return True
        else:
            return False
    
    def getValue(self):
        return self.value

    def setValueByMousePos(self, pos):
        x, y = pos
        if x < self.sliderRect.x:
            self.value = 0
        elif x > (self.sliderRect.x + self.sliderRect.w):
            self.value = self.max
        else:
            self.value =  int((x - self.sliderRect.x) / float(self.sliderRect.w) * self.max)
		
    def setValueByNumber(self, value):
        self.value = value