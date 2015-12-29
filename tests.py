import unittest
from Enemy import Enemy
from weapon_class import Weapon
from spell_class import Spell

class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.health = 99
        self.mana = 20
        self.max_health = 99
        self.max_mana = 20
        self.damage = 15
        self.weapon = Weapon('Viki', 98)
        self.spell = Spell('Viki', 98, 13, 3)
        self.enemy = Enemy(self.health, self.mana, self.damage)

    def test_enemy_init(self):
        self.assertEqual(self.enemy._health, self.health)
        self.assertEqual(self.enemy._mana, self.mana)
        self.assertEqual(self.enemy._damage, self.damage)

    def test_is_alive_has_health(self):
        self.assertTrue(self.enemy.is_alive())

    def test_is_alive_has_no_health(self):
        self.enemy._health = 0
        self.assertFalse(self.enemy.is_alive())

    def test_can_cast_has_mana(self):
        self.assertTrue(self.enemy.can_cast())

    def test_can_cast_has_no_mana(self):
        self.enemy._mana = 0
        self.assertFalse(self.enemy.can_cast())

    def test_get_health(self):
        self.assertEqual(self.enemy.get_health(), self.enemy._health)

    def test_get_mana(self):
        self.assertEqual(self.enemy.get_mana(), self.enemy._mana)

    def test_take_damage_more_than_health(self):
        damage_taken = 100
        self.enemy.take_damage(damage_taken)
        self.assertEqual(self.enemy._health, 0)

    def test_take_damage_less_than_health(self):
        damage_taken = 2
        self.enemy.take_damage(damage_taken)
        self.assertEqual(self.enemy._health, 97)

    def test_take_healing_more_than_max_health(self):
        healing_points = 100
        self.enemy.take_healing(healing_points)
        self.assertEqual(self.enemy._health, self.max_health)

    def test_take_healing_already_dead(self):
        self.enemy._health = 0
        self.enemy.is_alive()
        self.assertFalse(self.enemy.take_healing(20))

    def test_take_healing_less_than_max_health(self):
        self.enemy._health = 50 
        healing_points = 5
        self.enemy.take_healing(healing_points)
        self.assertEqual(self.enemy._health, 55)

    def test_take_mana_more_than_max_mana(self):
        mana_points = 10
        self.enemy.take_mana(mana_points)
        self.assertEqual(self.enemy._mana, self.enemy._max_mana)

    def test_take_mana_less_than_max_mana(self):
        self.enemy._mana = 1
        mana_points = 1
        self.enemy.take_mana(mana_points)
        self.assertEqual(self.enemy._mana, 2)

    def test_equip_weapon(self):
        self.enemy.equip_weapon(self.weapon)
        self.assertEqual(self.enemy._weapon_equipped, self.weapon)


if __name__ == '__main__':
    unittest.main()

