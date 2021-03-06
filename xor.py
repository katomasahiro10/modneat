#usage sample

import random

from modneat import agents

# target inputs and outputs
inputs = [[0,0],[1,0],[0,1],[1,1]]
outputs = [0,1,1,0]

# define populations
a = agents.Agents('ExHebbianNetwork',10,False)

print(a[0].is_automatic_change)
# show first individual
print(a[0].get_output_without_update(inputs[0]))
print(a[0].get_output_without_update(inputs[1]))
print(a[0].get_output_without_update(inputs[2]))
print(a[0].get_output_without_update(inputs[3]))
a[0].show_network('first_individual')

for g in range(1000):
    for n in range(10):
        error = 0.0
        error += (a[n].get_output_with_update(inputs[0])[0] - outputs[0]) ** 2
        error += (a[n].get_output_with_update(inputs[1])[0] - outputs[1]) ** 2
        error += (a[n].get_output_with_update(inputs[2])[0] - outputs[2]) ** 2
        error += (a[n].get_output_with_update(inputs[3])[0] - outputs[3]) ** 2
        a[n].fitness = error * -1
    if(g % 100 == 0):
        print(g, a.average_fitness )

    # evolution
    a = a.evolution(elite_num = 2, mutate_prob = 0.1, sigma = 0.1)

# show best individual
print(a[0].get_output_with_update(inputs[0]))
print(a[0].get_output_with_update(inputs[1]))
print(a[0].get_output_with_update(inputs[2]))
print(a[0].get_output_with_update(inputs[3]))
a[0].show_network('best_individual')
a.save_agents('agents.pickle')
