"""
Efficiency plot
===============

Compare the ratio between two histograms h1 and h2 when the entries of h1 are a subset of the entries of h2. Only plot the efficiency comparison.
"""

# Set the seed for the .sample() method
import numpy as np

np.random.seed(8311311)

from plothist import get_dummy_data

df = get_dummy_data()

name = "variable_1"

x_total = df[name][df["category"] == 2]
x_sample = x_total.sample(frac=0.75) # x_sample is a subset of x_total

x_range = (min(x_total), max(x_total))

from plothist import make_hist

h_sample = make_hist(x_sample, bins=50, range=x_range)
h_total = make_hist(x_total, bins=50, range=x_range)

###
import matplotlib.pyplot as plt
from plothist import plot_comparison

fig, ax = plt.subplots()

plot_comparison(h_sample, h_total, ax=ax, xlabel=name, comparison="efficiency")

fig.savefig("1d_comparison_only_efficiency.svg", bbox_inches="tight")
