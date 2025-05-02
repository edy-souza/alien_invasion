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

        # Posiciona cada espaçonave nova na parte inferior central da tela.
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Flag de movimento; começa com uma espaçonave que não está se movendo.
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        ''' Atualiza a posição da espaçonave com base na flag de movimento.'''
        if self.moving_right:
            self.rect.x += 1
        
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        '''Desenha a espaçonave em sua localização atual.'''
        self.screen.blit(self.image, self.rect)