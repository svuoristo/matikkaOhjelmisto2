import numpy as np
from tabulate import tabulate

# t. 1
print("t. 1.1")
print(f"a) {round(np.degrees(2.493), 1)}")
print(f"b) {round(np.degrees(0.911), 1)}")

# t. 2
print("\nt. 1.2")
print(f"a) {round(np.radians(137.7), 3)}")
print(f"b) {round(np.radians(62.3), 3)}")

# t. 3
print("\nt. 1.3")
degrees = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
angles = []

for degree in degrees:
    angles.append([degree, np.radians(degree)])

print(tabulate(angles, headers=['asteet', 'radiaanit'],tablefmt="grid"))