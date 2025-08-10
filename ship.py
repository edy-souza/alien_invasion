import pygame
import sys

class Ship:
    '''Classe para gerenciar a nave do jogador.'''
    
    def __init__(self, ai_game):
        '''Inicializa a espaçonave e define sua posição inicial.'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
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
        
        # Armazena um float para a posição horizontal exata da espaçonave.
        self.x = float(self.rect.x)
        
        # Flag de movimento; começa com uma espaçonave que não está se movendo.
        self.moving_right = False
        self.moving_left = False
    
        # Coloca cada espaçonave nova na parte inferior central da tela.
        self.rect.midbottom = self.screen_rect.midbottom
               
    def update(self):
        ''' Atualiza a posição da espaçonave com base na flag de movimento.'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed 
            
        # Atualiza o objeto rect do self.x
        self.rect.x = self.x

    def blitme(self):
        '''Desenha a espaçonave em sua localização atual.'''
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        ''' Centraliza a espaçonave na tela '''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)