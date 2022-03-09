import datetime

from PlannedStart import PlannedStart


class LegacyCalculator:
   def __init__(self) -> None:
      pass

   def calculate(self, dates):
      dates.sort()
      return PlannedStart()
