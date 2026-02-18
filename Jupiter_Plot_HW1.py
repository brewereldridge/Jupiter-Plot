import matplotlib.pyplot as plt

# Jupiter and moon data (Jan 9-15) 
az_jup, alt_jup = 291.24, 5.15
az_io,  alt_io  = 291.24, 5.13
az_eur, alt_eur = 291.24, 5.11
az_gan, alt_gan = 291.24, 5.06
az_cal, alt_cal = 291.24, 5.04

#Plot - made bigger because i wasn't able to distinguish between the orbits
plt.figure(figsize=(12, 8))

# Jupiter Path
plt.plot(az_jup, alt_jup, 'go-', label="JUPITER", linestyle='', linewidth=5, markersize=26)

# Moon Paths
plt.plot(az_io, alt_io, color='red', marker='o', linestyle='', label="Io", markersize=6, linewidth=2)
plt.plot(az_eur, alt_eur, color='blue', marker='o', linestyle='', label="Europa", markersize=6, linewidth=2)
plt.plot(az_gan, alt_gan, color='orange', marker='o', linestyle='', label="Ganymede", markersize=6, linewidth=2)
plt.plot(az_cal, alt_cal, color='purple', marker='o', linestyle='', label="Callisto", markersize=6, linewidth=2)


# labels
plt.title("Jupiter System", fontsize=24, fontweight='bold')
plt.xlabel("Azimuth (Degrees)", fontsize=18)
plt.ylabel("Altitude (Degrees)", fontsize=18)

# adjusting ticks
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Zooming in on the data range so it looks bigger
plt.xlim(291.2, 291.3) 
plt.ylim(5, 5.5)

plt.grid(True, linestyle='--', alpha=0.7)

# legend
plt.legend(loc='upper right', fontsize=16, frameon=True, shadow=True)

plt.tight_layout()
#show the plot
plt.show()