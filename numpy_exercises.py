
# How many negative numbers are there?

negative_nums = a[a < 0]
len(negative_nums)

# How many positive numbers are there?

positive_nums = a[a > 0]
len(positive_nums)

# How many even positive numbers are there?

even_positive_nums = positive_nums[positive_nums % 2 == 0]
len(even_positive_nums)

# If you were to add 3 to each data point, how many positive numbers would there be?

add_three = a + 3
add_three, add_three % 2 == 0

# If you squared each number, what would the new mean and standard deviation be?

num_sqrd = a ** 2
num_sqrd, num_sqrd.mean(), num_sqrd.std()

# A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set.

centered = a - a.mean()

a, a.mean(), centered

# Calculate the z-score for each data point. 

import scipy.stats as stats 
stats.zscore(a)

# -------- OR --------------

z_score = (a - a.mean()) / a.std()
z_score


## More Numpy Practice exercises

# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum(a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min(a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max(a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

sum(a) / len(a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

total = 1
for num in a:
    total += num
total

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

[num ** 2 for num in a]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

[num for num in a if num % 2 == 1]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

[num for num in a if num % 2 == 0]

## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Turning list(s) b into numpy array
b = np.array(b)

# Exercise 1 - Use sum_of_b as the variable.
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

# Numpy solution:
sum_of_b = b.sum()
b.sum()

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

# Numpy solution:
min_of_b = b.min()
min_of_b

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

# Numpy solution:
max_of_b = b.max()
max_of_b

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

# Numpy solution:
mean_of_b = b.mean()
mean_of_b

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

# Numpy solution:
product_of_b = np.prod(b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

# Numpy solution:
squares_of_b = b ** 2

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

# Numpy solution:
odds_in_b = b[b % 2 == 1]
odds_in_b
                        
# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

# Numpy solution:
evens_in_b = b[b % 2 == 0]
evens_in_b

# Exercise 9 - print out the shape of the array b.

np.shape(b)

# Exercise 10 - transpose the array b.

np.transpose(b)

b.T

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b.reshape(-1)

b.shape(6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

b.reshape(6, 1)


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

c = np.array(c)


# Exercise 2 - Determine the standard deviation of c.

np.std(c)

# Exercise 3 - Determine the variance of c.

np.var(c)

# Exercise 4 - Print out the shape of the array c

c.shape

# Exercise 5 - Transpose c and print out transposed result.

c.T

# Exercise 6 - Get the dot product of the array c with c. 

np.dot(c, c).sum()

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

(c * c.T).sum()

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

(c * c.T).prod()



## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

np.sin(d)

# Exercise 2 - Find the cosine of all the numbers in d

np.cos(d)

# Exercise 3 - Find the tangent of all the numbers in d

np.tan(d)

# Exercise 4 - Find all the negative numbers in d

d = np.array(d)
d[d < 0]

# Exercise 5 - Find all the positive numbers in d

d[d > 0]

# Exercise 6 - Return an array of only the unique numbers in d.

np.unique(d)

# Exercise 7 - Determine how many unique numbers there are in d.

np.unique(d)

# Exercise 8 - Print out the shape of d.

d.shape

# Exercise 9 - Transpose and then print out the shape of d.

d.T.shape

# Exercise 10 - Reshape d into an array of 9 x 2

d.reshape(9, 2)