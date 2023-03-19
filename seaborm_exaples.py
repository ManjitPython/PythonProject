import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
data = pd.read_csv("your_dataset.csv")
sns.scatterplot(x="total_bill", y="tip", data=data)
plt.show()