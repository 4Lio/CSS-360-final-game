import pygame as pg
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = resource_path('resources/sound/')

        self.shotgun = pg.mixer.Sound(os.path.join(self.path, 'shotgun.wav'))
        self.enemy_death = pg.mixer.Sound(os.path.join(self.path, 'npc_death.wav'))
        self.enemy_hurt = pg.mixer.Sound(os.path.join(self.path, 'npc_pain.wav'))
        self.player_hurt = pg.mixer.Sound(os.path.join(self.path, 'player_pain.wav'))
        self.music = pg.mixer.music.load(os.path.join(self.path, 'the_lion_song1.wav'))
        self.player_hurt.set_volume(0.2)
        self.enemy_hurt.set_volume(0.1)
        self.enemy_death.set_volume(0.1)
        pg.mixer.music.set_volume(0.1)