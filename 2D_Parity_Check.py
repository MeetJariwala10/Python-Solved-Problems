# Two-dimensional Parity check

import numpy as np

# Taking rows and columns as input from user
rows = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))

s_data = []

for i in range(rows):

    print("Row: ", (i+1))
    data = [int(x) for x in input("Enter values for rows: ").split()]
    s_data.append(data)


# Data before adding parities
sender_data = np.array(s_data)
print("\nOriginal Data: \n", sender_data)

# Calculating parities vertically
col_data = sender_data.sum(axis = 0)
row_parity = np.where(col_data % 2 == 0, 0, 1)
print("\nRow parities: ", row_parity)

# Stacks array in sequence vertically (row wise)
new_data = np.vstack([sender_data, row_parity])
print("\nRow parities added: \n", new_data)

# Calculating parities horizontally
row_data = new_data.sum(axis = 1)
col_parity = np.where(row_data % 2 == 0, 0, 1)
print("\nColumn parities: ",col_parity)

# For adding col_parity to the data vertically at last
data_to_send = np.c_[new_data, col_parity]
print("\nColumn parities added: \n", data_to_send)

# Final data to be sent
print("\nData to be sent: \n", data_to_send)
