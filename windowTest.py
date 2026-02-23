import arcade
from tile import Tile, TILE_WIDTH, TILE_HEIGHT

# Game window class
class GameWindow(arcade.Window):

    def __init__(self):
        super().__init__(
            800,
            600,
            "Test Game",
            resizable=True
        )
        self.background_color = arcade.color.FOREST_GREEN

        # Sprite list goes here
        self.tile_list = arcade.SpriteList()


    # Set up game
    def setup(self):
        tile = Tile(400, 300, arcade.color.RED,7)
        self.tile_list.append(tile)


    # Screen render that clears the board
    def on_draw(self):
        self.clear()

        self.tile_list.draw()

        for tile in self.tile_list:
            # Boarder
            arcade.draw_lbwh_rectangle_outline(
                tile.center_x - TILE_WIDTH / 2,
                tile.center_y - TILE_HEIGHT / 2,
                TILE_WIDTH,
                TILE_HEIGHT,
                arcade.color.ASH_GREY,
                3
            )

            arcade.draw_text(
                str(tile.value),
                tile.center_x,
                tile.center_y,
                tile.value_color,
                40,
                anchor_x="center",
                anchor_y="center",
            )


    # When user presses a mouse button
    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    # When user releases a mouse button
    def on_mouse_release(self, x, y, button, key_modifiers):
        pass

    # When user moves the mouse
    def on_mouse_motion(self, x, y, dx, dy):
        pass

def main():
    window = GameWindow()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()

