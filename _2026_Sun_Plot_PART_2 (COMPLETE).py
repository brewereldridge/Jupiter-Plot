import matplotlib.pyplot as plt
import numpy as np
# DATA
az_noon = [212.36, 212.10, 213.50, 216.24, 220.46, 226.09, 234.43, 241.95, 250.36, 
           256.70,262.09, 263.98, 262.94, 259.36, 252.73, 246.62, 239.73, 234.87, 
           230.15, 226.52, 222.50, 219.44, 216.31, 214.08]

alt_noon = [29.51, 31.84, 35.84, 39.72, 43.76, 47.63, 51.78, 54.57, 57.09, 58.81, 60.44,
            61.46, 62.11, 61.95, 60.42, 57.91, 53.48, 49.02, 43.55, 38.88, 33.92, 30.82,
            28.69, 28.25]

plt.figure(figsize=(10,7))

# Figure 8 path of the sun
plt.plot(az_noon, alt_noon, 'bo-', markersize=4, color='orange')

# Insert tower for reference
tower_width = 5.7
tower_height = 21.8

tower = plt.Rectangle((210,0), tower_width, tower_height, color="blue", alpha=0.5)
plt.gca().add_patch(tower)

# Graph the full sky
plt.xlim(0,360)
plt.ylim(0,90)
plt.grid(True, linestyle=':', alpha=0.6)

#Label
plt.title('Solar Analemma (Cairo 2026)')
plt.ylabel('Altitude (Degrees)')
plt.xlabel('Azimuth (Degrees)')

#Show key
plt.show()