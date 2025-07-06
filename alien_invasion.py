import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    '''Classe geral para gerenciar recursos e comportamentos do jogo.'''
    
    def __init__(self):
        
        '''Inicializa o jogo e cria recursos do jogo.'''
        
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()       
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
        # Define o background da tela.
        self.background_color = self.settings.background_color
        
    def run_game(self):
        
        '''Inicia o loop princiapl do jogo.'''
        
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
        
        elif event.key == pygame.K_q:
            sys.exit()
        
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        ''' Responde a teclas soltas'''
        
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        ''' Cria um novo projétil e o adiciona ao grupo de projéteis '''
        
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
            
                  
    def _update_screen(self):
        '''Atualiza as imagens na tela e alterna para a nova tela.'''
        
        # Redesenha a tela durante cada passagem pelo loop.
        self.screen.fill(self.settings.background_color)
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.ship.blitme()
        self.aliens.draw(self.screen)
                
        # Deixa a tela mais recente visível.
        pygame.display.flip()
        
    def _update_aliens(self):
        ''' Verifica se a frota está na borda e, em seguida, atualiza as posições '''
        
        self._check_fleet_edges()
        self.aliens.update()
        
    def _fire_bullet(self):
        ''' Cria um novo projétil e o adiciona ao grupo de projéteis'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        ''' Atualiza a posição dos projéteis e descarta os projéteis antigos'''
        # Atualiza a posição dos projéteis
        self.bullets.update()
        
        # Descarta os projeties que desapareceram
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                
    def _create_fleet(self):
        ''' Cria uma frota de alienígenas'''
        
        # Cria um alienígena e continua adicionando alienígenas
        # até que não haja mais espaço
        # O distanciamento entre alienígenas é a largura de um alienígena
        alien = Alien(self)  
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            # Termina uma fileira; redefine o valor de x, e incrementa o valor de y
            current_x = alien_width
            current_y += 2 * alien_height
        
        current_x = alien_width
        while current_x < (self.settings.screen_width - 25 * alien_width):
            self._create_alien(current_x, current_y)
            current_x += 2 * alien_width
            
    def _create_alien(self, x_position, y_position):
        ''' Cria um alienígena e o posiciona na fileira'''
        
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)  
        
    def _check_fleet_edges(self):
        ''' Responde apropriadamente se algum alienígena alcançou uma borda '''     
        
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break    

    def _change_fleet_direction(self):
        ''' Faz toda a frota descer e mudar de direção '''
        
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
if __name__ == '__main__':
    # Cria uma instância do jogo e executa o jogo.
    ai = AlienInvasion()
    ai.run_game()
