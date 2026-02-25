import arcade

from tile import TILE_WIDTH, TILE_HEIGHT


class Discard:
    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y

        # For when there are tiles to put in the deck
        # self.tiles = arcade.SpriteList()

        self.boarder = 4

    def draw(self):
        arcade.draw_lbwh_rectangle_outline(
            self.center_x - TILE_WIDTH / 2,
            self.center_y - TILE_HEIGHT / 2,
            TILE_WIDTH + self.boarder,
            TILE_HEIGHT + self.boarder,
            arcade.color.DEEP_COFFEE,
            self.boarder
        )

        # Draw tiles