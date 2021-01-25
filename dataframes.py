##1 Copy the code from the lesson to create a dataframe full of student grades.

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

#a. Create a column named passing_english that indicates whether each student has a passing grade in english.

df.assign(passing_english = df.english >= 70)

#b. Sort the english grades by the passing_english column. How are duplicates handled?

df.sort_values(by='passing_english')
# an error occurs

#c. Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)



#d. Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.



#e. Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.





##2 Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

#a. How many rows and columns are there?

data('mpg', show_doc=True) 
234 rows and 11 columns

#b. What are the data types of each column?

mpg.info()

#c. Summarize the dataframe with .info and .describe

mpg.info()

mpg.describe()

#d. Rename the cty column to city.

mpg.rename(columns = {'cty': 'city', 'hwy': 'highway'}, inplace=True)
mpg.columns

#e. Rename the hwy column to highway.

mpg.rename(columns = {'cty': 'city', 'hwy': 'highway'}, inplace=True)
mpg.columns

#f. Do any cars have better city mileage than highway mileage?



#g. Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.

mpg['mileage_difference'] = mpg['highway'] - mpg['city']
mpg.head()

#h Which car (or cars) has the highest mileage difference?



#i Which compact class car has the lowest highway mileage? The best?



#j Create a column named average_mileage that is the mean of the city and highway mileage.



#l Which Dodge car has the best average mileage? The worst?