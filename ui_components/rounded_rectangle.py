import arcade

class RoundedRectangle():
    def __init__(self, x, y, width, height, radius, color):
        self.center_x = x
        self.center_y = y
        self.width = width
        self.height = height
        self.color = color
        self.radius = radius

    def draw(self):
        # horizontal rectangle
        arcade.draw_rect_filled(
            arcade.rect.XYWH(self.center_x,
            self.center_y,
            self.width - 2 * self.radius,
            self.height),
            self.color
        )

        arcade.draw_rect_filled(
            arcade.rect.XYWH(self.center_x,
            self.center_y,
            self.width,
            self.height - 2 * self.radius),
            self.color
        )

        bl_corner = (self.center_x - self.width / 2 + self.radius, self.center_y - self.height / 2 + self.radius)
        br_corner = (self.center_x + self.width / 2 - self.radius, self.center_y - self.height / 2 + self.radius)
        tl_corner = (self.center_x - self.width / 2 + self.radius, self.center_y + self.height / 2 - self.radius)
        tr_corner = (self.center_x + self.width / 2 - self.radius, self.center_y + self.height / 2 - self.radius)

        arcade.draw_circle_filled(bl_corner[0], bl_corner[1], self.radius, self.color)
        arcade.draw_circle_filled(br_corner[0], br_corner[1], self.radius, self.color)
        arcade.draw_circle_filled(tl_corner[0], tl_corner[1], self.radius, self.color)
        arcade.draw_circle_filled(tr_corner[0], tr_corner[1], self.radius, self.color)