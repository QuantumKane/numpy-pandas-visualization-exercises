
# How many negative numbers are there?

negative_nums = a[a < 0]
negative_nums

# How many positive numbers are there?

positive_nums = a[a > 0]
positive_nums


# How many even positive numbers are there?

even_positive_nums = positive_nums % 2 == 0
even_positive_nums

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

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.