# Imports
import arcade

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Arcade Game"
RADIUS = 150

class rickshooter(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title):