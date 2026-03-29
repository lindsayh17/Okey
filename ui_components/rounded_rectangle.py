import arcade

class RoundedRectangle:
    """
    Rectangle with rounded corners
    """
    def __init__(self, coords, dimensions, radius, color):
        self.center_x = coords[0]
        self.center_y = coords[1]
        self.width = dimensions[0]
        self.height = dimensions[1]
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

        bl_corner = (self.center_x - self.width / 2 + self.radius,
                     self.center_y - self.height / 2 + self.radius)
        br_corner = (self.center_x + self.width / 2 - self.radius,
                     self.center_y - self.height / 2 + self.radius)
        tl_corner = (self.center_x - self.width / 2 + self.radius,
                     self.center_y + self.height / 2 - self.radius)
        tr_corner = (self.center_x + self.width / 2 - self.radius,
                     self.center_y + self.height / 2 - self.radius)

        arcade.draw_circle_filled(bl_corner[0], bl_corner[1],
                                  self.radius, self.color)
        arcade.draw_circle_filled(br_corner[0], br_corner[1],
                                  self.radius, self.color)
        arcade.draw_circle_filled(tl_corner[0], tl_corner[1],
                                  self.radius, self.color)
        arcade.draw_circle_filled(tr_corner[0], tr_corner[1],
                                  self.radius, self.color)

    def collided_with_rect(self, x, y):
        """
        Custom function to check if collision occurred between button and mouse press

        :param x: x coordinate
        :param y: y coordinate
        :return: true if collided, false otherwise
        """

        x_true = self.center_x - self.width / 2 <= x <= self.center_x + self.width / 2
        y_true = y >= self.center_y - self.height / 2 <= y <= self.center_y + self.height / 2

        return x_true and y_true
