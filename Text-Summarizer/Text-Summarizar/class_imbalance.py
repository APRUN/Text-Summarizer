import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils import resample
from imblearn.over_sampling import SMOTE

# Load the dataset (replace 'your_dataset.csv' with the actual file path)
df = pd.read_csv('Text-Summarizar\\essays.csv')

# Check the first few rows and column names to ensure it's loaded correctly
print(df.head())
print(df.columns)

# Assuming 'label' column exists (replace with actual label column if different)
# Check the class distribution in the 'label' column
print("Class distribution before handling imbalance:")
print(df['text'].value_counts())

# Visualizing class distribution before handling imbalance
plt.figure(figsize=(8, 6))
sns.countplot(x='text', data=df, palette='Set2')
plt.title('Class Distribution Before Handling Imbalance')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()

# Handling Class Imbalance using Resampling

# Separate majority and minority classes based on the label column
majority_class = df[df['text'] == 0]  # Example: class '0' as majority
minority_class = df[df['text'] == 1]  # Example: class '1' as minority

# Option 1: Undersampling (reduce the number of samples in the majority class)
majority_undersampled = resample(majority_class, 
                                 replace=False,  # without replacement
                                 n_samples=len(minority_class),  # match the minority class size
                                 random_state=42)

# Combine the undersampled majority class with the minority class
df_undersampled = pd.concat([majority_undersampled, minority_class])

# Option 2: Oversampling (increase the number of samples in the minority class)
minority_oversampled = resample(minority_class, 
                                replace=True,  # with replacement
                                n_samples=len(majority_class),  # match the majority class size
                                random_state=42)

# Combine the oversampled minority class with the majority class
df_oversampled = pd.concat([majority_class, minority_oversampled])

# Option 3: SMOTE (Synthetic Minority Over-sampling Technique)
smote = SMOTE(random_state=42)
X = df.drop(columns=['label'])  # Drop the label column
y = df['label']  # The label column
X_resampled, y_resampled = smote.fit_resample(X, y)

# Visualizing the class distribution after resampling
plt.figure(figsize=(8, 6))

# Plot for undersampling
sns.countplot(x='label', data=df_undersampled, palette='Set2')
plt.title('Class Distribution After Undersampling')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()

# Plot for oversampling
sns.countplot(x='label', data=df_oversampled, palette='Set2')
plt.title('Class Distribution After Oversampling')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()

# Plot for SMOTE
sns.countplot(x=y_resampled, palette='Set2')
plt.title('Class Distribution After SMOTE')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()

# Check the class distribution after resampling
print("Class distribution after undersampling:\n", df_undersampled['label'].value_counts())
print("Class distribution after oversampling:\n", df_oversampled['label'].value_counts())
print("Class distribution after SMOTE:\n", pd.Series(y_resampled).value_counts())
