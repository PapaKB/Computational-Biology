import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import spearmanr, pearsonr, kendalltau

##The idea of the tutorials is to explore the questions on the sheet and add more to them by identifying 
##pattern etc.
# WEEK 1


# TASK 1
# Sheet name doesn't have to be specified as there is only one sheet in the folder
df = pd.read_excel('Cell-Cycle-Set.xlsx', sheet_name=0) 

# This drops any rows or columns with NaN values
df.dropna(inplace=True)


# TASK 2.1
# Creating a figure to have multiple histograms on it
fig, ax1 = plt.subplots()

# Adding two histograms to one figure
ax1.hist(df.mean_RNA_G1, label='RNA')
ax1.hist(df.mean_protein_G1, label='Protein')

# Shows legend
ax1.legend()

# Prints data from excel sheet
# print(df)

# Shows grid lines
plt.grid()

#labelling axes and adding title
ax1.set_title('Histogram of G1 Expression')
ax1.set_xlabel('Mean G1 expression')
ax1.set_ylabel('Frequency')

# Must use show() otherwise the histogram will not be presented
plt.show()


# Task 2.2
# corr returns a tuple. The first value is the correlation and the second is the probability that two uncorrelated 
# variables would return the same result
g1Pearson = df['mean_RNA_G1'].corr(df['mean_protein_G1'], method=pearsonr)[0]
g1Spearman = df['mean_RNA_G1'].corr(df['mean_protein_G1'], method=spearmanr)[0]
g1Kendall = df['mean_RNA_G1'].corr(df['mean_protein_G1'], method=kendalltau)[0]

sPearson = df['mean_RNA_S'].corr(df['mean_protein_S'], method=pearsonr)[0]
sSpearman = df['mean_RNA_S'].corr(df['mean_protein_S'], method=spearmanr)[0]
sKendall = df['mean_RNA_S'].corr(df['mean_protein_S'], method=kendalltau)[0]


g2Pearson = df['mean_RNA_G2'].corr(df['mean_protein_G2'], method=pearsonr)[0]
g2Spearman = df['mean_RNA_G2'].corr(df['mean_protein_G2'], method=spearmanr)[0]
g2Kendall = df['mean_RNA_G2'].corr(df['mean_protein_G2'], method=kendalltau)[0]

print('''G1 RNA and Protein correlation:\n 	Pearson = %f\n 	Spearman = %f\n 	Kendall = %f
S RNA and Protein correlation:\n 	Pearson = %f\n 	Spearman = %f\n 	Kendall = %f
G2 RNA and Protein correlation:\n 	Pearson = %f\n 	Spearman = %f\n 	Kendall = %f'''
	% (g1Pearson, g1Spearman, g1Kendall, sPearson, sSpearman, sKendall, g2Pearson, g2Spearman, g2Kendall))	


# TASK 2.3
# (ax2, ax3, ax4) means three sets of axes will be shown in one row
fig, (ax2, ax3, ax4) = plt.subplots(1, 3)
fig.set_size_inches(15,5)
ax2.scatter(df.mean_RNA_G1, df.mean_protein_G1, label='r={:0.2f}(Spearman),'.format(
            g1Spearman) + '\n{:0.2f}(Pearson),'.format(g1Pearson) + '\n{:0.2f}(Kendall)'.format(g1Kendall))
ax2.set_title('Mean RNA G1 vs Mean Protein G1')
ax2.set_xlabel('Mean RNA G1')
ax2.set_ylabel('Mean Protein G1')

ax3.scatter(df.mean_RNA_S, df.mean_protein_S, color='red', label='r={:0.2f}(Spearman),'.format(
            sSpearman) + '\n{:0.2f}(Pearson),'.format(sPearson) + '\n{:0.2f}(Kendall)'.format(sKendall))
ax3.set_title('Mean RNA S vs Mean Protein S')
ax3.set_xlabel('Mean RNA S')
ax3.set_ylabel('Mean Protein S')

ax4.scatter(df.mean_RNA_G2, df.mean_protein_G2, color='green', label='r={:0.2f}(Spearman),'.format(
            g2Spearman) + '\n{:0.2f}(Pearson),'.format(g2Pearson) + '\n{:0.2f}(Kendall)'.format(g2Kendall))
ax4.set_title('Mean RNA G2 vs Mean Protein G2')
ax4.set_xlabel('Mean RNA G2')
ax4.set_ylabel('Mean Protein G2')

ax2.legend()
ax3.legend()
ax4.legend()

plt.show()

