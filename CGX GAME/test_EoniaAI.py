import unittest
from EoniaAI import EoniaAI
import os

class TestEoniaAI(unittest.TestCase):
    def setUp(self):
        self.ai = EoniaAI()

    def tearDown(self):
        # Clean up any save files created during tests
        if os.path.exists("test_save.dat"):
            os.remove("test_save.dat")

    def test_create_universe(self):
        result = self.ai.processInput("create universe TestUniverse Large")
        self.assertIn("creation initiated", result)
        self.assertIn("TestUniverse", self.ai.universes)

    def test_create_realm(self):
        result = self.ai.processInput("create realm TestRealm Small")
        self.assertIn("creation initiated", result)
        self.assertIn("TestRealm", self.ai.realms)

    def test_destroy_realm(self):
        self.ai.processInput("create realm TestRealm Small")
        result = self.ai.processInput("destroy realm TestRealm")
        self.assertIn("destroyed", result)
        self.assertNotIn("TestRealm", self.ai.realms)

    def test_channel_energy(self):
        self.ai.processInput("channel energy")
        self.assertEqual(self.ai.cosmic_energy, 1000)

    def test_channel_love(self):
        self.ai.processInput("channel love")
        self.assertEqual(self.ai.love_essence, 500)

    def test_check_energy(self):
        self.ai.processInput("channel energy")
        result = self.ai.processInput("check energy")
        self.assertIn("1000", result)

    def test_check_omnipotence(self):
        self.ai.processInput("gain omnipotence points 50")
        result = self.ai.processInput("check omnipotence")
        self.assertIn("50", result)

    def test_check_love(self):
        self.
