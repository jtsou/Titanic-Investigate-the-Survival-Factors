# Titanic

Started by loading titanic dataset.

The project is to investigate what factored in the survival rate of the Titanic tragedy.

I started by importing the libraries first

The libraries are matplotlib.pyplot as plt, numpy as np, pandas as pd, seaborn as sns

Next I started data wranging process:

My way to deal with the missing values is to just drop it. That way, I am able to calculate the data without messing with the original source.For example, the 'Age' column is missing some values, so what I did was that I simply omit that, since '0' means something for age.

After data munging, I started with plots for data visualization purposes. This way, I can have a better idea of what I am looking for in the analysis that might be worth for further analysis.

Conclusion: At life and death, wealthy have higher survival rates; and young females have an advantage.
