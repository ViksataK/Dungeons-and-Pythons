import unittest
from Hero import Hero
from weapon_class import Weapon
from spell_class import Spell


class TestHero(unittest.TestCase):
    def setUp(self):
        self.name = 'Rado'
        self.title = 'RadoRado'
        self.health = 70
        self.mana = 80
        self.mana_regen_rate = 15
        self.hero = Hero(
            self.name, self.title, self.health,
            self.mana, self.mana_regen_rate
        )
        self.spell = Spell('Kodene', 23, 30, 2)
        self.weapon = Weapon('AXE', 23)

    def test_init(self):
        self.assertEqual(self.name, self.hero._name)
        self.assertEqual(self.title, self.hero._title)
        self.assertEqual(self.health, self.hero._health)
        self.assertEqual(self.mana, self.hero._mana)
        self.assertEqual(self.mana_regen_rate, self.hero._mana_regen_rate)
        self.assertEqual(self.health, self.hero._max_health)
        self.assertEqual(self.mana, self.hero._max_mana)
        self.assertEqual(None, self.hero._weapon_equipped)
        self.assertEqual(None, self.hero._spell_learned)

    def test_is_alive(self):
        self.assertTrue(self.hero.is_alive())
        self.hero._health = 0
        self.assertFalse(self.hero.is_alive())
        self.hero._health = -10
        self.assertFalse(self.hero.is_alive())

    def test_learn_spell(self):
        self.hero.learn_spell(self.spell)
        self.assertEqual(self.hero._spell_learned, self.spell)

    def test_equip_weapon(self):
        self.hero.equip_weapon(self.weapon)

    def test_can_cast(self):
        self.assertFalse(self.hero.can_cast())
        self.hero._mana = 10
        self.hero._spell_learned = self.spell
        self.assertFalse(self.hero.can_cast())
        self.hero._mana = self.hero._max_mana
        self.assertTrue(self.hero.can_cast())

    def test_known_as(self):
        self.assertEqual(
            self.hero.known_as(),
            'Rado the RadoRado'
        )

    def test_get_health(self):
        self.assertEqual(self.hero.get_health(), self.hero._health)

    def test_get_mana(self):
        self.assertEqual(self.hero.get_mana(), self.hero._mana)

    def test_take_damage(self):
        damage = 30
        health = self.hero._health
        self.hero.take_damage(damage)
        self.assertEqual(self.hero._health, health - damage)
        self.hero.take_damage(9000)
        self.assertEqual(self.hero._health, 0)

    def test_take_healing(self):
        self.hero._health = 0
        self.assertFalse(self.hero.take_healing(10))
        self.hero._health = self.hero._max_health
        self.assertTrue(self.hero.take_healing(10))
        self.assertEqual(self.hero._health, self.hero._max_health)
        health = 10
        healing = 20
        self.hero._health = health
        self.hero._max_health = health + healing * 2
        self.assertTrue(self.hero.take_healing(healing))
        self.assertEqual(self.hero._health, healing + health)

    def test_take_mana(self):
        self.hero._mana = 0
        init = self.hero._mana
        mana = 10
        a_lot_mana = 9000
        self.hero.take_mana(mana)
        self.assertEqual(self.hero._mana, init + mana)
        self.hero.take_mana(a_lot_mana)
        self.assertEqual(self.hero._mana, self.hero._max_mana)

    def test_attack(self):
        self.hero._weapon_equipped = None
        self.assertEqual(self.hero.attack(), 0)
        self.hero.equip_weapon(self.weapon)
        self.assertEqual(self.hero.attack(), self.weapon.get_damage())
        self.assertEqual(self.hero.attack('spell'), 0)
        self.hero.learn_spell(self.spell)
        self.assertEqual(self.hero.attack('spell'), self.spell.get_damage())
        self.hero._mana = 0
        self.assertEqual(self.hero.attack('spell'), 0)


if __name__ == '__main__':
    unittest.main()
