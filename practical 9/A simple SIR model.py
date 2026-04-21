import numpy as np
import matplotlib.pyplot as plt

N = 10000          
beta = 0.3         
gamma = 0.05       
time_steps = 1000  

S = N - 1
I = 1
R = 0

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
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)


plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')

plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.title('Stochastic SIR Model')
plt.legend()
plt.savefig('SIR_plot.png')  
plt.show()