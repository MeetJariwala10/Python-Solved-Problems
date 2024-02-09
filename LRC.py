# Longitudinal Redundancy Check (LRC)

import numpy as np

rows = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))

s_data = []

for i in range(rows):

    print("Row: ", (i+1))
    data = [int(x) for x in input("Enter values for rows: ").split()]
    s_data.append(data)


sender_data = np.array(s_data)

print("\nData to be sent: \n", sender_data)

r_row_data = sender_data.sum(axis = 0)

r_row = np.where(r_row_data % 2 == 0, 0, 1)

print("\nRedundant row / LRC: ", r_row)

r3 = np.vstack([sender_data, r_row])
print("\nAfter adding redundant row: \n", r3)

receiver_data = np.array([
    [1,1,0,0,1,0,1,0],
    [1,0,1,0,1,0,1,0],
    [1,1,0,0,1,1,0,0],
    [1,1,1,0,0,0,1,1],
    r_row
])

print("\nData Transmitted...")

print("\nReceived data: \n", receiver_data)

r_row_data2 = receiver_data[0 : len(receiver_data) - 1].sum(axis = 0)

r_row2 = np.where(r_row_data2 % 2 == 0, 0, 1)

print("\nRedundant row2 / LRC: ", r_row2)


if(np.array_equal(r_row, r_row2)):
    print("\nLRC at destination is equal to LRC of source... Data accepted")
else:
    print("\nLRC of destination is not equal LRC of source... Data rejected")
    