class Hero:
    def __init__(self, health, mana, damage):
        self._health = health
        self._mana = mana
        self._max_health = health
        self._max_mana = mana

    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def take_damage(self, damage_taken):
        if damage_taken > self._health:
            self._health = 0
        else:
            self._health -= damage_taken

    def take_healing(self, healing_points):
        if self._health < 0:
            return False
        if self._health + healing_points > self._max_health:
            self._health = self._max_health
            return True
        self._health += healing_points
        return True

    def take_mana(self, mana_points):
        if self._mana + mana_points > self._max_mana:
            self._mana = self._max_mana
        else:
            self._mana += mana_points

    def equip_weapon(self):
        pass

    def learn_spell(self):
        pass

    def attack(self):
        pass

    

