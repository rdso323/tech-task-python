from calendar import week
from datetime import datetime, timedelta
from PlannedStart import PlannedStart

class LegacyCalculator:
   def calculate(self, dates, requiredDays = 1):
      dates.sort()

      plannedStart = PlannedStart(datetime.min, 0)
      
      # check if dates no items then return early
      if(len(dates) == 0):
         return plannedStart

      requiredNumberInFirstWeek = requiredDays

      startOfFirstWeek = dates[0]
      # add a week
      startOfSecondWeek = startOfFirstWeek + timedelta(milliseconds = 7 * 24 * 60 * 60 * 1000)

      countsForFirstWeek = len([x for x in dates if x > startOfFirstWeek and x < startOfFirstWeek + timedelta(milliseconds = 7 * 24 * 60 * 60 * 1000)]) # add a week

      countsForSecondWeek = len([x for x in dates if x > startOfSecondWeek and x < startOfSecondWeek + timedelta(milliseconds = 7 * 24 * 60 * 60 * 1000)]) # add a week

      if( countsForSecondWeek > countsForFirstWeek and countsForSecondWeek >= requiredNumberInFirstWeek):
         plannedStart = PlannedStart(startOfSecondWeek, countsForSecondWeek)

      return plannedStart
