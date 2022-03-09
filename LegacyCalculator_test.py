import datetime
import unittest

from LegacyCalculator import LegacyCalculator

class LegacyCalculator_test(unittest.TestCase):
   def test_empty(self):
      # arrange
      calculator = LegacyCalculator()

      # act
      dates = []
      print(dates)
      calculator.calculate(dates)
      result = calculator.calculate(dates)

      # assert
      self.assertEqual(datetime.datetime.min, result.startTime())


if __name__ == '__main__':
   unittest.main()
