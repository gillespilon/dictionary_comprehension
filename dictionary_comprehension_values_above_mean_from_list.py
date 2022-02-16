#! /usr/bin/env python3
'''
Create a dictionary of values greater than the mean from another dictionary.
'''

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
keys_values = dict(zip(keys, values))
values_mean = sum(keys_values.values()) / len(keys_values)
print(values_mean)
result = {
    key: value for key, value in keys_values.items() if value > values_mean
}
print(result)
