from calendar import week
from datetime import datetime, timedelta
from PlannedStart import PlannedStart

class LegacyCalculator:
   def calculate(self, dates, required_days = 1):

      dates.sort()

      planned_start = PlannedStart(datetime.min, 0)
      
      # check if dates no items then return early
      if(len(dates) == 0):
         return planned_start

      # requiredNumberInFirstWeek = requiredDays 

      one_week = timedelta(milliseconds = 7 * 24 * 60 * 60 * 1000)
      counts_for_first_week=0
      counts_for_second_week=0

      start_off_first_week = dates[0]
      
      # add a week
      start_of_second_week = start_off_first_week + one_week

      # countsForFirstWeek = len([x for x in dates if x > startOfFirstWeek and x < startOfFirstWeek + timedelta(milliseconds = 7 * 24 * 60 * 60 * 1000)]) # add a week

      # countsForSecondWeek = len([x for x in dates if x > startOfSecondWeek and x < startOfSecondWeek + timedelta(milliseconds = 7 * 24 * 60 * 60 * 1000)]) # add a week

      for x in dates:
         if(x>start_off_first_week and x<start_of_second_week):
            counts_for_first_week+=1
         elif(x>start_of_second_week and x<(start_of_second_week+one_week)):
            counts_for_second_week+=1


      if( counts_for_second_week > counts_for_first_week and counts_for_second_week >= required_days):
         planned_start = PlannedStart(start_of_second_week, counts_for_second_week)
      elif(counts_for_first_week >= required_days):
         planned_start = PlannedStart(start_off_first_week, counts_for_first_week)


      return planned_start
