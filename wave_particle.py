import numpy as np
import matplotlib.pyplot as plt

# Definição da função da onda gaussiana com colapso
def wave_packet(x, t, k0=15, sigma=0.1):
    return np.exp(-(x - 0.2 - 0.015 * t)**2 / (2 * sigma**2)) * np.cos(k0 * (x - 0.2 - 0.015 * t)) * np.exp(-0.2 * t)

# Definir espaço e tempo
x = np.linspace(0, 1, 500)
t_values = np.array([0, 1, 2, 3, 4.01, 5.01, 6.01, 7.01, 8.02, 9.02])

# Criar o gráfico
plt.figure(figsize=(10, 5))

# Plotar a função de onda para diferentes tempos
for i, t in enumerate(t_values):
    color = plt.cm.plasma(i / len(t_values))  # Gradiente de cores para indicar tempo
    plt.plot(x, wave_packet(x, t), color=color, alpha=0.6, label=f"t = {t:.2f} s")

# Adicionando as linhas verticais representando as fases
plt.axvline(0.2, color="green", linestyle="--", label="Constancy (Wave - Continuous Movement)")
plt.axvline(0.55, color="orange", linestyle="--", label="Inconstancy (Measurement - Wave Collapsing)")
plt.axvline(0.75, color="red", linestyle="--", label="End (Collapse - Particle State)")

# Personalização do gráfico
plt.title("Wave-Particle Duality: Constancy, Inconstancy, and End")
plt.xlabel("Position (m)")
plt.ylabel("Wave Function (Ψ)")
plt.legend(loc="upper right", fontsize=8)
plt.grid(True, linestyle="--", alpha=0.6)

# Exibir o gráfico
plt.show()
