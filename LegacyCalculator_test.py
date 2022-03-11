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
      self.assertEqual(datetime.min, result.start_time)
      self.assertEqual(0, result.count)

   def test_withOneDate(self):
      # arrange
      calculator = LegacyCalculator()
      dates = [ datetime.now() ]

      # act
      result = calculator.calculate(dates)

      # assert
      self.assertEqual(datetime.min, result.start_time)
      self.assertEqual(0, result.count)

   def test_withManyDates_secondWeek(self):
      # arrange
      calculator = LegacyCalculator()
      dates = [
         datetime(2018, 1, 1),
         datetime(2018, 1, 2),
         datetime(2018, 1, 10),
         datetime(2018, 1, 11),
         datetime(2018, 1, 12),
      ]

      # act
      result = calculator.calculate(dates)

      # assert
      self.assertEqual(datetime(2018, 1, 8), result.start_time)
      self.assertEqual(3, result.count)


   def test_withManyDates_firstWeek(self):
      # arrange
      calculator = LegacyCalculator()
      dates = [
         datetime(2018, 1, 1),
         datetime(2018, 1, 2),
         datetime(2018, 1, 6),
         datetime(2018, 1, 11),
         datetime(2018, 1, 12),
      ]

      # act
      result = calculator.calculate(dates)

      # assert
      self.assertEqual(datetime(2018, 1, 1), result.start_time)
      self.assertEqual(2, result.count)


   def test_requiredDaysNotMet(self):
      # arrange
      calculator = LegacyCalculator()
      dates = [
         datetime(2018, 1, 1),
         datetime(2018, 1, 2),
         datetime(2018, 1, 6),
         datetime(2018, 1, 11),
         datetime(2018, 1, 12),
      ]

      # act
      result = calculator.calculate(dates,3)

      # assert
      self.assertEqual(datetime.min, result.start_time)
      self.assertEqual(0, result.count)

if __name__ == '__main__':
   unittest.main()
