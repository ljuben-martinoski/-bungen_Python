"""Program 1 — Coordinate Distance Calculator

Store city coordinates as tuples: city = ("Munich", 48.137, 11.576)
Create at least 3 cities
Write a function distance(city1, city2) that calculates the straight-line distance between 
two cities using their coordinates
Unpack tuples inside the function
Print a nicely formatted distance table"""

# Import the math library to use the sqrt() function for distance calculation
import math

# Define a function to get city information from the user
def get_city_input():
    # Ask user for the city name and convert it to a string
    name = str(input("Enter the city name: "))
    # Ask user for longitude and convert it to a decimal number
    lon = float(input(f"Enter the longitude for the city {name}"))
    # Ask user for latitude and convert it to a decimal number
    lat = float(input(f"Enter the latitude for the name {name}"))
    # Return all three values as a tuple (name, longitude, latitude)
    return name, lon, lat

# Define a function that takes two cities and calculates the distance between them
def distance(city1, city2):
    # Unpack city1 tuple into name1, longitude1, and latitude1
    name1, lon1, lat1 = city1
    # Unpack city2 tuple into name2, longitude2, and latitude2
    name2, lon2, lat2 = city2
    
    # Calculate distance using the Pythagorean theorem: sqrt((lat difference)^2 + (lon difference)^2)
    dist = math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)
    # Return the calculated distance
    return dist
    
# Print header message for user input
print("--City coordinates entry--")
# Get the first city's information from user and store it in c1
c1 = get_city_input()
# Print a separator line for visual clarity
print("-"* 20)
# Get the second city's information from user and store it in c2
c2= get_city_input()
# Print another separator line
print("-"* 20)
# Get the third city's information from user and store it in c3
c3 = get_city_input()
# Store all three cities in a list called cities
cities = [c1, c2, c3]

# Print a blank line followed by a line of equal signs to create a table header
print("\n" + "="*45)
# Print the table header with column labels (Route and Distance Units)
print(f"{'Route':<25} | {'Distance Units'}")
# Print another line of equal signs below the header
print("="*45)

# Create a list of route pairs: (city1 to city2), (city2 to city3), (city3 to city1)
routes = [(c1,c2), (c2,c3), (c3,c1)]

# Loop through each route pair
for city_start, city_end in routes:
    # Calculate the distance between the two cities in the current route
    d = distance(city_start, city_end)
    # Create a route name string combining the start city name and end city name
    route_name = f"{city_start[0]} to {city_end[0]}"
    # Print the route name and distance, formatted nicely in columns
    print(f"{route_name:<25} | {d:.4f}")

# Print the final line of equal signs to complete the table
print("="*45)





