# From invoice
trip_fee = 2420.47
distance_km = 9.4  # Assumed from initial state
time_in_minutes = 16  # Assumed from initial state
ride_type_fare = 150  # Assumed from initial state

# Base fare assumption (initial)
base_fare = 1650
base_cost = 875

# Calculate remaining costs
dynamic_cost = trip_fee - base_fare - ride_type_fare
cost_per_km = dynamic_cost / distance_km
cost_per_minutes = dynamic_cost / time_in_minutes

# Surge percentage assumption
surge_percentage = 10  # Assumed from initial state

# Display estimated parameters
print("Base Fare (Estimated): {:.2f}".format(base_fare))
print("Cost per Kilometer (Estimated): {:.2f}".format(cost_per_km))
print("Cost per Minute (Estimated): {:.2f}".format(cost_per_minutes))
print("Ride Type Fare (Estimated): {:.2f}".format(ride_type_fare))
print("Surge Percentage (Estimated): {}%".format(surge_percentage))
print("Base Cost (Assumed): {:.2f}".format(base_cost))
print("Distance (km): {:.2f}".format(distance_km))
print("Time (minutes): {:.2f}".format(time_in_minutes))
