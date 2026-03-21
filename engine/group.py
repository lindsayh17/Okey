"""
Evaluates 'groups' formed by tiles put together by the player testing them against rules
"""
class Group:
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
        if len(self.tiles) < 3:
            return False
        # extracting colors
        colors = []
        for tile in self.tiles:
            colors.append(tile.color)
        # ordering numbers in tile set
        numbers = []
        for tile in self.tiles:
            numbers.append(tile.number)
        numbers.sort()
        # check if all tiles are one color
        one_color = len(set(colors)) == 1

        # check for consecutive order
        consecutive_order = True
        for i in range(len(numbers) - 1):
            if numbers[i] + 1 != numbers[i + 1]:
                consecutive_order = False
                break

        return one_color and consecutive_order # returns either True or False








