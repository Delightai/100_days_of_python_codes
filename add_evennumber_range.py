target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
target+=1
even_numbers = 0
for X in range(0,target,2):
  even_numbers += X
  X = even_numbers
print (even_numbers)