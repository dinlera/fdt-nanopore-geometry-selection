import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
import pandas as pd

# Define data for the decision tree
data = {
    "Geometry": ["Conical", "Cigar", "Hourglass", "Conical", "Cigar", "Hourglass"],
    "Requires Charge Sensitivity": [1, 1, 0, 1, 0, 0],
    "Requires Size Sensitivity": [0, 1, 1, 0, 1, 1],
    "Trajectory Impact": [0, 1, 0, 1, 1, 0],
    "Preferred for Application": ["Charge Detection", "Size Detection", "General Detection",
                                  "Charge Detection", "Size Detection", "General Detection"]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Encode categorical features for the decision tree
df_encoded = df.replace({
    "Geometry": {"Conical": 0, "Cigar": 1, "Hourglass": 2},
    "Preferred for Application": {"Charge Detection": 0, "Size Detection": 1, "General Detection": 2}
})

# Separate features and target
X = df_encoded.drop(columns="Preferred for Application")
y = df_encoded["Preferred for Application"]

# Initialize and train the decision tree classifier
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=42)
clf.fit(X, y)

# Plot and save the decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=X.columns,
          class_names=["Charge Detection", "Size Detection", "General Detection"],
          filled=True, rounded=True)
plt.title("Decision Tree for Nanopore Geometry Selection")
plt.show()
