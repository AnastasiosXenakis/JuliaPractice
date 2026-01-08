import numpy as np
import matplotlib.pyplot as plt

def Sire(S0, I0, R0, beta, gamma, dt, T):

    N = int(T/dt) # Antall steg = tid/steglengde

    S = np.zeros(N)             # Klargjøre arrays
    I = np.zeros(N)             
    R = np.zeros(N)             
    t = np.linspace(0, T, N)

    S[0], I[0], R[0] = S0, I0, R0 # Startverdier

    
    # Magien skjer:
    for i in range(N - 1):
        dS = -beta * S[i] * I[i] * dt
        dI = (beta * S[i] * I[i] - gamma * I[i] ) * dt
        dR = gamma * I[i] * dt

        S[i + 1] = S[i] + dS
        I[i + 1] = I[i] + dI
        R[i + 1] = R[i] + dR

        return t, S, I, R

# Parametre
S0 = 990
I0 = 10
R0 = 0
beta = 0.39
gamma = 1/10
dt = 0.001
T = 1

# mer tasosmagi
t, S, I, R = Sire(S0, I0, R0, beta, gamma, dt, T)

plt.plot(t, S)
plt.plot(t, I)
plt.plot(t, R)
plt.xlabel("tid")
plt.ylabel("populasjon")
plt.title("SIR-modellen ved help av eulers metode")
plt.legend()
plt.grid()
plt.show()
