""" a simplified version of how mapreduce works for horizontal scaling"""

from functools import reduce

my_list = [1,2,3,4]

computer1_list = [1,2]
computer2_list = [2,4]

# to find sum of squared values, first we square everything, then we add together. 



#Traditional way to find some of squared values

ssv_trad = sum(i**2 for i in my_list)  # ssv_trad == 30

#MapReduce way. 

cp_1_squared_values = map(
    lambda i: i**2, computer1_list)

cp_2_squared_values = map(
    lambda i: i**2, computer2_list)

def add_number(x1, x2):
    return x1 + x2

ssv_mapreduce = reduce(add_number, [cp_1_squared_values, cp_2_squared_values])
print("Sum of squared values (trad): {}".format(ssv_trad)