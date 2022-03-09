from datetime import datetime

class PlannedStart:
   def __init__(self):
      self.startTime = datetime.min

   def startTime(self):
      return self.startTime
   
   def startTime(self, startTime):
      self.startTime = startTime
