# Programming-Assignment-3

NAME: Arabelle Villarin

SECTION: 2ECE-DㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤDATE SUBMITTED: September 19, 2024

------------------------------------------------------------------------------------------------
ㅤ
## PROBLEM 1ㅤ

### A.

The code uses a CSV file containing information about cars, the goal is to display the first five rows of the dataset. 

1st step:

Input "import pandas as pd" for efficiency and readability of pandas commands

2nd step:

Place 'cars.csv' file in the same directory

3rd step: 

Use 'cars.head()' to display the first five rows of the resulting cars


### B.

This code is similar to Problem 1 (A), its difference is that it displays the last 5 rows instead of the first 5 rows

It uses the function: 'cars.tail()'


## PROBLEM 2

### A.

1st step:

The 1st step of this code is similar to the 1st step of Problem 1 (A), by also using the same CSV file of 'cars.csv'.

2nd step:

It then displays the first odd five rows of the columns by using the code:

````
cars.iloc[:5, [1, 3, 5, 7, 9]]
````




### B.
### C.
### D.
