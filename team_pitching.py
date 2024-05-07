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
from pybaseball import team_pitching


pitching = team_pitching(2024)

x_axis = "ERA"
y_axis = "WHIP"

print(pitching)


stl = pitching[(pitching['Team'] == "STL")]
nonstl = pitching[(pitching['Team'] != "STL")]
# cin_hitters = hitters[(hitters['Team'] == "CIN")]

plt.figure(figsize=(20, 20))  # Set the figure size

sns.scatterplot(data=stl, x=x_axis, y=y_axis, color='red', alpha=1, size="W")  # Create scatter plot using seaborn
sns.scatterplot(data=nonstl, x=x_axis, y=y_axis, color='navy', alpha=1, size="W")  # Create scatter plot using seaborn

robotoFont = Font(name='roboto', size=18)

plt.title(x_axis + " vs. " + y_axis, fontsize = 18, fontweight = 'bold', y =1, fontfamily='roboto')  # Set plot title
# plt.suptitle(x_axis + " vs. " + y_axis, fontsize = 18, fontweight = 'bold', y =1)
plt.xlabel(x_axis, fontfamily='roboto')  # Set x-axis label
plt.ylabel(y_axis, fontfamily='roboto')  # Set y-axis label
# plt.gca().invert_yaxis() # Inverts the axis since K% being high is a bad thing
# plt.grid(True)  # Add grid

# Define the range for x-axis tick marks
x_tick_range = np.arange(2, 6.5, .5)  # Start from 0, end at 10 (exclusive), with a step of 2

# Define the range for y-axis tick marks
y_tick_range = np.arange(1, 2, .25)  # Start from 0, end at 20 (exclusive), with a step of 5

# Set x-axis tick marks
plt.xticks(ticks=x_tick_range, fontfamily='roboto')

# Set y-axis tick marks
plt.yticks(ticks=y_tick_range, fontfamily='roboto')


# This section goes through and adds a label to each dot on the scatter plot for the player's name, and then slightly adjusts the vertical positioning of the label to not be touching the dot
for index, row in stl.iterrows():
    plt.text(row[x_axis], row[y_axis] + .02, row["Team"], fontsize=5, ha='center', va='bottom', fontfamily='roboto',bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.2'))

# This section goes through and adds a label to each dot on the scatter plot for the player's name, and then slightly adjusts the vertical positioning of the label to not be touching the dot
for index, row in nonstl.iterrows():
    plt.text(row[x_axis], row[y_axis] + .02, row["Team"], fontsize=5, ha='center', va='bottom', fontfamily='roboto',bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.2'))

plt.show()  # Show plot


