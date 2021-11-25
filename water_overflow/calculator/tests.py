from django.test import TestCase

from .glass import Glass
from .water_overflow import WaterOverflow

class CalculatorAppTest(TestCase):
    def test_glass(self):
        self.assertTrue(Glass(1, 1).is_full())
        self.assertFalse(Glass(2, 1).is_full())
        self.assertTrue(Glass(1, 2).is_full())

        self.assertEquals(Glass(2, 1).get_overfill_content(), -1)
        self.assertEquals(Glass(1, 1).get_overfill_content(), 0)
        self.assertEquals(Glass(1, 2).get_overfill_content(), 1)

    def test_water_overflow(self):
        result = WaterOverflow.get_content(1)
        self.assertEquals(result[0][0].content, 250)
        self.assertEquals(result[2][2].content, 62.5)

        result = WaterOverflow.get_content(0.1)
        self.assertEquals(result[0][0].content, 100)

    def test_water_overflow_zero_liquid_volume_input(self):
        result = WaterOverflow.get_content(0)
        self.assertIsNone(result)

    def test_water_overflow_negative_liquid_volume_input(self):
        result = WaterOverflow.get_content(-1)
        self.assertIsNone(result)

    def test_water_overflow_check_last_row_to_at_least_contain_water(self):
        result = WaterOverflow.get_content(1)
        self.assertEquals(len(result), 3)  # 3 layers

        for glass in result[len(result) - 1]:
            self.assertTrue(glass.content > 0)
