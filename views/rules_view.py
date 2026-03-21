import arcade

import ui_components.button as button
import assets.colors as colr
from assets.utils import Views


class RulesView(arcade.View):
    def __init__(self, origin):
        super().__init__()

        # check original view
        self.origin = origin
        self.title_text = None
        self.exit_button = None

    def on_show_view(self):
        """ This is run once when we switch to this view """
        self.window.background_color = colr.THEME_DARK_BLUE

        title_x = self.window.width / 2
        title_y = 17 * self.window.height / 20

        button_width = self.window.width / 5
        button_height = self.window.height / 10

        arcade.load_font("assets/fonts/IrishGrover-Regular.ttf")

        # title text
        self.title_text = arcade.Text(
            "Rules",
            title_x,
            title_y,
            colr.THEME_PINK,
            font_size=self.window.height * 0.1,
            anchor_x="center",
            font_name="Irish Grover"
        )

        # play button
        self.exit_button = button.Button(title_x,
                                         self.window.height / 10,
                                         button_width,
                                         button_height,
                                         "Exit",
                                         colr.THEME_YELLOW,
                                         colr.THEME_DARK_BLUE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        self.window.default_camera.use()

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.title_text.draw()
        self.exit_button.draw()

    def on_mouse_press(self, x, y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        if self.exit_button.button_pressed(x,y):
            match self.origin:
                case Views.TITLE:
                    from views.title_view import TitleView
                    next_view = TitleView()
                # case Views.MENU:
                #     next_view = MenuView()
                # case _:
                #     next_view = MenuView()
            self.window.show_view(next_view)