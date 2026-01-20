import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

k = ctrl.Antecedent(np.arange(11), 'keywords')
p = ctrl.Antecedent(np.arange(11), 'punctuation')
s = ctrl.Consequent(np.arange(101), 'spam')

k['low'] = fuzz.trimf(k.universe, [0, 0, 5])     # Few keywords
k['high'] = fuzz.trimf(k.universe, [5, 10, 10])  # Many keywords

p['low'] = fuzz.trimf(p.universe, [0, 0, 5])     # Few punctuation marks
p['high'] = fuzz.trimf(p.universe, [5, 10, 10])  # Many punctuation marks

s['safe'] = fuzz.trimf(s.universe, [0, 0, 50])    # Not spam
s['spam'] = fuzz.trimf(s.universe, [50, 100, 100])# Spam

r1 = ctrl.Rule(k['high'] | p['high'], s['spam'])

r2 = ctrl.Rule(k['low'] & p['low'], s['safe'])

sim = ctrl.ControlSystemSimulation(ctrl.ControlSystem([r1, r2]))

sim.input['keywords'] = 20       # Many suspicious words
sim.input['punctuation'] = 4    # Moderate punctuation

sim.compute()

# Display final spam probability
print("Spam Probability:", round(sim.output['spam'], 2), "%")
