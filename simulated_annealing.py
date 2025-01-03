import math 
import random

# Definign objective function 
def objective_function(state, competitor_fares):
    total_fares = (
        state['base_fare'] +
        state['cost_per_km'] * state['distance_km'] +
        state['cost_per_minutes'] * state['time_in_minutes'] +
        state['ride_type_fare'] +
        (state['surge_percentage']/100) * state['base_fare']
    )
    
    # minimizing the differences with competitors fares
    avg_competitor_fare = sum(competitor_fares) / len(competitor_fares)
    cost_difference = abs(total_fares -avg_competitor_fare)
    
    # penalty is total fare is less than the base operational cost
    operational_cost = state['base_cost'] + state['cost_per_km'] * state['distance_km']
    penalty = max(0, operational_cost - total_fares)
    return cost_difference + penalty

def tweak_states(state):
    # generate a neighbouring state by slightly teaking on variable
    new_state = state.copy()
    tweak_variable = random.choice(['base_fare', 'cost_per_km', 'cost_per_min', 'ride_type_fare', 'surge_percentage'])
    
    if tweak_variable == "base_fare":
        new_state[tweak_variable] += random.uniform(-1, 1)
    elif tweak_variable == "cost_per_km":
        new_state[tweak_variable] += random.uniform(-0.1, 0.1)
    elif tweak_variable == "cost_per_minute":
        new_state[tweak_variable] += random.uniform(-0.05, 0.05)
    elif tweak_variable == "ride_type_fare":
        new_state[tweak_variable] += random.uniform(-2, 2)
    elif tweak_variable == "surge_percentage":
        new_state[tweak_variable] += random.uniform(-5, 5)
        
    # Ensure values remain positive
    for key in new_state: 
        new_state[key] = max(0, new_state[key])
        
    return new_state

def acceptance_probability(current_cost, new_cost, temperature):
    # Determining the probability of accepting a worse state
    if new_cost < current_cost:
        return 1.0
    return math.exp((current_cost - new_cost) / temperature)

def simulated_annealing(initial_state, competitors_fares, max_iterations=1000, initial_temperature=100, cooling_rate=0.95):
    # Simulated_annealing for fare optimization
    current_state = initial_state
    current_cost = objective_function(current_state, competitors_fares)
    best_state = current_state
    best_cost = current_cost
    temperature = initial_temperature
    
    for iteration in range(max_iterations):
        # Geerate a neighboring state
        new_state = tweak_states(current_state)
        new_cost = objective_function(new_state, competitors_fares)
        # Decision whether to accept the new state
        if new_cost < current_cost or random.random() < acceptance_probability(current_cost, new_cost, temperature):
            current_state  = new_state
            current_cost = new_cost
            print("Accepting new state")
            # Updating Best state
            if new_cost < best_cost:
                best_state = new_state
                best_cost = new_cost
                print("updating cost")
                
        # Cooling down the temperature
        temperature *= cooling_rate
        print("cooling temperature")
        
        # Terminating early if temperature is very low
        if temperature < 1e-5:
            break
    return best_cost, best_state
# Test cases
initial_state = {
    'base_fare': 1650,
    'cost_per_km': 150,
    'cost_per_minutes': 33,
    'ride_type_fare': 150,
    'surge_percentage': 10,
    'base_cost': 875,  # Operational base cost
    'distance_km': 9.4,  # Distance in km
    'time_in_minutes': 16  # Time in minutes
}

competitors_fares = [932, 186, 33, 200, 26]

best_state, best_cost = simulated_annealing(initial_state, competitors_fares)

print(best_state)
print(best_cost)
     
        