import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils import resample

# Load the dataset
df = pd.read_csv('Text-Summarizar\\essays.csv')

# Check the class distribution
print(df['ext'].value_counts())

# Separate majority and minority classes based on the 'ext' column
majority_class = df[df['ext'] == 0]  # Majority class where 'ext' is 0
minority_class = df[df['ext'] == 1]  # Minority class where 'ext' is 1

# Undersample majority class to match minority class size
majority_undersampled = resample(majority_class,
                                 replace=False,  # without replacement
                                 n_samples=len(minority_class),  # match the minority class size
                                 random_state=42)

# Combine the undersampled majority class with the minority class
df_undersampled = pd.concat([majority_undersampled, minority_class])

# Visualizing the class distribution before and after undersampling

# Before undersampling
plt.figure(figsize=(8, 6))
sns.countplot(x='ext', data=df, palette='Set2')
plt.title('Class Distribution Before Undersampling')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()

# After undersampling
plt.figure(figsize=(8, 6))
sns.countplot(x='ext', data=df_undersampled, palette='Set2')
plt.title('Class Distribution After Undersampling')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()
