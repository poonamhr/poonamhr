import csv
import requests
from colorama import init, Fore, Style
from prettytable import PrettyTable

init()


class Temperature:
    def __init__(self, place):
        self.place = place

        self.forecast_week = 3

    def get_temp(self):
        url = f"https://wttr.in/%7B{self.place}%7D?format=%t"

        response = requests.get(url)
        if response.status_code == 200:
            try:
                temperature = response.text.strip()
                temperature = float(temperature.replace("°C", "").replace("+", "").strip())
                return temperature
            except ValueError:
                print("Something went wrong! Couldn't parse the temperature")
                return None
        else:
            print("Something went wrong! Expected code status = 200 OK ")
            return None

    def get_temp_forecast(self):
        url = f"https://wttr.in/%7B{self.place}%7D"
        response = requests.get(url)

        if response.status_code == 200:
            forecast = response.text.strip()
            return forecast
        else:
            print("Something went wrong! Couldn't fetch the weather. ")
            return None

    # average Function will print the average classification according to the temperature

    def average(self, temperature):
        if temperature < 10:
            return f"{Fore.BLUE}BELOW AVERAGE{Style.RESET_ALL}"
        elif 10 <= temperature <= 25:
            return f"{Fore.GREEN}AVERAGE{Style.RESET_ALL}"
        else:
            return f"{Fore.RED}ABOVE AVERAGE{Style.RESET_ALL}"

    # print_temperature Function will print the current temp and forecast for 3 days accordingly the action of the user

    def print_temperature(self, forecast_days=None):
        if forecast_days == 3:
            forecast = self.get_temp_forecast()
            if forecast:
                print(f" 3-Day Weather Forecast for {self.place}: ")
                print(forecast)
            else:
                print("No forecast data available. ")
        else:
            temp_now = self.get_temp()
            if temp_now is None:
                print(f"Something went wrong! Couldn't retrieve the temperature. ")
            else:
                classification = self.average(temp_now)
                print(
                    f"\nThe current temperature in {self.place} is {Fore.LIGHTCYAN_EX}{temp_now}°C{Style.RESET_ALL} which is considered {classification}. \n")

# clothing_suggestion Function according to the temperature

    def clothing_suggestion(self, temperature):
        if temperature < 0:
            clothing = f"\n{Fore.CYAN}Heavy winter clothing like{Style.RESET_ALL} \n• a coat🧥, \n• hat, \n• gloves🧤, \n• boots🥾 and \n• scarf🧣"
        elif 0 <= temperature < 10:
            clothing = f"\n{Fore.CYAN}Warm clothing like{Style.RESET_ALL} \n• a sweater, \n• jacket"
        elif 10 <= temperature < 20:
            clothing = f"\n{Fore.CYAN}light clothing like{Style.RESET_ALL} \n• long-sleeve shirt👔 or \n• a light jacket"
        elif 20 <= temperature < 30:
            clothing = f"\n{Fore.CYAN}Comfortable clothing like{Style.RESET_ALL} \n• t-shirts👕👚, \n• shorts🩳, \n• summer-dresses👗"
        else:
            clothing = f"\n{Fore.CYAN}Light clothing like{Style.RESET_ALL} \n• a t-shirt👕👚, \n• shorts🩳, and \n• sunglasses🕶️ (sunscreen is recommended)"
        print(
            f"\nBased on the current temperature of {temperature}°C, it's recommended to wear: {clothing}. ")


def main():
    print(f"{Fore.MAGENTA}\n        WELCOME TO THE TEMPERATURE MONITOR SYSTEM! \n{Style.RESET_ALL}")
    while True:
        place = input("Enter a city name: ")
        if check_city(place):
            break
        else:
            print(f"{place} is not a valid city name. \n")

    table_cities = []
    action = []
    update_data(table_cities, place)
    temperature = Temperature(place)
    actions(action, temperature, table_cities)

# update_data Function updates the cities entered by the user


def update_data(table_cities, city):
    city = city.strip().upper()
    found = False
    for data in table_cities:
        if data["CITY"] == city:
            found = True
            break
    if not found:
        new_id = len(table_cities) + 1
        table_cities.append({"ID": new_id, "CITY": city})

# print_table Function to print the table with data of the entered cities by the user


def print_table(table_cities):
    table = PrettyTable()
    table.field_names = ["ID", "CITY"]

    for data in table_cities:
        table.add_row([data["ID"], data["CITY"]])
    print(f"\n{Fore.MAGENTA}Record of the Entered Cities: {Style.RESET_ALL}")
    print(table)

# check_city Function for ensuring if the city is valid or invalid


def check_city(city):
    file_path = "world-cities.csv"
    with open(file_path, newline='') as file_csv:
        reader = csv.DictReader(file_csv)
        cities = [row['name'].strip().lower() for row in reader]
    city = city.strip().lower()
    return city in cities

# actions Function for the inputs of the user


def actions(action, temperature, table_cities):
    PINK = "\033[38;2;231;84;128m"
    RESET = "\033[0m"
    while True:

        action = input(f"{Fore.YELLOW}\nType (in capital letters only):{Style.RESET_ALL}\n❖ {PINK}'CURRENT'{RESET} to check today's temperature, \n❖ {PINK}'FORECAST'{RESET} for 3-day weather forecast, \n❖ {PINK}'CHANGE'{RESET} to change the city, \n❖ {PINK}'CLOTHING'{RESET} for clothing suggestion, \n❖ {PINK}'SHOW TABLE'{RESET} to print the table \n❖ or type {PINK}'EXIT'{RESET} to exit \n")

        result = action_execution(action, temperature, table_cities)
        if result == "EXIT":
            print(f"{Fore.CYAN}            THANK YOU FOR VISITING! {Style.RESET_ALL}")
            break
        elif not result:
            print("Something went wrong! Couldn't quit the action.")

# action_execution function for handling the different actions of the user


def action_execution(action, temperature, table_cities, new_place=None):
    if action == "CURRENT":
        temperature.print_temperature()
        return True

    elif action == "FORECAST":
        temperature.print_temperature(forecast_days=3)
        return True

    elif action == "EXIT":
        return "EXIT"

    elif action == "CHANGE":
        if new_place is None:
            new_place = input("\n Enter a new place: ")
        update_data(table_cities, new_place)
        temperature.place = new_place
        print(f"City changed to {new_place}. ")
        return True

    elif action == "CLOTHING":
        temp_now = temperature.get_temp()
        if temp_now is not None:
            temperature.clothing_suggestion(temp_now)
            return True
        else:
            print("Something went wrong! ")
            return False

    elif action == "SHOW TABLE":
        print_table(table_cities)
        return True

    else:
        print("Please type either 'CURRENT', 'FORECAST', 'CHANGE', 'CLOTHING', 'SHOW TABLE' or 'EXIT'! ")
        return False


if __name__ == "__main__":
    main()
