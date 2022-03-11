from datetime import datetime

class PlannedStart:
   def __init__(self, start_time = datetime.min, count = 0):
      self.start_time = start_time
      self.count = count

   def start_time(self):
      return self.start_time
   
   def start_time(self, start_time):
      self.start_time = start_time

   def count(self):
      return self.count

   def count(self,count):
      self.count = count
