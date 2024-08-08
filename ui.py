from player import *
from settings import *
import pygame, random

class UI:
    def __init__(self, player):
        self.player = player
        self.display_surface = pygame.display.get_surface()
        self.font, self.bet_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE), pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.win_font =  pygame.font.Font(UI_FONT, WIN_FONT_SIZE)
        self.win_text_angle = random.randint(-4, 4)

    def dispaly_info(self):
        player_data = self.player.get_data()

        balance_surf = self.font.render("Balace: $" + player_data['balance'], True, TEXT_COLOR, None)
        x, y = 20, self.display_surface.get_size()[1] - 30
        balace_rect = balance_surf.get_rect(bottomleft = (x, y))

        bet_surf = self.font.render("Wager: $" + player_data['bet_size'], True, TEXT_COLOR, None)
        x = self.display_surface.get_size()[0] - 20
        bet_rect = bet_surf.get_rect(bottomright = (x, y))

        pygame.draw.rect(self.display_surface, False, balace_rect)
        pygame.draw.rect(self.display_surface, False, bet_rect)
        self.display_surface.blit(balance_surf, balace_rect)
        self.display_surface.blit(bet_surf, bet_rect)

        if self.player.last_payout:
            last_payout = player_data['last_payout']
            win_surf = self.win_font.render("WIN! $" + last_payout, True, TEXT_COLOR, None)
            x1 = 800
            y1 = self.display_surface.get_size()[1] - 60
            win_surf = pygame.transform.rotate(win_surf, self.win_text_angle)
            win_rect = win_surf.get_rect(center = (x1, y1))
            self.display_surface.blit(win_surf, win_rect)

    def update(self):
        pygame.draw.rect(self.display_surface, 'Black', pygame.Rect(0, 900, 1600, 100))
        self.dispaly_info()


