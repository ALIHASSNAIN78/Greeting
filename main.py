import time
time = time.strftime("%H:%M:%S")
a = "Sir!"
print("***********Time***************")
print("Current Time: ", time)
if(time >= "00:00:00" and time <= "12:00:00"):
    print("Good Morning!", a)
elif(time > "12:00:00" and time <= "16:00:00" ): # 4pm
    print("Good Afternoon!", a)
elif(time > "16:00:00" and time <= "19:00:00"):  # 7Pm
    print("Good Evening!", a)
else:
    print("Good Night!", a)



