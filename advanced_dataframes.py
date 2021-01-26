
from pydataset import data

##1. Load the mpg dataset. Read the documentation for it, and use the data to answer these questions

mpg = data('mpg')

#a. On average, which manufacturer has the best miles per gallon?

mpg.sort_values(by = 'average_mileage', ascending = False).head()

#b. How many different manufacturers are there?

mpg['manufacturer'].nunique()

#c. How many different models are there?

mpg['model'].nunique()

#d. Do automatic or manual cars have better miles per gallon?



##2. Joining and Merging

# Copy the users and roles dataframes from the examples above. What do you think a right join would look like? An outer join? What happens if you drop the foreign keys from the dataframes and try to merge them?
