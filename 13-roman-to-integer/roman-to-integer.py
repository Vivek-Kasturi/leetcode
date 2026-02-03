class Solution:
   def romanToInt(self, s: str) -> int:
       digit = 0
       prev_value = 0  
 
       for letter in s:
           if letter == "I":
               value = 1
           elif letter == "V":
               value = 5
           elif letter == "X":
               value = 10
           elif letter == "L":
               value = 50
           elif letter == "C":
               value = 100
           elif letter == "D":
               value = 500
           elif letter == "M":
               value = 1000
 
           # Apply subtraction rule
           if value > prev_value:
               digit += value - 2 * prev_value
           else:
               digit += value
 
           prev_value = value  
 
       return digit