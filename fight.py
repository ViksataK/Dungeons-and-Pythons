class Fight:
    def __init__(self, hero, enemy):
        self._hero = hero
        self._enemy = enemy
        self._s_turn = self._hero

    def battle(self):
        if self._hero.is_alive() and self._enemy.is_alive():
            pass

        elif not self._enemy.is_alive():
            pass

        elif not self._hero.is_alive():
            pass
