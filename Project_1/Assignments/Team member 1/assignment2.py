import random
import time
while True:
    temperature=random.randrange(20, 40)
    humidity=random.randrange(50,70)
    print("Temperature is : ",temperature," C ")
    if(temperature>30):
        print("High temperature is detected..")
    time.sleep(2)
