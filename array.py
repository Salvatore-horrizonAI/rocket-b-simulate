import numpy as np
import matplotlib.pyplot as plt


massa_iniziale = 50000  
massa_carburante = 40000 
massa_finale = massa_iniziale - massa_carburante
spinta = 2000000  
tasso_consumo = 5000 
g = 9.81  
angolo_lancio = np.radians(80)  
tempo_di_bruciatura = massa_carburante / tasso_consumo

dt = 0.1  
t = np.arange(0, tempo_di_bruciatura + 100, dt)  
x = np.zeros_like(t)
y = np.zeros_like(t)
vx = np.zeros_like(t)
vy = np.zeros_like(t)
massa = np.zeros_like(t)
massa[0] = massa_iniziale
for i in range(1, len(t)):
    if t[i] <= tempo_di_bruciatura:
        
        massa[i] = massa[i-1] - tasso_consumo * dt
        accelerazione = spinta / massa[i-1]  
        ax = accelerazione * np.cos(angolo_lancio)
        ay = accelerazione * np.sin(angolo_lancio) - g
    else:
        massa[i] = massa_finale
        ax = 0
        ay = -g  
    
    
    vx[i] = vx[i-1] + ax * dt
    vy[i] = vy[i-1] + ay * dt
    x[i] = x[i-1] + vx[i] * dt
    y[i] = y[i-1] + vy[i] * dt
   
    if y[i] < 0:
        break


x = x[:i+1]
y = y[:i+1]
t = t[:i+1]
plt.figure(facecolor="black", figsize=(12, 7))
plt.plot(x, y, color="cyan", linewidth=2)
plt.title("Rocket-B  - Traiettoria di un razzo simulazione", color="white")
plt.xlabel("Distanza orizzontale (m)", color="white")
plt.ylabel("Altitudine (m)", color="white")
plt.grid(True, color="gray", linestyle="--", alpha=0.5)
plt.axhline(0, color="white", linestyle=":")  
plt.legend()
ax = plt.gca()
ax.set_facecolor('black')
ax.tick_params(colors='white')
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
plt.show()