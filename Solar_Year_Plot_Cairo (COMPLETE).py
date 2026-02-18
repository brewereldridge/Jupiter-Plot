import matplotlib.pyplot as plt

# Data is pulled from Horizon System 
# Target: Sun, Location: Cairo, Egypt, Time: 2026

ra = [18.74, 19.76, 20.95, 21.88, 22.77, 23.63, 0.67, 1.53, 2.55, 3.48, 4.64, 5.61, 
      6.72, 7.68, 8.77, 9.64, 10.67, 11.52, 12.50, 13.38, 14.47, 15.41, 16.51, 17.47]

dec = [-23.04, -21.22, -17.26, -12.87, -7.8, -2.25, 4.46, 9.75, 15.06, 18.88, 22.05, 23.31, 
       23.09, 21.48,18.08, 14.21, 8.40, 3.15, -3.07, -8.48, -14.47, -18.55, -21.81, -23.26]

# RA vs DEC

plt.figure(figsize=(10,5))
plt.plot(ra,dec,'ro', color='orange') #switched from "ro-" to avoid lines overlapping
plt.axhline(0, color='blue', linewidth=1) #equator for reference
plt.xlabel('Right ascension (Decimal Hours)')
plt.ylabel("Declination (Degrees)")
plt.grid(True, linestyle ='--',alpha=0.6)
plt.legend()

#Show Graph
plt.show()