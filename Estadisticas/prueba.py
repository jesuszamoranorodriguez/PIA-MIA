from statistics import fmean, kde, median
from math import isnan
from itertools import filterfalse

grades = [6, 7, 5]
weights = [0.5, 0.20, 0.30]

print(fmean(grades, weights))

kde = kde(grades, weights)

print(kde)