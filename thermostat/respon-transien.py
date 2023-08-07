import numpy as np
import matplotlib.pyplot as plt
import control

# Definisikan plant (sistem termostat)
num = [1]
den = [10, 1]
plant = control.TransferFunction(num, den)

# Waktu simulasi
t = np.linspace(0, 10, 100)

# Kontroler P
Kp = 1
controller_p = control.TransferFunction([Kp], [1])
system_p = control.feedback(controller_p * plant)
t_p, y_p = control.step_response(system_p, T=t)

# Kontroler PI
Kp = 0.8
Ki = 0.2
controller_pi = control.TransferFunction([Kp, Ki], [1, 0])
system_pi = control.feedback(controller_pi * plant)
t_pi, y_pi = control.step_response(system_pi, T=t)

# Kontroler PID
Kp = 0.6
Ki = 0.2
Kd = 0.1
controller_pid = control.TransferFunction([Kp, Ki, Kd], [1, 0])
system_pid = control.feedback(controller_pid * plant)
t_pid, y_pid = control.step_response(system_pid, T=t)

# Plotting grafik respon transien
plt.figure(figsize=(10, 6))
plt.plot(t_p, y_p, label='P')
plt.plot(t_pi, y_pi, label='PI')
plt.plot(t_pid, y_pid, label='PID')
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Transient Response of Thermostat Control System')
plt.legend()
plt.grid(True)
plt.show()
