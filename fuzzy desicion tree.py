import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define the input criteria as fuzzy variables
charge_sensitivity = ctrl.Antecedent(np.arange(0, 11, 1), 'charge_sensitivity')
size_sensitivity = ctrl.Antecedent(np.arange(0, 11, 1), 'size_sensitivity')
trajectory_impact = ctrl.Antecedent(np.arange(0, 11, 1), 'trajectory_impact')

# Define the output (choice of nanopore geometry) as a fuzzy variable
geometry_choice = ctrl.Consequent(np.arange(0, 11, 1), 'geometry_choice')

# Define fuzzy membership functions for each input
charge_sensitivity['low'] = fuzz.trimf(charge_sensitivity.universe, [0, 0, 5])
charge_sensitivity['medium'] = fuzz.trimf(charge_sensitivity.universe, [0, 5, 10])
charge_sensitivity['high'] = fuzz.trimf(charge_sensitivity.universe, [5, 10, 10])

size_sensitivity['low'] = fuzz.trimf(size_sensitivity.universe, [0, 0, 5])
size_sensitivity['medium'] = fuzz.trimf(size_sensitivity.universe, [0, 5, 10])
size_sensitivity['high'] = fuzz.trimf(size_sensitivity.universe, [5, 10, 10])

trajectory_impact['low'] = fuzz.trimf(trajectory_impact.universe, [0, 0, 5])
trajectory_impact['medium'] = fuzz.trimf(trajectory_impact.universe, [0, 5, 10])
trajectory_impact['high'] = fuzz.trimf(trajectory_impact.universe, [5, 10, 10])

# Define fuzzy membership functions for output (geometry choice)
geometry_choice['conical'] = fuzz.trimf(geometry_choice.universe, [0, 0, 5])
geometry_choice['cigar'] = fuzz.trimf(geometry_choice.universe, [0, 5, 10])
geometry_choice['hourglass'] = fuzz.trimf(geometry_choice.universe, [5, 10, 10])

# Define the rules for the fuzzy decision tree
rule1 = ctrl.Rule(charge_sensitivity['high'] & size_sensitivity['low'], geometry_choice['conical'])
rule2 = ctrl.Rule(charge_sensitivity['high'] & size_sensitivity['high'] & trajectory_impact['medium'], geometry_choice['cigar'])
rule3 = ctrl.Rule(charge_sensitivity['low'] & size_sensitivity['high'], geometry_choice['hourglass'])
rule4 = ctrl.Rule(charge_sensitivity['medium'] & trajectory_impact['high'], geometry_choice['cigar'])
rule5 = ctrl.Rule(size_sensitivity['high'] & trajectory_impact['low'], geometry_choice['hourglass'])

# Control system creation and simulation
geometry_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
geometry_simulation = ctrl.ControlSystemSimulation(geometry_ctrl)

# Example inputs
geometry_simulation.input['charge_sensitivity'] = 7  # High charge sensitivity
geometry_simulation.input['size_sensitivity'] = 6    # High size sensitivity
geometry_simulation.input['trajectory_impact'] = 3   # Low trajectory impact

# Perform fuzzy inference
geometry_simulation.compute()

# Output result
print(f"Geometry choice (fuzzy score): {geometry_simulation.output['geometry_choice']}")

# Visualize the result
geometry_choice.view(sim=geometry_simulation)
plt.show()
