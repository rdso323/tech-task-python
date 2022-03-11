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

      # requiredNumberInFirstWeek = requiredDays 

      one_week = timedelta(milliseconds = 7 * 24 * 60 * 60 * 1000)
      countsForFirstWeek=0
      countsForSecondWeek=0

      startOfFirstWeek = dates[0]
      # add a week
      startOfSecondWeek = startOfFirstWeek + one_week

      # countsForFirstWeek = len([x for x in dates if x > startOfFirstWeek and x < startOfFirstWeek + timedelta(milliseconds = 7 * 24 * 60 * 60 * 1000)]) # add a week

      # countsForSecondWeek = len([x for x in dates if x > startOfSecondWeek and x < startOfSecondWeek + timedelta(milliseconds = 7 * 24 * 60 * 60 * 1000)]) # add a week

      for x in dates:
         if(x>startOfFirstWeek and x<startOfSecondWeek):
            countsForFirstWeek+=1
         elif(x>startOfSecondWeek and x<(startOfSecondWeek+one_week)):
            countsForSecondWeek+=1


      if( countsForSecondWeek > countsForFirstWeek and countsForSecondWeek >= requiredDays):
         plannedStart = PlannedStart(startOfSecondWeek, countsForSecondWeek)
      elif(countsForFirstWeek >= requiredDays):
         plannedStart = PlannedStart(startOfFirstWeek, countsForFirstWeek)


      return plannedStart
