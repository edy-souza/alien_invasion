import pygame
import sys

class Ship:
    '''Classe para gerenciar a nave do jogador.'''
    
    def __init__(self, ai_game):
        '''Inicializa a espaçonave e define sua posição inicial.'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Tenta carregar a imagem da nave.
        try:
            self.image = pygame.image.load('images/ship.bmp')
            print("Imagem da nave carregada com sucesso!")  # Depuração
        except pygame.error as e:
            print(f"Erro ao carregar a imagem da nave: {e}")
            sys.exit()

        self.rect = self.image.get_rect()

        # Começa cada espaçonave nova no centro inferior da tela.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Desenha a espaçonave em sua localização atual.'''
        self.screen.blit(self.image, self.rect)