import matplotlib.pyplot as plt
import numpy as np

# 1. Plot the sun
# use the scatter function to plot a single point. scale the size to make it look like the sun. s=300 or higher
# sun azimuth is 180 degrees. altitude is 43.8
plt.scatter(180.0, 43.8, color='yellow', s=300, label="Sun")

# 2. Plot the tower (shade in)
# tower is centered at 180. width is 5.7m. 180 - 5.7/2 = 177.15
left_edge = 177.15
tower = plt.Rectangle((left_edge, 0), 5.7, 21.8, color='orange', label="Tower (40m)")
plt.gca().add_patch(tower)

# 3. Set the view limits so the POV looks right
plt.xlim(0,360)
plt.ylim(0,90)

# 4. Labels
plt.xlabel('Azimuth (Degrees)')
plt.ylabel('Altitude (Degrees)')
plt.title('Solar Position vs Tower Position (Cairo - Feb 4th, 2026)')
plt.legend()

# 5. Show the window
plt.show()