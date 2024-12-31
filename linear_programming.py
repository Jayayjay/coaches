import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def base_fare():
    return 1700

def distance_fare(distance, cost_per_km):
    return distance * cost_per_km

def time_fare(time, cost_per_min):
    return time * cost_per_min

def ride_option_fare(ride_type):
    fares = {"Economy": 200, "Premium": 1000}
    return fares.get(ride_type, 20)

def surge_price(demand, supply, base_price):
    if supply == 0:
        return base_price * 2
    surge_multiplier = 1 + (demand / supply)
    return base_price * surge_multiplier

def service_fare():
    return (2/100) * base_fare()

def total_fare_calculation(distance, time, cost_per_km, cost_per_minute, ride_type, demand, supply):
    base = base_fare()
    distance_cost = distance_fare(distance, cost_per_km)
    time_cost = time_fare(time, cost_per_minute)
    ride_cost = ride_option_fare(ride_type)
    surge = surge_price(demand, supply, base + distance_cost + time_cost + ride_cost)
    service = service_fare()
    return base + distance_cost + time_cost + ride_cost + surge + service
    
distance = 7.9  # km
time = 17  # mins
cost_per_km = 186 #In naira
cost_per_minute = 33 # in naira
ride_type = "Economy"
# how do we calculate the demand and supply rates
demand = 50 # how do we calculate the demand and supply rates
supply = 30

total_fare = total_fare_calculation(distance, time, cost_per_km, cost_per_minute, ride_type, demand, supply)
print("Total Fare:", total_fare)

# # Visualization 
# def visualize_fare_comparison(your_model, competitors):
#     labels = ["Your Model", "Competitor A", "Competitor B"]
#     fares = [your_model, competitors[0], competitors[1]]
#     plt.bar(labels, fares, color=["blue", "green", "red"])
#     plt.title("Fare Comparison")
#     plt.ylabel("Fare (in currency)")
#     plt.show()
    
# visualize_fare_comparison(14445.466666666667, 2900)