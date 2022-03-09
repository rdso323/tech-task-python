from datetime import datetime

class PlannedStart:
   def __init__(self):
      self.startTime = datetime.min
      self.count = 0

   def startTime(self):
      return self.startTime
   
   def startTime(self, startTime):
      self.startTime = startTime

   def count(self):
      return self.count
