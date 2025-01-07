import math 
import random

# Defining objective function 
def objective_function(state, competitor_fares):
    total_fares = (
        state['base_fare'] +
        state['cost_per_km'] * state['distance_km'] +
        state['cost_per_minutes'] * state['time_in_minutes'] +
        state['ride_type_fare'] +
        (state['surge_percentage'] / 100) * state['base_fare']
    )
    
    # Minimizing the differences with competitors' fares
    avg_competitor_fare = sum(competitor_fares) / len(competitor_fares)
    cost_difference = abs(total_fares - avg_competitor_fare)
    
    # Penalty if total fare is less than the base operational cost
    operational_cost = state['base_cost'] + state['cost_per_km'] * state['distance_km']
    penalty = max(0, operational_cost - total_fares)
    return cost_difference + penalty

def tweak_states(state):
    # Generate a neighboring state by slightly tweaking one variable
    new_state = state.copy()
    tweak_variable = random.choice(['base_fare', 'cost_per_km', 'cost_per_minutes', 'ride_type_fare', 'surge_percentage'])
    
    if tweak_variable in ['base_fare', 'cost_per_km', 'cost_per_minutes', 'ride_type_fare']:
        new_state[tweak_variable] += random.uniform(-1, 1)
    elif tweak_variable == "surge_percentage":
        new_state[tweak_variable] += random.uniform(-5, 5)
        
    # Ensure values remain positive
    for key in new_state: 
        new_state[key] = float(max(0, new_state[key]))
        
    return new_state

def acceptance_probability(current_cost, new_cost, temperature):
    # Determining the probability of accepting a worse state
    if new_cost < current_cost:
        return 1.0
    return math.exp((current_cost - new_cost) / temperature)

def simulated_annealing(initial_state, competitors_fares, max_iterations=10000, initial_temperature=200, cooling_rate=0.95):
    # Simulated annealing for fare optimization
    current_state = initial_state
    current_cost = objective_function(current_state, competitors_fares)
    best_state = current_state
    best_cost = current_cost
    temperature = initial_temperature
    
    for iteration in range(max_iterations):
        # Generate a neighboring state
        new_state = tweak_states(current_state)
        new_cost = objective_function(new_state, competitors_fares)
        
        # Decide whether to accept the new state
        if new_cost < current_cost or random.random() < acceptance_probability(current_cost, new_cost, temperature):
            current_state  = new_state
            current_cost = new_cost
            
            # Update best state
            if new_cost < best_cost:
                best_state = new_state
                best_cost = new_cost
                
        # Cool down the temperature
        temperature *= cooling_rate
        
        # Terminate early if temperature is very low
        if temperature < 1e-5:
            break
    
    return best_cost, best_state

# Test cases
initial_state = {
    'base_fare': 1645.0,
    'cost_per_km': 65.30,
    'cost_per_minutes': 38.78,
    'ride_type_fare': 130.0,
    'surge_percentage': 10.0,
    'base_cost': 875.0,  # Operational base cost
    'distance_km': 9.4,  # Distance in km
    'time_in_minutes': 16.0  # Time in minutes
}

competitors_fares = [932.0, 186.0, 33.0, 200.0, 26.0]

best_cost, best_state = simulated_annealing(initial_state, competitors_fares)

print("Best State:", best_state)
print("Best Cost:", best_cost)
