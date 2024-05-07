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


# hitters = batting_stats(2024, qual=100)
teams = team_batting(2024)
print(teams)

x_axis = "R"
y_axis = "EV"

# Filter players who hit over 30 home runs
cardinals = hitters # [(hitters['Team'] == "STL")]
cardinals = cardinals.sort_values(by='EV', ascending=True)


# Display the filtered DataFrame
print(cardinals)

plt.figure(figsize=(14, 12))  # Set the figure size
sns.scatterplot(data=teams, x=x_axis, y=y_axis, color='blue', alpha=0.75)  # Create scatter plot using seaborn
plt.title(x_axis + " vs. " + y_axis)  # Set plot title
plt.xlabel(x_axis)  # Set x-axis label
plt.ylabel(y_axis)  # Set y-axis label
plt.grid(True)  # Add grid

for index, row in teams.iterrows():
    plt.text(row[x_axis], row[y_axis] + .05, row["Team"], fontsize=8, ha='center', va='bottom')

plt.show()  # Show plot


