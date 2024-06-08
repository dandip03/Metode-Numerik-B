import numpy as np
import matplotlib.pyplot as plt
import time

def riemann_integration(f, a, b, N):
    dx = (b - a) / N
    total = 0.0
    for i in range(N):
        xi = a + (i + 0.5) * dx
        total += f(xi)
    return total * dx

def f(x):
    return 4 / (1 + x**2)

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

results = []
errors = []
times = []

for N in N_values:
    start_time = time.time()
    pi_approx = riemann_integration(f, 0, 1, N)
    end_time = time.time()
    
    error = np.sqrt((pi_approx - pi_ref)**2)
    exec_time = end_time - start_time
    
    results.append(pi_approx)
    errors.append(error)
    times.append(exec_time)

# Plotting results
plt.figure(figsize=(12, 6))

# Plotting approximation vs N
plt.subplot(1, 3, 1)
plt.plot(N_values, results, marker='o')
plt.axhline(y=pi_ref, color='r', linestyle='--', label='Referensi pi')
plt.xscale('log')
plt.xlabel('N')
plt.ylabel('Nilai pi aproksimasi')
plt.title('Aproksimasi pi vs N')
plt.legend()

# Plotting error vs N
plt.subplot(1, 3, 2)
plt.plot(N_values, errors, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('Galat RMS')
plt.title('Galat RMS vs N')

# Plotting execution time vs N
plt.subplot(1, 3, 3)
plt.plot(N_values, times, marker='o')
plt.xscale('log')
plt.xlabel('N')
plt.ylabel('Waktu Eksekusi (detik)')
plt.title('Waktu Eksekusi vs N')

plt.tight_layout()
plt.show()