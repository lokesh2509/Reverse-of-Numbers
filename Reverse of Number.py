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