# WEEK 2
# TASK 1
# gobp contains entries from the sheet where there GOBP field contains 'cell cycle'
gobp = df[df.GOBP.str.contains('cell cycle')]
fig, ax5 = plt.subplots(1,3)
fig.set_size_inches(15,5)

# You can index on one axes variable to create multiple axes but the number must be specified in subplots
# Note that a marker field can be added in scatter to change the shape of plots
# alpha can be used as a fiels in scatter to change the transparency of plots
ax5[0].scatter(df.mean_RNA_G1, df.mean_protein_G1, color='blue', label='No filter', alpha=0.6)
ax5[0].scatter(gobp.mean_RNA_G1, gobp.mean_protein_G1, color='red', label='GOBP contains \'cell cycle\'', alpha=0.6)
ax5[0].set_title('Mean RNA G1 Vs Mean Protein G1')
ax5[0].set_ylabel('Mean Protein')
ax5[0].set_xlabel('Mean RNA')
ax5[0].legend()

ax5[1].scatter(df.mean_RNA_S, df.mean_protein_S, color='blue', label='No filter', alpha=0.6)
ax5[1].scatter(gobp.mean_RNA_S, gobp.mean_protein_S, color='red', label='GOBP contains \'cell cycle\'', alpha=0.6)
ax5[1].set_title('Mean RNA S Vs Mean Protein S')
ax5[1].set_ylabel('Mean Protein')
ax5[1].set_xlabel('Mean RNA')
ax5[1].legend()

ax5[2].scatter(df.mean_RNA_G2, df.mean_protein_G2, color='blue', label='No filter', alpha=0.6)
ax5[2].scatter(gobp.mean_RNA_G2, gobp.mean_protein_G2, color='red', label='GOBP contains \'cell cycle\'',alpha=0.6)
ax5[2].set_title('Mean RNA G2 Vs Mean Protein G2')
ax5[2].set_ylabel('Mean Protein')
ax5[2].set_xlabel('Mean RNA')
ax5[2].legend()

plt.show()

gobpG1Pearson = gobp['mean_protein_G1'].corr(gobp['mean_RNA_G1'], method=pearsonr)[0]
gobpSPearson = gobp['mean_protein_S'].corr(gobp['mean_RNA_S'], method=pearsonr)[0]
gobpG2Pearson = gobp['mean_protein_G2'].corr(gobp['mean_RNA_G2'], method=pearsonr)[0]

print('''G1 Pearson correlation where GOBP contains \'cell cycle\' = %f
S Pearson correlation where GOBP contains \'cell cycle\' = %f
G2 Pearson correlation where GOBP contains \'cell cycle\' = %f'''% (gobpG1Pearson, gobpSPearson, gobpG2Pearson))

# TASK 2
# gocc contains entries from the sheet where there GOBP field contains 'ribosome'
gocc = df[df.GOCC.str.contains('ribosome')]
fig, ax6 = plt.subplots(1,3)
fig.set_size_inches(15,5)

# Note that a marker field can be added in scatter to change the shape of plots
ax6[0].scatter(df.mean_RNA_G1, df.mean_protein_G1, color='blue', label='No filter', alpha=0.6)
ax6[0].scatter(gocc.mean_RNA_G1, gocc.mean_protein_G1, color='red', label='GOCC contains \'ribosome\'', alpha=0.6)
ax6[0].set_title('Mean RNA G1 Vs Mean Protein G1')
ax6[0].set_ylabel('Mean Protein')
ax6[0].set_xlabel('Mean RNA')
ax6[0].legend()

ax6[1].scatter(df.mean_RNA_S, df.mean_protein_S, color='blue', label='No filter', alpha=0.6)
ax6[1].scatter(gocc.mean_RNA_S, gocc.mean_protein_S, color='red', label='GOCC contains \'ribosome\'', alpha=0.6)
ax6[1].set_title('Mean RNA S Vs Mean Protein S')
ax6[1].set_ylabel('Mean Protein')
ax6[1].set_xlabel('Mean RNA')
ax6[1].legend()

ax6[2].scatter(df.mean_RNA_G2, df.mean_protein_G2, color='blue', label='No filter', alpha=0.6)
ax6[2].scatter(gocc.mean_RNA_G2, gocc.mean_protein_G2, color='red', label='GOCC contains \'ribosome\'', alpha=0.6)
ax6[2].set_title('Mean RNA G2 Vs Mean Protein G2')
ax6[2].set_ylabel('Mean Protein')
ax6[2].set_xlabel('Mean RNA')
ax6[2].legend()

plt.show()

