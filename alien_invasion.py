import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Classe geral para gerenciar recursos e comportamentos do jogo.'''
    
    def __init__(self):
        
        '''Inicializa o jogo e cria recursos do jogo.'''
        
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        
        self.ship = Ship(self)
        
        # Define o background da tela.
        self.background_color = self.settings.background_color
        
    def run_game(self):
        
        '''Inicia o loop princiapl do jogo.'''
        
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        ''' Responde a eventos de pressionamentos de teclas e mouse.'''
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN: # Quando uma tecla é pressionada
                self._check_keydown_events(event)
            
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        ''' Respode a teclas pressionadas'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            
    def _check_keyup_events(self, event):
        ''' Responde a teclas soltas'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
               
    def _update_screen(self):
        '''Atualiza as imagens na tela e alterna para a nova tela.'''
        
        # Redesenha a tela durante cada passagem pelo loop.
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()
                
        # Deixa a tela mais recente visível.
        pygame.display.flip()
    

if __name__ == '__main__':
    # Cria uma instância do jogo e executa o jogo.
    ai = AlienInvasion()
    ai.run_game()
