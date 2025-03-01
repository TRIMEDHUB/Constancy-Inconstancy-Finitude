import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema (Oscilador Amortecido)
m = 1.0      # Massa (kg)
k = 10.0     # Constante da mola (N/m)
b = 0.5      # Coeficiente de amortecimento (N.s/m)
x0 = 5.0     # Deslocamento inicial (m)
v0 = 0.0     # Velocidade inicial (m/s)

# Função para calcular a solução analítica
def oscilador_amortecido(t, m, k, b, x0, v0):
    gamma = b / (2 * m)
    omega_0 = np.sqrt(k / m)
    omega = np.sqrt(omega_0**2 - gamma**2)
    A = np.sqrt(x0**2 + (v0 + gamma * x0)**2 / omega**2)
    phi = np.arctan((v0 + gamma * x0) / (omega * x0))
    x_t = A * np.exp(-gamma * t) * np.cos(omega * t - phi)
    return x_t

# Tempo de simulação
t = np.linspace(0, 20, 1000)

# Cálculo da solução
x_analitico = oscilador_amortecido(t, m, k, b, x0, v0)

# Criar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(t, x_analitico, label="Displacement (m)", color="blue", linestyle="-")

# Marcar as fases
plt.text(2, 3, "Constancy", color="green", fontsize=12)
plt.text(7, 2, "Inconstancy", color="orange", fontsize=12)
plt.text(17, 0.5, "End", color="red", fontsize=12)

# Personalização do gráfico
plt.title("Damped Oscillator: Constancy, Inconstancy, and End")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.axhline(0, color='black', linewidth=0.5)
plt.legend(loc="upper right")
plt.grid(True, linestyle="--", alpha=0.6)

# Exibir o gráfico
plt.show()
