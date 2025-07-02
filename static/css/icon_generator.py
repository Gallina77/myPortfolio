import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set up figure and axis
fig, ax = plt.subplots(figsize=(4, 4))
ax.set_xlim(0, 120)
ax.set_ylim(0, 120)
ax.set_aspect('equal')
#ax.set_facecolor('#EFE9D5')  # background-light

# Draw grid lines <primary-light) (background-light)
grid_color = '#EFE9D5'
ax.plot([40, 40], [10, 110], color=grid_color, linewidth=4)
ax.plot([80, 80], [10, 110], color=grid_color, linewidth=4)
ax.plot([10, 110], [40, 40], color=grid_color, linewidth=4)
ax.plot([10, 110], [80, 80], color=grid_color, linewidth=4)

# Draw an X in the top-left cell (primary-light)
x_color = '#71BBB2'
ax.plot([15, 35], [105, 85], color=x_color, linewidth=5)
ax.plot([35, 15], [105, 85], color=x_color, linewidth=5)

# Draw an O in the center cell (primary-medium)
circle = patches.Circle((60, 60), 12, edgecolor='#f8f9fa', facecolor='none', linewidth=5)
ax.add_patch(circle)

# Hide axes
ax.axis('off')

# Save as PNG
plt.savefig("tic_tac_toe_icon.png", bbox_inches='tight', pad_inches=0.1, transparent=True)
plt.close()