def create_tuple(list_of_nums):
    # Create a tuple from a list and return it.
    tup_of_nums = tuple(list_of_nums)
    return tup_of_nums


def get_value(tup):
    # Return the 3rd value in the provided tuple
    return tup[2]


def get_values(tup):
    # return the values from index 1-3
    # 3 should be inclusive
    return tup[1:4]


def get_max(tup):
    # return the largest number in the provided tuple
    return max(tup)

#Notes
# A tuple in Python is a collection of objects which is ordered and immutable. Tuples cannot be changed. JS does not have a tuple equivalent.
# Tuples are declared like lists, just using () instead of []:
# my_tuple = (1,2,3), or new_tup = tuple(), or tuppy = ()
# tuples can have a mix of datatypes.
# tuples are iterable and we can access indices/values just like lists.
# There are also built in methods for tuples, such as finding min and max values, and even converting tuples to lists (and lists to tuples):
# min(tup) / max(tup)
# new_tup = tuple(my_list)
# new_list = list(my_tup)
# del my_tup
