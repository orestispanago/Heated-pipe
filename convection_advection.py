import matplotlib.pyplot as plt
import numpy as np

L = 50  # m, pipe length
r = 0.1  # m, pipe radius
n = 100  # nodes used
mdot = 3  # kg/s
Cp = 4180  # J/(kg*K) heat capacity of water
rho = 1000  # kg/m3 density of water

Tin = 400  # K pipe inlet temperature
T0 = 300  # pipe initial temperature

q_flux = 100000  # W/m2 heat flux into fluid

t_final = 700  # s, final simulation time
dt = 1  # s, time step
dx = L / n  # m, node width

x = np.linspace(dx / 2, L - dx / 2, n)
T = np.ones(n) * T0

dTdt = np.zeros(n)

Tss = Tin + q_flux * 2 * np.pi * r * x / (mdot * Cp)

t = np.arange(0, t_final, dt)


for i in range(1, len(t)):
    plt.figure(1)
    plt.clf()
    dTdt[1:n] = (
        mdot * Cp * (T[0 : n - 1] - T[1:n]) + q_flux * 2 * np.pi * r * dx
    ) / (rho * Cp * dx * np.pi * r ** 2)
    dTdt[0] = (mdot * Cp * (Tin - T[0]) + q_flux * 2 * np.pi * r * dx) / (
        rho * Cp * dx * np.pi * r ** 2
    )
    T = T + dTdt * dt
    # plt.clf()
    plt.plot(x, Tss, label="Steady-state")
    plt.plot(x, T, label="Transient")
    plt.title(f"Time: {t[i]} s")
    plt.ylabel("Temperature (K)")
    plt.xlabel("Distance (m)")
    plt.legend()
    # plt.show()
    plt.pause(0.05)