goccG1Pearson = gocc['mean_protein_G1'].corr(gocc['mean_RNA_G1'], method=pearsonr)[0]
goccSPearson = gocc['mean_protein_S'].corr(gocc['mean_RNA_S'], method=pearsonr)[0]
goccG2Pearson = gocc['mean_protein_G2'].corr(gocc['mean_RNA_G2'], method=pearsonr)[0]

print('''G1 Pearson correlation where GOCC contains \'ribosome\' = %f
S Pearson correlation where GOCC contains \'ribosome\' = %f
G2 Pearson correlation where GOCC contains \'ribosome\' = %f'''% (goccG1Pearson, goccSPearson, goccG2Pearson))

# TASK 3
"""
expand = true will return a dataframe where for each entry each word from the GOBP field will be in a separate
column, whereas expand = false would return a series(a type of list) of GOBP terms for each entry in one column. 
stack() reformats this new dataframe so that there will essentially be one column with subsections(indexes)
for each GOBP term the entry has. value_counts() counts across all entries how many times a GOBP term appears.
""" 
print(df.GOBP.str.split(';',expand=True).stack().value_counts())

# TASK 4
# Create new fields in the data for the differences in mean proteins and mean RNAs for G1-S, S-G2, G2-G1
df['mean_RNA_G1S'] = df.mean_RNA_S-df.mean_RNA_G1
df['mean_protein_G1S'] = df.mean_protein_S-df.mean_protein_G1
df['mean_RNA_SG2'] = df.mean_RNA_G2-df.mean_RNA_S
df['mean_protein_SG2'] = df.mean_protein_G2-df.mean_protein_S
df['mean_RNA_G2G1'] = df.mean_RNA_G1-df.mean_RNA_G2
df['mean_protein_G2G1'] = df.mean_protein_G1-df.mean_protein_G2

""" 
Creating a function to mean center and variance scale the values.
Mean centering is subtracting the mean of all values in the column from each value so the new mean
of the column will be 0. Varaince scaling means dividing by standard deviation of column
"""
meanCenterAndScale = lambda x : (x - x.mean())/ x.std()

# iloc is needed to select a colum in a dataframe
#[:,-6:] the comma refers to the column in the dataframe, so ,-6: means from the sixth last column to the last
df.iloc[:,-6:] = meanCenterAndScale(df.iloc[:,-6:])

# 3 separate graphs each for tthe pairs of preotein and rna qith three scatterplots. One for protein
# vs rna, another for the same with gobp and another for gocc
gobp = df[df.GOBP.str.contains('cell cycle')]
gocc = df[df.GOCC.str.contains('ribosome')]

fig, (ax7, ax8, ax9) = plt.subplots(1, 3)
fig.set_size_inches(15,5)

ax7.scatter(df.mean_RNA_G1S, df.mean_protein_G1S, color='red', label='No filter')
ax7.scatter(gobp.mean_RNA_G1S, gobp.mean_protein_G1S, color='blue', label='GOBP contains \'cell cycle\'')
ax7.scatter(gocc.mean_RNA_G1S, gocc.mean_protein_G1S, color='green', label='GOCC contains \'ribosome\'')

ax8.scatter(df.mean_RNA_SG2, df.mean_protein_SG2, color='red', label='No filter')
ax8.scatter(gobp.mean_RNA_SG2, gobp.mean_protein_SG2, color='blue', label='GOBP contains \'cell cycle\'')
ax8.scatter(gocc.mean_RNA_SG2, gocc.mean_protein_SG2, color='green', label='GOCC contains \'ribosome\'')

ax9.scatter(df.mean_RNA_G2G1, df.mean_protein_G2G1, color='red', label='No filter')
ax9.scatter(gobp.mean_RNA_G2G1, gobp.mean_protein_G2G1, color='blue', label='GOBP contains \'cell cycle\'')
ax9.scatter(gocc.mean_RNA_G2G1, gocc.mean_protein_G2G1, color='green', label='GOCC contains \'ribosome\'')

ax7.set_title('Mean RNA G1S vs Mean Protein G1S')
ax7.set_ylabel('Mean protein G1S')
ax7.set_xlabel('Mean RNA G1S')
ax7.legend()

ax8.set_title('Mean RNA SG2 vs Mean Protein SG2')
ax8.set_ylabel('Mean protein SG2')
ax8.set_xlabel('Mean RNA SG2')
ax8.legend()

ax9.set_title('Mean RNA G2G1 vs Mean Protein G2G1')
ax9.set_ylabel('Mean protein G2G1')
ax9.set_xlabel('Mean RNA G2G1')
ax9.legend()
plt.show()
