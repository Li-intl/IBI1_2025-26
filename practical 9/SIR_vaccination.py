import numpy as np
import matplotlib.pyplot as plt
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000
vaccination_rates = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

plt.figure(figsize=(7, 5), dpi=150)
for vac_rate in vaccination_rates:
    S = int(N * (1 - vac_rate)) - 1
    I = 1
    R = 0
    V = int(N * vac_rate)
    S_list = [S]
    I_list = [I]
    R_list = [R]

    for t in range(time_steps):
        infection_prob = beta * (I / N)
        new_infected = np.random.binomial(S, infection_prob)
        new_recovered = np.random.binomial(I, gamma)

        S -= new_infected
        I += new_infected - new_recovered
        R += new_recovered

        I_list.append(I)

    plt.plot(I_list, label=f'Vaccination {int(vac_rate*100)}%')

plt.xlabel('Time')
plt.ylabel('Number of infected individuals')
plt.title('SIR model with different vaccination rates')
plt.legend(loc='upper right', fontsize=7)
plt.savefig('SIR_vaccination_plot.png')
plt.show()