currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = (currentTimeInt + waitTimeInt) % 24
print(finalTimeInt)

#changed to correct variables
#such as currentTimeStr, waitTimeStr, and finalTimeInt 
#and use modulo (% 24)to ensure the result stays within a 24-hour clock
