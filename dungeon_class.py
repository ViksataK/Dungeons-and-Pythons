class Dungeon:

    def __init__(self, path):
        self.path = path
        self.game_map = []
        self.hero = None

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
        for i in self.game_map:
            for j in self.game_map[i]:
                if self.game_map[i][j] == 'S':
                    self.game_map[i][j] = 'H'
                    self.hero = hero
                    return True
        return False

    def in_map(slef):
        pass

    def move_hero(self, derection):
        pass

    def pick_treasures(self):
        pass
