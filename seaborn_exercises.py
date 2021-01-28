
# Use the iris database to answer the following quesitons:

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pydataset import data

get_db_url = f'mysql+pymysql://{user}:{password}@{host}/iris_db'
    
query = """
    SELECT * FROM measurements limit 10
"""
iris_measure = pd.read_sql(query, get_db_url)
iris_measure

# What does the distribution of petal lengths look like?

sns.distplot(iris_measure.petal_length)

# Is there a correlation between petal length and petal width?

sns.lmplot(x='petal_length', y='petal_width', data=iris_measure)
plt.title('Petal Length vs Petal Width')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

# Would it be reasonable to predict species based on sepal width and sepal length?

sns.regplot(x='sepal_length', y='sepal_width', data=iris_measure)
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

# Which features would be best used to predict species?

sns.boxplot(y = 'sepal_length', x = 'species_id', data = iris_measure)

##1 Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set.

anscombe = sns.load_dataset('anscombe')

# Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. What do you notice?

anscombe.groupby('dataset').describe()

# Plot the x and y values from the anscombe data. Each dataset should be in a separate column.

sns.lmplot(data = anscombe, x = 'x', y = 'y', col = 'dataset')


##2 Load the InsectSprays dataset and read it's documentation. 

sprays = data('InsectSprays')
data('InsectSprays', show_doc = True)

# Create a boxplot that shows the effectiveness of the different insect sprays.

sns.boxplot(data = sprays, x = 'count', y = 'spray')

##3 Load the swiss dataset and read it's documentation.

swiss = data('swiss')
data('swiss', show_doc = True)

# Create visualizations to answer the following questions:
# Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. (Choose a cutoff point for what constitutes catholic)

swiss['is_catholic'] = (swiss['Catholic'] > 40)
swiss.head(10)

# Does whether or not a province is Catholic influence fertility?

sns.jointplot(data = swiss, x = 'Fertility', y = 'Catholic', hue = 'is_catholic')

# What measure correlates most strongly with fertility?

sns.pairplot(data = swiss.iloc[:, :-1])


##4 Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.

get_db_url = f'mysql+pymysql://{user}:{password}@{host}/chipotle'
    
query = """
    SELECT * FROM orders
"""
chipotle = pd.read_sql(query, get_db_url)

chipotle['item_price'] = chipotle.item_price.str.replace('$', '').astype(float)

top_4 = chipotle.groupby('item_name')[['quantity', 'item_price']].sum().nlargest(4, ['quantity'], keep = "all")
top_4.item_price.sort_values(ascending = False).plot.bar()


##5 Load the sleepstudy data and read it's documentation.

sleep_study = data('sleepstudy')
data('sleepstudy', show_doc = True)

# Use seaborn to create a line chart of all the individual subject's reaction times and a more prominant line showing the average change in reaction time.



