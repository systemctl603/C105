from pandas import read_csv
import math

df = read_csv("data.csv")

list_of_nums = [int(item) for item in list(df)]

population = len(list_of_nums)

mean = sum(list_of_nums) / population

summation = 0
for num in list_of_nums:
  summation += ((num - mean)**2)

stdev = math.sqrt(summation / population)
print(stdev)
