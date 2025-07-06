class Settings:
    '''Classe para armazenar todas as configurações do jogo.'''
    
    def __init__ (self):
        ''' Inicializa as configurações do jogo.'''
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 700
        self.background_color = (230, 230, 230)
        
        # Configurações da nave
        self.ship_speed = 1.5 
        
        # Configurações do projétil
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Configurações do alienígena
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        
        # fleet_direction de 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1