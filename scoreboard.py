import pygame.font

class Scoreboard:
    ''' Classe para exibir informações de pontuação'''
    
    def __init__(self, ai_game):
        ''' Inicializa os atributos de pontuação'''
 
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Configurações de fonte para informações de pontuação
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepara a imagem inicial de pontuação
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        
    def prep_score(self):
        ''' Transforma a pontuação em uma imagem renderizada'''
        
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.background_color)
        
        # Exibe a pontuação no canto superior direito da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        ''' Desenha a pontuação na tela '''
        
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        
    def prep_high_score(self):
        ''' Transforma a pontuação em imagem renderizada '''
        
        high_score = round(self.stats.high_score, -1)
        high_score_str = f'{high_score: ,}'
        self.high_score_image = self.font.render(high_score_str, True,
                    self.text_color, self.settings.background_color)
        
        # Centraliza a pontuação máxima na parte superior da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top    
        
    def check_high_score(self):
        ''' Verifica se há uma nova pontuação máxima'''
        
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            
    def prep_level(self):
        ''' Transforma o nível em uma imagem renderizada '''
        
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                self.text_color, self.settings.background_color)
        
        # Posiciona o nível abaixo da pontuação
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
        