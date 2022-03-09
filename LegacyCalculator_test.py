from datetime import datetime
import unittest

from LegacyCalculator import LegacyCalculator

class LegacyCalculator_test(unittest.TestCase):
   def test_empty(self):
      # arrange
      calculator = LegacyCalculator()

      # act
      result = calculator.calculate([])

      # assert
      self.assertEqual(datetime.min, result.startTime)

   def test_withOneDate(self):
      # arrange
      calculator = LegacyCalculator()
      dates = [ datetime.now() ]

      # act
      result = calculator.calculate(dates)

      # assert
      self.assertEqual(datetime.min, result.startTime)
      self.assertEqual(0, result.count)


if __name__ == '__main__':
   unittest.main()
