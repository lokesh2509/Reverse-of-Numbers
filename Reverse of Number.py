"""
The task you have to perform is “Foods and Calories.” This task consists of a total of 15 points to evaluate your performance.

Problem Statement:-
You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. You have to reserve this list of food items containing calories.

You have to use the following three methods to reserve a list:

Inbuild method of python
List name [::-1] slicing trick
Swap the first element with the last one and second element with second last one and so on like,
[6 7 8 34 5] -> [5 34 8 7 6]



Input:
Take a list as an input from the user

[5, 4, 1]

Output:
[1, 4, 5]

[1, 4, 5]

[1, 4, 5]

All three methods give the same results!
"""

food_lst = ["Pizza", "Burger", "Chowmein", "Egg Roll", "French Fries"]

a = food_lst.copy()
b = food_lst.copy()
c = food_lst.copy()

#Method 1
a.reverse()
m1 = a

#Method 2
m2 = b[::-1]

#Method 3
c[0], c[4] = c[4], c[0]
c[1], c[3] = c[3], c[1]
m3 = c

print(f"Original list is {food_lst}\n Method 1's output is {m1}\n Method 2's output is {m2}\n Method 3's output is {m3}")

if m1 == m2 == m3:
    print("All three methods give the same results!")
else:
    print("All three methods are not giving the same results!")