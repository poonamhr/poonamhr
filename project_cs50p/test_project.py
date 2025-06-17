import pytest
from project import update_data, print_table, check_city, action_execution


def test_update_data():
    table_cities = []

    update_data(table_cities, "Athens")
    assert len(table_cities) == 1
    assert table_cities[0]["CITY"] == "ATHENS"
    assert table_cities[0]["ID"] == 1

    update_data(table_cities, "Corfu")
    assert len(table_cities) == 2
    assert table_cities[1]["CITY"] == "CORFU"
    assert table_cities[1]["ID"] == 2

    update_data(table_cities, "Athens")
    assert len(table_cities) == 2
    assert table_cities[0]["CITY"] == "ATHENS"


def test_print_table(capsys):
    table_cities = [{"ID": 1, "CITY": "Athens"}, {"ID": 2, "CITY": "Corfu"}]
    print_table(table_cities)

    captured = capsys.readouterr()
    assert "Record of the Entered Cities" in captured.out
    assert "Athens" in captured.out
    assert "Corfu" in captured.out


def test_check_city():
    assert check_city("Athens") == True
    assert check_city("Corfu") == True

    assert check_city("Athenn") == False
    assert check_city("Corfuuu") == False


class MockTemperature:
    def __init__(self, place):
        self.place = place

    def print_temperature(self, forecast_days=None):
        if forecast_days:
            print(f"Forecast for {forecast_days} days in {self.place}")
        else:
            print(f"Current temperature in {self.place}")

    def get_temp(self):
        return 30

    def clothing_suggestion(self, temp):
        print(f"Clothing Suggestion for temperature: {temp} ")


class MockTableCities(list):
    pass


def test_action_execution(capsys):
    temperature = MockTemperature("Athens")

    result = action_execution("CURRENT", temperature, MockTableCities())
    assert result == True

    result = action_execution("FORECAST", temperature, MockTableCities())
    assert result == True

    result = action_execution("EXIT", None, None)
    assert result == "EXIT"

    result = action_execution("INVALID", None, None)
    assert result == False

    table_cities = MockTableCities()
    new_place = "Corfu"

    result = action_execution("CHANGE", temperature, table_cities, new_place=new_place)
    assert result == True
    assert temperature.place == "Corfu"
    assert len(table_cities) == 1
    assert table_cities[0]["CITY"] == "CORFU"

    table_cities.append({"ID": 1, "CITY": "Athens"})
    table_cities.append({"ID": 2, "CITY": "Corfu"})

    result = action_execution("SHOW TABLE", temperature, table_cities)
    captured = capsys.readouterr()
    assert result == True
    assert "Record of the Entered Cities" in captured.out
    assert "Athens" in captured.out
    assert "Corfu" in captured.out

    result = action_execution("CLOTHING", temperature, None)
    captured = capsys.readouterr()
    assert result == True
    assert "Clothing Suggestion for temperature: 30" in captured.out
