import numpy as np
import scipy.linalg as linalg

#Define the names of your states, can really be anything (strings, char, ints, etc)
state = ["single","married","divorced"]
new_states = np.arange(len(state))

#Define your probability transition Matrix (A)
A = np.array([[0.2,0.6,0.2],[0.3,0.0,0.7],[0.5,0.0,0.5]])
n_columns = len(A)

#Monte Carlo Simulation Algorithm
steps = 10**6
start_state = 0
pi = np.zeros(n_columns)
pi[start_state] = 1
prev_state = start_state

i = 0
while i<steps:
    current_state = np.random.choice(new_states, p=A[prev_state])
    pi[current_state] += 1
    prev_state = current_state
    i += 1

print("pi = ",pi/steps)


