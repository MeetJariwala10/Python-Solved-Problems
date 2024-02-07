# Greedy about profit (maximum profit)
def maximum_profit(items, capacity):

    items.sort(key = lambda x : x[0], reverse = True)

    total_profit = 0
    
    for (profit, weight) in items:

        if(weight <= capacity):
            total_profit += profit
            capacity -= weight

        else:
            total_profit += (capacity / weight) * profit
            break
        
    return (total_profit)
    

# Greedy about weight (Minimum Weight)
def minimum_weight(items, capacity):

    items.sort(key = lambda x : x[1])
    
    total_profit = 0

    for (profit, weight) in items:

        if(weight <= capacity):
            total_profit += profit
            capacity -= weight

        else:
            total_profit += (capacity / weight) * profit
            break
        
    return (total_profit)


# Greedy about both (profit and weight)
def Greedy_Knapsack(items, capacity):

    items.sort(key = lambda x : x[0] / x[1], reverse = True)

    total_profit = 0

    for (profit, weight) in items:

        if(weight <= capacity):

            total_profit += profit
            capacity -= weight

        else:
            total_profit += (capacity / weight) * profit
            break

    return (total_profit)


# items = [(10, 2), (5, 3), (15, 5), (7, 7), (6, 1), (18, 4), (3, 1)]
# capacity = 15

# items = [(10, 3), (7, 2), (12, 4), (13, 3), (6, 13), (20, 8)]
# capacity = 15

items = [(25, 18), (24, 15), (15, 10)]
capacity = 20

print("Maximum profit method")
outcome1 = maximum_profit(items, capacity)
print(outcome1)

print("Minimum weight method")
outcome2 = minimum_weight(items, capacity)
print(outcome2)

print("Balance of profit and weight")
outcome = Greedy_Knapsack(items, capacity)
print(outcome)



