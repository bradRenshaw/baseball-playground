import requests
import json
import openpyxl
import numpy as np
import pandas as pd
import pybaseball as pb
import matplotlib.pyplot as plt
import seaborn as sns
from pybaseball import batting_stats
from pybaseball import team_batting
from openpyxl.styles import Font

hitters = batting_stats(2024, qual=25)

x_axis = "OPS"
y_axis = "K%"

print(hitters)

stl_hitters = hitters[(hitters['Team'] == "STL")]
nonstl_hitters = hitters[(hitters['Team'] != "STL")]
# cin_hitters = hitters[(hitters['Team'] == "CIN")]

plt.figure(figsize=(20, 20))  # Set the figure size

sns.scatterplot(data=stl_hitters, x=x_axis, y=y_axis, color='red', alpha=1, size="AB")  # Create scatter plot using seaborn
sns.scatterplot(data=nonstl_hitters, x=x_axis, y=y_axis, color='navy', alpha=1, size="AB")  # Create scatter plot using seaborn

robotoFont = Font(name='roboto', size=18)

plt.title(x_axis + " vs. " + y_axis, fontsize = 18, fontweight = 'bold', y =1, fontfamily='roboto')  # Set plot title
# plt.suptitle(x_axis + " vs. " + y_axis, fontsize = 18, fontweight = 'bold', y =1)
plt.xlabel(x_axis, fontfamily='roboto')  # Set x-axis label
plt.ylabel(y_axis, fontfamily='roboto')  # Set y-axis label
plt.gca().invert_yaxis() # Inverts the axis since K% being high is a bad thing
# plt.grid(True)  # Add grid

# Define the range for x-axis tick marks
x_tick_range = np.arange(0, 1.5, .25)  # Start from 0, end at 10 (exclusive), with a step of 2

# Define the range for y-axis tick marks
y_tick_range = np.arange(0, .5, .05)  # Start from 0, end at 20 (exclusive), with a step of 5

# Set x-axis tick marks
plt.xticks(ticks=x_tick_range, fontfamily='roboto')

# Set y-axis tick marks
plt.yticks(ticks=y_tick_range, fontfamily='roboto')


# This section goes through and adds a label to each dot on the scatter plot for the player's name, and then slightly adjusts the vertical positioning of the label to not be touching the dot
for index, row in stl_hitters.iterrows():
    plt.text(row[x_axis], row[y_axis] + .01, row["Name"], fontsize=6, ha='center', va='bottom', fontfamily='roboto',bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.2'))

# for index, row in nonstl_hitters.iterrows():
#     plt.text(row[x_axis], row[y_axis] + .01, row["Name"], fontsize=6, ha='center', va='bottom', fontfamily='roboto')

plt.show()  # Show plot



