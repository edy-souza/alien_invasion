import pygame

class Ship:
    ''' Classe para gerenciar a nave do jogador.'''
    
    def __init__ (self, ai_game):
        ''' Inicializa a espaçonave e define sua posição inicial.'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Carrega a imagem da nave e obtém seu retângulo.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
              