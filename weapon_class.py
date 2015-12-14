class Weapon:
    def __init__(self, name, damage):
        self._name = name
        self.damage = damage

    def get_damage(self):
        return self.damage

    def get_name(self):
        return self._name
