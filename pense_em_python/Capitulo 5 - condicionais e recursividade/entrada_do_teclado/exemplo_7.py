import math
signal_power1 = 9
noise_power1 = 10
ratio1 = signal_power1 / (noise_power1)
decibels1 = 10 * math.log10(ratio1)
print(decibels1)

