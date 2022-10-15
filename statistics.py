
from __future__ import division

def calculateStats(numbers):
  min_val = min(numbers)
  print("MIN",min_val)
  max_val = max(numbers)
  print("MAX",max_val)
  avg = 0 if len(numbers) == 0 else sum(numbers)/len(numbers)
  print("AVG",avg)
  return {"avg" : avg,"min": min_val,"max": max_val}

#Added code 
def EmailAlert():
  return 20.5

def LEDAlert():
  return 16.5

def StatsAlerter(maxThreshold, x):
  return None
