
#1. Use pandas to create a Series


#a) Name the variable that holds the series fruits.

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
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

cash =  = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
cash_series = pd.Series(cash)
cash_series

#a) What is the data type of the series?

cash_series.dtype()

#b) Use series operations to convert the series to a numeric data type

float_num = cash_series.str.replace('$', '').str.replace(',', '').astype('float')
float_num

#c) What is the maximum value? The minimum?

float_num.max()

float_num.min()

#d) Bin the data into 4 equally sized intervals and show how many values fall into each bin

float_num.value_counts(bins=4)

#e) Plot a histogram of the data. Be sure to include a title and axis labels.

float_num.value_counts(bins=4).sort_index(ascending=False).plot.barh(ec = 'black', 
                                                                    color= 'slateblue',  
                                                                    width = .8)

plt.title('Cash Values')
plt.xlabel('Count')
plt.ylabel('US $')
plt.show()



#3. Use pandas to create a Series

exams  = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
exam_series = pd.Series(exams)
exam_series

#a) What is the minimum exam score? The max, mean, median?



#b) Plot a histogram of the scores.



# c) Convert each of the numbers above into a letter grade.



# d) Write the code necessary to implement a curve.

