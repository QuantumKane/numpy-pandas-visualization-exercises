
#1. Use pandas to create a Series


#a) Name the variable that holds the series fruits.

fruit_series = pd.Series(fruits)
fruit_series

#b) Run .describe() on the series to see what describe returns for a series of strings.

fruit_series.describe()

#c) Run the code necessary to produce only the unique fruit names

fruit_series.unique()

#d) Determine how many times each value occurs in the series.

fruit_series.value_counts()

#e) Determine the most frequently occurring fruit name from the series.



#f) Determine the least frequently occurring fruit name from the series.


#g) Write the code to get the longest string from the fruits series.


#h) Find the fruit(s) with 5 or more letters in the name.


#i) Capitalize all the fruit strings in the series.

capitalized_fruits = fruit_series.str.title()
capitalized_fruits

#j) Count the letter "a" in all the fruits (use string vectorization)


#k) Output the number of vowels in each and every fruit.



#l) Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.



#m) Write the code to get only the fruits containing "berry" in the name



#n) Write the code to get only the fruits containing "apple" in the name





