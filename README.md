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

1st step:

Using the loc method to access rows by the label.

2nd step:

````
cars['Model'] == 'Mazda RX4'
````
This part checks the Model column of the cars DataFrame to find rows where the value is equal to 'Mazda RX4'. This condition also uses boolean function.


### C.

1st step:

This part is similar to the 1st step of Problem 2 (B), by using the loc method.

2nd step:

````
cars['Model'] == 'Camaro Z28'
````
This part checks the Model column in the cars DataFrame for rows where the value is 'Camaro Z28'. It creates a boolean Series where True indicates a match.

3rd step:

'cyl' indicates that it is specifically retrieving the cylinder column.

### D.

1st step:

This part is similar to the 1st step of Problem 2 (B and C), by using the loc method.

2nd step:

using '.isin' to check if the values in the Model column are one of the specified models. It returns a boolean Series where True indicates a match for any of the three car models.

3rd step:

Inputting 'cyl' and 'gear' specifically retrieves the cylinder and gear columns of the resulting rows.

-------------------------------------------------------------------------------------------------------------------------------------
## Conclusion

The given problems are easy to make because of the few functions to be coded. It saves time and effort creating rows and columns one by one.



