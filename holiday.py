# Print available cities user can fly to
print("Available cities: Cape Town, Durban, Johannesburg")

# Prompt user to enter information
city_flight = input("Enter city you are flying to?: ").strip().lower()
num_nights = int(input("Enter number of nights you will be spending?: "))
rental_days = int(input("Enter number of days you will hire a car for?: "))

# Cost functions
def hotel_cost(nights):
    return 1400 * nights  # R1400 per night

def plane_cost(city):
    if city == "cape town":
        return 3000
    elif city == "durban":
        return 1900
    elif city == "johannesburg":
        return 1600
    else:
        return None  # invalid city

def car_rental(days):
    return 200 * days  # R200 per day

# Required holiday_cost() function
def holiday_cost(num_nights, city_flight, rental_days):
    flight = plane_cost(city_flight)

    # Validate city BEFORE calculating anything else
    if flight is None:
        return None  # return None if invalid city

    hotel = hotel_cost(num_nights)
    car = car_rental(rental_days)
    total = hotel + flight + car
    return total

# Calculate total holiday cost
total_holiday_cost = holiday_cost(num_nights, city_flight, rental_days)

# If invalid city
if total_holiday_cost is None:
    print("\nInvalid city entered. Please choose from: Cape Town, Durban, Johannesburg.")
else:
    # Normal output
    print("\n----- HOLIDAY COST BREAKDOWN -----")
    print(f"Hotel cost for {num_nights} nights: R{hotel_cost(num_nights)}")
    print(f"Flight cost to {city_flight.title()}: R{plane_cost(city_flight)}")
    print(f"Car rental cost for {rental_days} days: R{car_rental(rental_days)}")
    print("----------------------------------")
    print(f"Total holiday cost: R{total_holiday_cost}")