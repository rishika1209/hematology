import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib
df = pd.read_csv('server/Anemia.csv') 
X = df[["Gender", "Hemoglobin", "MCV"]]
y = df['Result']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, shuffle=True, random_state=101)
clf=DecisionTreeClassifier()
clf.fit(X_train,y_train)
joblib.dump(clf , "Decision_Tree_model.joblib")
print("no error")
