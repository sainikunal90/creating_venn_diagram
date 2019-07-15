from matplotlib_venn import venn2, venn2_circles
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np 


#BC & GPL Loading
df1 = pd.read_csv(r'C:\Python Scripts\suresh venn\BC_N_GPL.csv',dtype='unicode')
df11 = pd.DataFrame(df1)
a = df11['temp.mask'].values.tolist()

#Casual Games Loading
df2 = pd.read_csv(r'C:\Python Scripts\suresh venn\CASUAL_GAMES.csv',dtype='unicode')
df22 = df2['910957911592']
df222 = pd.DataFrame(df22)
b = df222['910957911592'].values.tolist()


#Fantasy Games Loading
df3 = pd.read_csv(r'C:\Python Scripts\suresh venn\FANTASY.csv',dtype='unicode')
df33 = df3['910957567616']
df333 = pd.DataFrame(df33)
c = df333['910957567616'].values.tolist()

lst1 = a
lst2 = b
lst3 = c

venn3([set(lst1), set(lst2), set(lst3)])

venn3([set(lst1), set(lst2), set(lst3)], set_labels = ('BC & GPL    ', '    CASUAL GAMES', 'Fantasy'))
plt.title('User behaviour of game usage\n')
plt.show()