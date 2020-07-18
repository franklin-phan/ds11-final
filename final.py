import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

df = pd.read_csv('final-project/Movies2020.csv')


Franklin_score = df['Personal Score']
Franklin_mean = round(np.mean(Franklin_score),2)
print(f'Franklin\'s average score is {Franklin_mean}.')

IMDB_score = df['IMDB Score']
IMDB_mean = round(np.mean(IMDB_score),2)
print(f'IMDB\'s average score is {IMDB_mean}.')

RT_score = df['Rotten Tomatoes Score']
RT_mean = round(np.mean(RT_score),2)
print(f'Rotten Tomatoes\'s average score is {RT_mean}.')

budget = df['Budget (in millions)']
budget_mean = round(np.mean(budget),2)
print(f'The average film budget is {budget_mean} million.')

#question: does budget affect my personal score?
#null hyptothesis: budget does not affect my personal score
# I cannot reject the null hypothesis because 
# the p-value of 0.18 is greater than the significance level of 0.05
# It doesn't mean the null hypothesis is true. It probably means
# that there just isn't enough data.

low_budget_greats = df[ (df['Budget (in millions)'] < 50)]
high_budget_greats = df[ (df['Budget (in millions)'] > 50)]

budget_ttest = ttest_ind(low_budget_greats['Personal Score'], high_budget_greats['Personal Score'])

print(budget_ttest)

# print(df[df['Favorite'] == 'Yes'])

# sns.countplot(x="Favorite",hue="Genre", data=df)

# barplot: personal score vs. budget
# sns.barplot(x="Personal Score", y="Budget (in millions)", data=df)

#bar plot: genre vs. personal score
sorted_bo = df['Box Office'].sort_values()

# sns.barplot(x="Budget (in millions)", y=sorted_bo, data=df)

# plt.boxplot(Franklin_score)
# plt.boxplot(IMDB_score)
# plt.boxplot(RT_score)

filmData = df[["Personal Score","IMDB Score","Rotten Tomatoes Score"]]
sns.heatmap(filmData.corr(), annot=True)
plt.show()