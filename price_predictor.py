import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree
import matplotlib.pyplot as plt

# Reading the data
current_dir  = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'data', 'ford.csv')
data = pd.read_csv(file_path)

# Handling categorical columns with One-Hot Encoding
categorical_cols = ["model", "transmission", "fuelType"]
data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

# Splitting the data in to train and test data
X = data.drop(columns=['price'])
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Creating the DecisionTreeRegressor model
model = DecisionTreeRegressor()
model.fit(X_train, y_train)
preds = model.predict(X_test)

# Score
score = model.score(X_test, preds)
print(score)

# ADDITIONAL VISUALIZATIONS

# DECISION TREE
# Displays the DecisionTreeRegressor model in a visual graph

plt.figure(figsize=(15, 10))
plot_tree(model, filled=True, feature_names=X.columns)
plt.show()

"""
# FEATURE IMPORTANCE
# Shows the importance of each feature in the Decision Tree

importance = model.feature_importances_
feature_names = X.columns

# Sort feature importances in descending order
indices = importance.argsort()[::-1]

plt.figure(figsize=(10, 6))
plt.title("Feature Importance")
plt.bar(range(X.shape[1]), importance[indices], align="center")
plt.xticks(range(X.shape[1]), feature_names[indices], rotation=90)
plt.tight_layout()
plt.show()
"""
"""
# ACTUAL VS PREDICTED
# Visualizes the actual and the predicted prices

plt.figure(figsize=(8, 6))
plt.scatter(y_test, preds)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--')
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs. Predicted Prices")
plt.show()
"""

#TODO
#Making the model available to use in a GUI is still in the making.
#from joblib import dump
#dump(model, 'ford_price_pred.py')