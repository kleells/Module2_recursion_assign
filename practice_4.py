# Write a Python function called max_num()to find
# the maximum of three numbers.

from unittest import result


def max_num(num1, num2, num3):
    return max([num1, num2, num3])


print(max_num(4, 52, 106))

# Write a Python function called mult_list() to
# multiply all the numbers in a list.

def mult_list(numList):
    result = 1
    for n in numList:
        result = result * n
    return result

list = [5, 10, 2]

print (mult_list(list))

# Write a Python function called rev_string() to
# reverse a string.

def rev_string(str):
    print(str[::-1])

rev_string("Willy Wonka")

# Write a Python function called num_within() to check
# whether a number falls in a given range.

# The function accepts the number, beginning of range,
# and end of range (inclusive) as arguments.

# Examples: num_within(3,2,4) returns True, num_within(3,1,3)
# returns True, num_within(10,2,5) returns False.

def num_within(n, start_num, end_num):
    return n in range(start_num, end_num+1)

print(num_within(5, 2, 7))
print(num_within(5, 7, 9))
print(num_within(1, 3, 6))
print(num_within(6, 5, 9))

# Write a Python function called pascal() that prints out the
# first n rows of Pascal's triangle.

# The function accepts the number n, the number of rows to print

# Note : Pascal's triangle is an arithmetic and geometric figure
# first imagined by Blaise Pascal. Each number is the two numbers
# above it added together.

def pascals(n):
    if n == 1:
        return [[1]] # Base case termination condition
    else:
        result = pascals(n-1) # Recursive call
        # Calculate current row using info from previous row
        current_row = [1]
        prev_row = result[-1] # Take from end of result
        for i in range(len(prev_row)-1):
            current_row.append(prev_row[i] + prev_row[i+1])
        current_row += [1]
        result.append(current_row)
        return result


triangle = pascals(10)
for row in triangle:
    print(row)
