import arcade
from engine.tile import TILE_WIDTH, TILE_HEIGHT
from stand_slot import StandSlot, DIVIDER_GAP
from com import COM_WIDTH
from stand import Stand

class OpenStand(Stand):
    """
    Open stand with slots and tiles drawn on top
    """
    def __init__(self):
        super().__init__()
        self.slots = []
        self.open_stand_start_x = 0

    def setup(self, screen_width):
        self.slots = []

    def draw_stand(self, curr_player):
        self.open_stand_start_x = 2 * COM_WIDTH + DIVIDER_GAP + TILE_WIDTH / 2

        start_y = self.total_stand_height + TILE_HEIGHT / 2 + DIVIDER_GAP

        # Build as many rows as the player has sets in their open
        for current_set, _ in enumerate(curr_player.open_tiles):
            stand_y = start_y + current_set * (TILE_HEIGHT + 2 * DIVIDER_GAP)
            # Build as many columns as there are length of the current set +
            # 2 empty slots on either side
            for column in range(len(curr_player.open_tiles[current_set]) + 4):
                # stand_slot position
                stand_x = self.open_stand_start_x + column * TILE_WIDTH

                # create stand_slot and append to the slot list
                stand_slot = StandSlot(stand_x, stand_y, arcade.color.BLUE)
                stand_slot.holding_tile = False
                self.slots.append(stand_slot)
