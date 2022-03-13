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

   def test_with_one_date(self):
      # arrange
      calculator = LegacyCalculator()
      dates = [ datetime.now() ]

      # act
      result = calculator.calculate(dates)

      # assert
      self.assertEqual(datetime.min, result.start_time)
      self.assertEqual(0, result.count)


   def test_with_many_dates_first_week(self):
      # arrange
      calculator = LegacyCalculator()
      dates = [
         datetime(2018, 1, 1),
         datetime(2018, 1, 2),
         datetime(2018, 1, 6),
         datetime(2018, 1, 11),
         datetime(2018, 1, 12)
      ]

      # act
      result = calculator.calculate(dates)

      # assert
      self.assertEqual(datetime(2018, 1, 1), result.start_time)
      self.assertEqual(2, result.count)



   def test_with_many_dates_second_week(self):
      # arrange
      calculator = LegacyCalculator()
      dates = [
         datetime(2018, 1, 1),
         datetime(2018, 1, 2),
         datetime(2018, 1, 10),
         datetime(2018, 1, 11),
         datetime(2018, 1, 12)
      ]

      # act
      result = calculator.calculate(dates)

      # assert
      self.assertEqual(datetime(2018, 1, 8), result.start_time)
      self.assertEqual(3, result.count)


   def test_with_many_dates_later(self):
      # arrange
      calculator = LegacyCalculator()
      dates = [
         datetime(2018, 1, 1),
         datetime(2018, 1, 2),
         datetime(2018, 1, 16),
         datetime(2018, 2, 2)
      ]

      # act
      result = calculator.calculate(dates)

      # assert
      self.assertEqual(datetime(2018, 1, 1), result.start_time)
      self.assertEqual(1, result.count)


   def test_required_days_not_met(self):
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
