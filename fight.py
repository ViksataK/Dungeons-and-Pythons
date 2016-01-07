from Hero import Hero
from Enemy import Enemy
from weapon_class import Weapon


class Fight:
    def __init__(self, hero, enemy):
        self._hero = hero
        self._enemy = enemy
        self._s_turn = 0
        self.result = ['A fight has started between our hero and an enemy']

    def battle(self):
        while True:
            if self._hero.is_alive() and self._enemy.is_alive():
                if self._s_turn == 0:
                    if self._hero.can_cast():
                        self._enemy.take_damage(self._hero.attack(by='spell'))
                        self.result.append("Hero hit enemy with a spell")
                    elif not self._hero.can_cast():
                        self._enemy.take_damage(self._hero.attack())
                        self.result.append("Hero hit enemy with a weapon")
                    self._s_turn = 1
                    continue

                if self._s_turn == 1:
                    self._hero.take_damage(self._enemy.attack())
                    self.result.append(" enemy hit hero with a dmg")
                    self._s_turn = 0
                    continue

            elif not self._enemy.is_alive():
                self.result.append("Enemy is dead!")
                return str(self.result)

            elif not self._hero.is_alive():
                self.result.append("Our hero has fallen")
                return str(self.result)


def main():
    go = Hero("gosho", "loshoto", 100, 100, 2)
    gso = Enemy()
    sword = Weapon("mech", 20)
    go.equip_weapon(sword)
    bitka = Fight(go, gso)
    print(bitka.battle())

if __name__ == '__main__':
    main()
