# Session 9 


# Exercises - mini ETL

In this exercises we want to create a simple process that reads data from a
source (a CSV file in our case), does some transformations to that data, and
outputs another file (a JSON file in our case).

## Exercise 1

create a function named `read_data` that reads the `balances.csv` into a list
of dictionaries.

## Exercise 2

Create a function named `transform` that receives a list of diccionaries as
input and return a dictionary with the average balance per state.

## Exercise 3

Create a function `sink` that receives the final dicionary and a file name
and stores that dict as JSON in the given filename.
