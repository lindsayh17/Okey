"""
Evaluates 'groups' formed by tiles put together by the player testing them against rules
"""


class Group:
    """
    Represents a grouping of tiles and evaluates whether is a run, set, or invalid
    """
    TYPE1 = "type1" # run - same color, different number (consecutive)
    TYPE2 = "type2" # set - different color, same number (grouping)
    TYPE3 = "type3" # invalid - gets 0 points
    def __init__(self, tiles):
        self.tiles = tiles
        self.type = None
        self.points = 0

        self.evaluate()

    def evaluate(self):
        if self.is_run():
            self.type = self.TYPE1
            self.points = self.calculate_points()
        elif self.is_set():
            self.type = self.TYPE2
            self.points = self.calculate_points()
        else:
            self.type = self.TYPE3
            self.points = 0


    def is_run(self):
        """
        This function check for a run. A run is defined as those
        groups of tiles with the same color and different number
        (a consecutive run) -> 1(red), 2(red), 3(red)
        """
        if len(self.tiles) < 3:
            return False

        # extract colors
        colors = []
        for tile in self.tiles:
            colors.append(tile.color)

        # extract numbers
        numbers = []
        for tile in self.tiles:
            numbers.append(tile.number)
        # sort to account for a player's disarranged tiles -> 1, 3, 2
        numbers.sort()

        # check if all tiles are the same color
        same_color = len(set(colors)) == 1

        # check for consecutive order
        consecutive_order = True
        for i in range(len(numbers) - 1):
            if numbers[i] + 1 != numbers[i + 1]:
                consecutive_order = False
                break

        # returns either True or False
        return same_color and consecutive_order


    def is_set(self):
        """
        This function check for a set. A set is tiles of same number, but
        different color --> 1(red), 1(blue), 1(black)
        """
        if len(self.tiles) < 3:
            return False

        # extract colors
        colors = []
        for tile in self.tiles:
            colors.append(tile.color)

        # extract numbers
        numbers = []
        for tile in self.tiles:
            numbers.append(tile.number)

        # check if all tiles are the same number
        one_number = len(set(numbers)) == 1

        # check that are colors are different
        diff_colors = len(set(colors)) == len(colors)

        # returns either True or False
        return diff_colors and one_number

    def calculate_points(self):
        """
        Calculates the points if in a valid grouping
        """
        total = 0

        for tile in self.tiles:
            total = total + tile.number

        return total


