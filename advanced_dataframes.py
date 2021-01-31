
from pydataset import data

##1. Load the mpg dataset. Read the documentation for it, and use the data to answer these questions

mpg = data('mpg')

#a. On average, which manufacturer has the best miles per gallon?

mpg.groupby('manufacturer').average_mileage.mean().nlargest(1, keep='all')

#b. How many different manufacturers are there?

mpg['manufacturer'].nunique()

#c. How many different models are there?

mpg['model'].nunique()

#d. Do automatic or manual cars have better miles per gallon?

def transmissions(trans):
    if trans.find('auto') > -1:
        return 'auto'
    else:
        return 'manual'
    
mgp[auto_or_manual] = mpg.trans.apply(transmission)
mgp.groupby('auto_or_manual')[['city', 'highway']].agg('mean')

##2. Joining and Merging

# Copy the users and roles dataframes from the examples above.

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})


# What do you think a right join would look like? 

pd.merge(users, roles, left_on='role_id', right_on='id', how='right')

# An outer join? 

pd.merge(users, roles, left_on='role_id', right_on='id', how='outer')

# What happens if you drop the foreign keys from the dataframes and try to merge them?

# Confusion happens

##3 Getting data from SQL databases

#a. Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url formatted like in the examples in this lesson.
from env import host, password, user

def get_db_url(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
#b. Use your function to obtain a connection to the employees database.

query = """
    SELECT * FROM employees limit 5
"""

employees = pd.read_sql(query, url)

#c. Once you have successfully run a query:
#Intentionally make a typo in the database url. What kind of error message do you see?

NameError: name 'get_dbs_url' is not defined

#Intentionally make an error in your SQL query. What does the error message look like?

ProgrammingError: (pymysql.err.ProgrammingError) (1146, "Table 'employees.employee' doesn't exist")

#d. Read the employees and titles tables into two separate dataframes

query = """
    SELECT * FROM employees limit 5
"""
employees = pd.read_sql(query, get_db_url)

query = """
    SELECT * FROM titles limit 5
"""
titles = pd.read_sql(query, get_db_url)

#e. Visualize the number of employees with each title.



#f. Join the employees and titles dataframes together.

emp_title = pd.merge(employees, titles, on='emp_no')
emp_title.head()

#g. Visualize how frequently employees change titles.



#h. For each title, find the hire date of the employee that was hired most recently with that title.

all_emp_titles.groupby('title').hire_date.max()

#i.Write the code necessary to create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL and python/pandas code)


##4 Use your get_db_url function to help you explore the data from the chipotle database. Use the data to answer the following questions:

#a. What is the total price for each order?


#b. What are the most popular 3 items?

chipotle['item_name'].value_counts().head(3)

#c. Which item has produced the most revenue?
