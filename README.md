# Vehicle Insurance Calculator

## Description

A tool that allows the user to register vehicles especifing model, brand, year of manufacture and price.

After registered, the user can calculate the insurance monthly fee based on the given information.

Using the functions present in the script, the user can print the cars table on the terminal (show_cars_table), register a vehicle (register_vehicle) and after inserting data on the database, the main.py file calculates the insurance fee of all existing vehicules.

## Tools Used

I used python to manipulate a MySQL database in a docker container.

I had never used this tools before this project, so it was a very challenging oportunity of learning.

The vehicle insurance calculator helped me learn about CRUD, interaction with databases and also a little about validating inputs, which was used to estabilish a pattern of brands (accepting only the brands present on the list brands in the validate.py file) and year of manufacture (accepting only values between 1970 and 2023).


