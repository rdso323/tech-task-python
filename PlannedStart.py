from datetime import datetime

class PlannedStart:
   def __init__(self, startTime = datetime.min, count = 0):
      self.startTime = startTime
      self.count = count

   def startTime(self):
      return self.startTime
   
   def startTime(self, startTime):
      self.startTime = startTime

   def count(self):
      return self.count
