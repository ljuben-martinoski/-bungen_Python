"""
Docstring for Lists.Übungen.temperatur_tracker
"""


# Create an empty list for temperatures
# Add 5 temperature readings using .append()
# Calculate and print:
#   - How many readings
#   - Average temperature
#   - Highest temperature
#   - Lowest temperature
import math 

def temperature_tracke():

    temperatures = []

    temperatures.append(23)
    temperatures.append(33)
    temperatures.append(18)
    temperatures.append(27)
    temperatures.append(38)
    print(f"Number of readings: {len(temperatures)}")
    average = sum(temperatures)/ len(temperatures)
    print(f"The Average temperature of the readings is: {average:.2f}°C")# :.2f this is the format specifier that means show 2 decimal places,: is just the format separator
    print(f"The Highest temperature is: {min(temperatures)}C°")
    print(f"The lowest temperatur is: {min(temperatures)}C°")
    

temperature_tracke()


          



