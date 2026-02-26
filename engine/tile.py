import arcade

TILE_WIDTH = 60
TILE_HEIGHT = 100
TILE_COLORS = ["Red", "Black", "Blue", "Orange"]
TILE_SUITS = ["Circle", "Triangle", "Square", "Heart"]

class Tile(arcade.Sprite):
    def __init__(self, x, y, value, color, number, suit, is_joker=False, copy_id = 0):
        super().__init__(hit_box_algorithm="None")

        self.value = value
        self.is_face_up = False
        self.color = color
        self.number = number  # Numbers are 1 to 13
        self.suit = suit
        self.is_joker = is_joker
        self.copy_id = copy_id  # two copies of each # tile - this distinguishes duplicate tiles

        self.texture = arcade.make_soft_square_texture(
            80,
            arcade.color.ANTI_FLASH_WHITE,
            outer_alpha = 255
        )

        self.width = TILE_WIDTH
        self.height = TILE_HEIGHT

        self.center_x = x
        self.center_y = y

    def draw(self):
        # Rectangle
        arcade.draw_lbwh_rectangle_filled(
            self.center_x - TILE_WIDTH / 2,
            self.center_y - TILE_HEIGHT / 2,
            TILE_WIDTH,
            TILE_HEIGHT,
            (222, 212, 193)
        )

        if self.is_face_up:
            # Value
            arcade.draw_text(
                str(self.value),
                self.center_x,
                self.center_y + (TILE_HEIGHT / 5),
                self.value_color,
                40,
                anchor_x="center",
                anchor_y="center",
                bold=True
            )

            # Symbol
            arcade.draw_text(
                "♥",
                self.center_x,
                self.center_y - (TILE_HEIGHT / 3.5),
                self.value_color,
                15,
                anchor_x="center",
                anchor_y="center"
            )

    def set_face_down(self):
        """ Turn card face-down """
        self.is_face_up = False

    def set_face_up(self):
        """ Turn card face-up """
        self.is_face_up = True

    def is_face_up(self):
        return self.is_face_up

    def __repr__(self):
        if self.is_joker:
            return "JOKER"
        # for printing clearly
        return f"{self.color}-{self.suit}-{self.number}({self.copy_id}) of 2 copy"