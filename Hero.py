from spell_class import Spell
from weapon_class import Weapon


class Hero:
    def __init__(self, name, title, health, mana, mana_regen_rate):
        self._name = name
        self._title = title
        self._health = health
        self._mana = mana
        self._mana_regen_rate = mana_regen_rate
        self._max_health = health
        self._max_mana = mana
        self._weapon_equipped = None
        self._spell_learned = None

    def is_alive(self):
        if self._health > 0:
            return True
        return False

    def can_cast(self):
        if self._mana > 0:
            return True
        return False

    def known_as(self):
        return "{} the {}".format(self._name, self._title)

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

    def equip_weapon(self, weapon):
        self._weapon_equipped = weapon

    def learn_spell(self, spell):
        self._spell_learned = spell

    def attack(self, by="weapon"):
        if by == "weapon":
            if self._weapon_equipped is None:
                print("No weapon equiped")
                return 0
            return self._weapon_equipped.get_damage()
        if by == "spell":
            if self.can_cast:
                self._mana -= self._spell_learned.get_mana_cost()
                return self._spell_learned.get_damage()
