import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Create a DataFrame from the given dataset
data = [['SW', 2, 'F', 20],
        ['Math', 3, 'M', 20],
        ['Art', 3, 'F', 15],
        ['English', 3, 'M', 28],
        ['Math', 3, 'F', 26],
        ['English', 3, 'M', 17],
        ['Math', 3, 'F', 26],
        ['SW', 3, 'F', 40],
        ['SW', 3, 'M', 33],
        ['English', 3, 'M', 18],
        ['Math', 3, 'M', 25],
        ['Math', 3, 'F', 30],
        ['SW', 3, 'F', 45],
        ['Art', 3, 'M', 20]]

columns = ['major', 'year', 'gender', 'StudyHours']
df = pd.DataFrame(data, columns=columns)


# Encode categorical variables (major and gender)
df_encoded = pd.get_dummies(df, columns=['major'])
df_encoded['gender'] = df_encoded['gender'].map({'F': 0, 'M': 1})  # Map 'F' to 0 and 'M' to 1

# Split the data into features (X) and target (y)
X = df_encoded.drop('StudyHours', axis=1)
y = df_encoded['StudyHours']

# Create a DecisionTreeRegressor with specified maximum depth
model = DecisionTreeRegressor(max_depth=5, random_state=0)

# Fit the model to the data
model.fit(X, y)

# Visualize the decision tree with custom node attributes and final node values
plt.figure(figsize=(12, 8))
plot_tree(model, rounded=True, feature_names=X.columns.tolist(),
          class_names=["StudyHours"], precision=2, label='root', proportion=True,
          impurity=False, node_ids=True, fontsize=12)
plt.show()
