# 1. Crea five_number_summary(nums) que devuelva 
# (min, Q1, median, Q3, max) usando statistics. Usa statistics.quantiles 
# para los cuartiles y statistics.median para la mediana.

import statistics

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def five_number_summary(nums):
    return (min(nums), statistics.quantiles(nums)[0], statistics.median(nums), statistics.quantiles(nums)[2], max(nums))

X = five_number_summary(nums)

print(X)