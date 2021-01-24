
#1. Use pandas to create a Series


#a) Name the variable that holds the series fruits.

fruits_series = pd.Series(fruits)
fruits_series

#b) Run .describe() on the series to see what describe returns for a series of strings.

fruits_series.describe()

#c) Run the code necessary to produce only the unique fruit names

fruits_series.unique()

#d) Determine how many times each value occurs in the series.

fruits_series.value_counts()

#e) Determine the most frequently occurring fruit name from the series.

fruits_series.value_counts()

#f) Determine the least frequently occurring fruit name from the series.

fruits_series.value_counts()

#g) Write the code to get the longest string from the fruits series.

longest_str = fruits_series.str.len().max()
longest_str

#h) Find the fruit(s) with 5 or more letters in the name.

five_or_more = fruits_series[fruits_series.str.len() > 4]
five_or_more

#i) Capitalize all the fruit strings in the series.

capitalized_fruits = fruits_series.str.title()
capitalized_fruits

#j) Count the letter "a" in all the fruits (use string vectorization)

fruits_series.str.count('a')

#k) Output the number of vowels in each and every fruit.

vowels = list('aeiou')

def count_vowels(fruit):
    return len([let for let in fruit.lower() if let in vowels])

fruits_series.apply(count_vowels)

#l) Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

fruits_series[fruits_series.apply(lambda fruit: fruit.count('o') > 1)]

#m) Write the code to get only the fruits containing "berry" in the name

fruits_series[fruits_series.str.contains('berry')]

#n) Write the code to get only the fruits containing "apple" in the name

fruits_series[fruits_series.str.contains('apple')]

#o) Which fruit has the highest amount of vowels?

fruits_series[(fruits_series.str.count(r'[aeiou]')).max()]


#2 Use pandas to create a Series 

cash_series = pd.Series(cash)
cash_series

#a) What is the data type of the series?


#b) Use series operations to convert the series to a numeric data type


#c) What is the maximum value? The minimum?



#d) What is the maximum value? The minimum?



#e) Plot a histogram of the data. Be sure to include a title and axis labels.




#3. Use pandas to create a Series

exam_series = pd.Series(exams)
exam_series

