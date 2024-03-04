import unittest
from unittest import TestCase
from GunTask.Gun import Gun


class MyTestCase(unittest.TestCase):
    def test_GunIsEmpty(self):
        gun: Gun = Gun(0,'1234')
        self.assertTrue(gun.is_empty())  # add assertion here

    def test_Gun_Can_Shoot(self):
        gun: Gun = Gun(0, '1234')
        self.assertTrue(gun.is_empty())
        gun.reload_Gun()
        gun.Shoot_Gun('1234')
        self.assertEqual(4, gun.Checkammo())

    def test_Gun_Can_Reload(self):
        gun: Gun = Gun(0,'1234')
        self.assertTrue(gun.is_empty())
        gun.reload_Gun()
        self.assertFalse(gun.is_empty())

    def test_Gun_Can_ShootTwice(self):
        gun: Gun = Gun(0,"1234")
        self.assertTrue(gun.is_empty())
        gun.reload_Gun()
        gun.Shoot_Gun("1234")
        gun.Shoot_Gun('1234')
        self.assertEqual(3, gun.Checkammo())

    def test_Gun_can_shootTwice_then_Reload(self):
        gun: Gun = Gun(0,'1234')
        self.assertTrue(gun.is_empty())
        gun.reload_Gun()
        gun.Shoot_Gun('1234')
        gun.Shoot_Gun('1234')
        gun.reload_Gun()
        self.assertEqual(5,gun.Checkammo())