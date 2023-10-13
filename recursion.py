import sys
# Countdown function 
def countdown(n):
 if n <= 0:
    print('Blastoff!')
 else:
    print(n)
    countdown(n-1)
# Count up function
def countup(n):
  if n == 0:
    print("Blastoff!")
  else:
    print(n)
    countup(n+1)

# Getting input
number = input("Give a number for counting!")
# Making sure it is an int
try:
  number = int(number)
except ValueError:
  sys.exit("Enter an integer the next time!!!!!!")
else:
    # if positive executing countdown.Otherwise, countdown!
    if number > 0:
        countdown(number)
    else:
        countup(number)

