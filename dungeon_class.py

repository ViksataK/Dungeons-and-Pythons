class Dungeon:

    def __init__(self, path):
        self.path = path
        self.game_map = []
        self.hero = None

    def get_hero_position(self):
        for i in range(len(self.game_map)):
            for j in range(len(self.game_map[i])):
                if self.game_map[i][j] == 'H':
                    return (i, j)

    def load_content(self):
        data = open(self.path, 'r')
        return data.read()

    def set_map(self):
        content = self.load_content()
        rows = content.split('\n')
        for row in rows:
            self.game_map.append(row.split(''))
        return self.game_map

    def print_map(self):
        for row in self.game_map:
            print(''.join(row))

    def spawn(self, hero):
        for i in range(len(self.game_map)):
            for j in range(len(self.game_map[i])):
                if self.game_map[i][j] == 'S':
                    self.game_map[i][j] = 'H'
                    self.hero = hero
                    return True
        return False

    def in_map(self):
        for i in range(len(self.game_map)):
            if i >= 0 and i <= len(self.game_map):
                for j in range(len(self.game_map[i])):
                    if j >= 0 and j <= len(self.game_map[i]):
                        return True
            return False

    def move_hero(self, direction):
        if direction == 'up':
            pos = self.get_hero_position()
            if self.game_map[pos[0] - 1][pos[1]] == ".":
                self.game_map[pos[0]][pos[1]] = "."
                self.game_map[pos[0] - 1][pos[1]] = 'H'
        if direction == 'down':
            pos = self.get_hero_position()
            if self.game_map[pos[0] - 1][pos[1]] == ".":
                self.game_map[pos[0]][pos[1]] = "."
                self.game_map[pos[0] + 1][pos[1]] = 'H'
        if direction == 'left':
            pos = self.get_hero_position()
            if self.game_map[pos[0] - 1][pos[1]] == ".":
                self.game_map[pos[0]][pos[1]] = "."
                self.game_map[pos[0]][pos[1] - 1] = 'H'
        if direction == 'right':
            pos = self.get_hero_position()
            if self.game_map[pos[0] - 1][pos[1]] == ".":
                self.game_map[pos[0]][pos[1]] = "."
                self.game_map[pos[0]][pos[1] + 1] = 'H'

    def pick_treasures(self):
        pass
