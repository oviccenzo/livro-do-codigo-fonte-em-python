import math
signal_power2 = 9
noise_power2 = 10
ratio2 = signal_power2 % (noise_power2)
decibels2 = 10 * math.log10(ratio2)
print(decibels2)