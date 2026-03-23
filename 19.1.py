'''#generate a python class with attributes and methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def have_birthday(self):
        self.age += 1
        return f"Happy birthday! You are now {self.age} years old."
# Example usage
person1 = Person("Alice", 30)   
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
print(person1.have_birthday())  # Output: Happy birthday! You are now 31 years old.

#GENERATE A C++ FUNCTION FOR FACTORIAL CALCULATION
#include <iostream>
using namespace std;
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
int main() {    
    int number;
    cout << "Enter a number to calculate its factorial: ";
    cin >> number;
    cout << "Factorial of " << number << " is " << factorial(number) << endl;
    return 0;
}
# CONVERT IT INTO PYTHON
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
number = int(input("Enter a number to calculate its factorial: "))
print(f"Factorial of {number} is {factorial(number)}")'''

'''#GENERATE A SQL QUERY TO SELECT ALL RECORDS FROM A TABLE CALLED "EMPLOYEES"
SELECT * FROM EMPLOYEES;
'''
#CONVERT IT INTO A PANDAS DATAFRAME
import pandas as pd
# Assuming you have a connection to your database and have executed the SQL query
# For example, using SQLAlchemy to connect to a database
from sqlalchemy import create_engine
# Create a connection to the database (replace with your own connection string)
engine = create_engine('your_connection_string_here')
# Execute the SQL query and load the results into a pandas DataFrame
query = "SELECT * FROM EMPLOYEES"
df = pd.read_sql_query(query, engine)
# Now 'df' contains all the records from the EMPLOYEES table

