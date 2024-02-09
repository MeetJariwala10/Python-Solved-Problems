# Vertical Redundancy Check (VRC) 

import random

sender = input("\nEnter binary number (Sender's side): ")

count1 = 0

# Counting number of 1's
for i in sender:
    if (i == "1"):
        count1 += 1
  
# If count is even 0 is added else 1 is added and even parity is generated
if(count1 % 2 == 0):
    str2 = sender + "0"
    print("\nEven parity generated... ")
    
else:
    str2 = sender + "1"
    count1 += 1
    print("\nEven parity generated... ")

# Assumed data is transmitted through various networks
print("\nData Transmitted: ", str2)
    
# Corrupting data using random (Optional)
len1 = len(str2)
receiver = str2[0 : int(len1/2)] + str(random.randint(0,1)) + str2[int(len1/2 + 1) : len1]

count2 = 0

# Counting 1's in received data
for i in receiver:
    
    if(i == "1"):
        count2 += 1
        
print("Data Received: ", receiver)
        
# If even parity then data accepted else rejected
if((count2 == count1) and count2 % 2 == 0):
    print("\nEven parity -> Data Accepted")
else:
    print("\nOdd parity -> Data Rejected")
    