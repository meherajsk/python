import numpy as np

speed = [86,87,88,86,87,85,86]
speed_1= [32,111,138,28,59,77,97]


x = np.mean(speed)
x_ = np.std(speed)

print(f"range of{x_} from the mean value {x}: {x_*x} \n")

y = np.mean(speed_1)
y_ = np.std(speed_1)

print(f"range of{y_} from the mean value {y}: {y_*y}")

"""
Standard Deviation is often represented by the symbol Sigma: σ
Variance is often represented by the symbol Sigma Squared: σ2
"""
exit(2)