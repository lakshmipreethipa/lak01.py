import math
class DistanceCalculator:
 def calculate_distance(x1,y1,x2,y2):
  try:
    distance = math.sqrt((x1-x2)**2+((y1-y2)**2))
  except TypeError:
   print("Error:invalid input value(s). ")
  else:
   return distance



