# TEMPERATURE MONITOR SYSTEM
#### Video Demo:  <https://youtu.be/D_FwysM1PFU?si=jwGP28f7cc6Xs-UK>
#### Description: My project responds to various actions of the user and outputs the desired option e.g CURRENT temperature,CHANGE city,FORECAST,CLOTHING and SHOW TABLE.It is a Python-based command-line application designed to fetch real-time weather data for cities across the world and provide insights and recommendation based on the current temperature.It leverages external APIs to obtain live temperature readings and forecast information,allowing users to plan their day and attire accordingly.Further,it features a robust system for handling user inputs,maintaining a record of searched cities,offering useful features like temperature classification and clothing suggestion.

## Structure
The project is implemented using Python.It has the following files:
- project.py
- test_project.py
- world-cities.csv

## project.py
1. project.py
It is the main application file that has the core logic of project.It uses different liabraries like csv,requests,colorama and prettytable.The Class and functions in this file are:
* Temperature Class:
It has the following functions:
a. __init__(self,place):Initializes the object with a city name.
b. get_temp(self):It fetches the current temperature of the specified city from the url of wttr.in and outputs message in case of an error.
c. get_temp_forecast(self):Retrieves a 3-day weather forecast for the city from the same url.
d. average(self,temperature):Classifies the temperature into three catagories,"AVERAGE","BELOW AVERAGE","ABOVE AVERAGE".
e. print_temperature(self,forecast_days=None):Displays the current and the 3-day waether forecast of the city.
f. clothing_suggestion(self,temperature):Provides clothing suggestions based on the temperature.

Other main functions:
* update_data(table_cities,city):Updates the list of cities entered by the user,ensuring no copies are added.
* print_table(table_cities):Displays a table(using Prettytable) of all the cities being inputted,printing their IDs and City names.
* check_city(city):Verifies if the inputted city name is valid by checking against the list of world-cities from the CSV file.
* actions(action,temperature,table_cities):Manages user actions such as checking current temperature,viewing forecasts,changing city, displaying city table record and exiting.
* action_Class(action,temperature,table_cities,new_place=None):Handles the execution of the specific user's actions like "CURRENT", "FORECAST","CHANGE","CLOTHING","SHOW TABLE" and "EXIT"

## test_project.py
This file contains unit tests that ensures the core functions and Class of project.py are working as expected.The tests are implemented using pytest and include:
* test_update_data():Tests the update_data() for correctly adding cities to the list and avoiding copies.
* test_print_table(capsys):Tests the print_table() by capturing its output and verifying the content.
* test_check_city():Verifies that the check_city() correctly identifies valid and invalid city names.
* test_action_Class(capsys):Tests the action_Class() for correct handling of different user actions.

## world-cities.csv
This CSV file contains a list of world cities.The check_city()references this file to validate user input for city names.It has columns:city name,country,etc.This file is critical to ensure that the user inputs valid city names recognized globally.

## Design
The project was designed with user interaction and experience in mind.Mainly:
* Input Validation:Ensures that users only input valid city names to avoid errors during API calls.
* User-Friendly:The command-line prompts and color-coded output(using colorama)makes the program visually appealing and easy to use.
* Modular Design:By separating functionalities into different functions,the code is more maintainable and testable.
* Error Handling:Gracefully handles potential errors,such as API failures or invalid temperature data,by outputing messages.
