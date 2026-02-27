import arcade
import ui_components.button as button

class TitleView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show_view(self):
        """ This is run once when we switch to this view """
        self.window.background_color = (1, 22, 56)

        arcade.load_font("../assets/fonts/IrishGrover-Regular.ttf")

        self.title_text = arcade.Text(
            "Okey",
            self.window.width / 2,
            self.window.height / 2,
            (255, 107, 107),
            font_size= self.window.height * 0.25,
            anchor_x="center",
            font_name="Irish Grover"
        )

        self.play_button = button.Button(self.window.width / 3,
                             self.window.height / 3,
                             self.window.width / 6,
                             self.window.height / 11,
                             "Play",
                             (255, 107, 107),
                                         (1, 22, 56))

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        self.window.default_camera.use()

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.title_text.draw()
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        self.play_button.draw()

def main():
    """ Main function """
    window = arcade.Window(1000, 800, "Okey")
    start_view = TitleView()
    window.show_view(start_view)
    arcade.run()

if __name__ == '__main__':
    main()

