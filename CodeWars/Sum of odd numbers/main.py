'''
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8

'''

def row_sum_odd_numbers(n):
    sum = 0
    num = n * (n - 1) + 1
    for i in range(n):
        sum += num
        num += 2
    return sum
    