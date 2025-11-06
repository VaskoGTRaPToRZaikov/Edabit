def series_resistance(lst):
   result = sum(lst)
   unit = " ohm" if result <= 1 else " ohms"
   return str(result) + unit
