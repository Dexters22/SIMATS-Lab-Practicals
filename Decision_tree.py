from sklearn import tree

# Example dataset (Play Tennis)
features = [[0, 0], [0, 1], [1, 0], [2, 1], [2, 2], [2, 1]]  # Encoded Outlook & Temp
labels = ["No", "No", "Yes", "Yes", "Yes", "No"]

clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(features, labels)

# Predict for new input (Outlook=Sunny(0), Temp=Mild(1))
print("Prediction:", clf.predict([[0, 1]]))
