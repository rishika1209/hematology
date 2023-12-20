import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC 
from sklearn.naive_bayes import GaussianNB 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE, ADASYN
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler
from collections import Counter
from sklearn import metrics
import joblib
df = pd.read_csv("server/Anemia.csv")

df['Hemoglobin_log'] = np.log(df['Hemoglobin'] + 0.01)
ss = StandardScaler()
df['Hemoglobin_scaled'] = ss.fit_transform(df['Hemoglobin'].values.reshape(-1, 1))
mm = MinMaxScaler()
df['Hemoglobin_minmax'] = mm.fit_transform(df['Hemoglobin'].values.reshape(-1, 1))
X = df.drop(['MCHC', 'Hemoglobin_log', 'Hemoglobin_scaled', 'Hemoglobin_minmax', 'Result', 'MCH'], axis=1)
y = df['Result']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, shuffle=True, random_state=101)
rus = RandomUnderSampler(random_state=42)
X_train_rus, y_train_rus = rus.fit_resample(X_train, y_train)
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)
adasyn = ADASYN(random_state=42)
X_train_adasyn, y_train_adasyn = adasyn.fit_resample(X_train, y_train)
ros = RandomOverSampler(random_state=42)
X_train_ros, y_train_ros = ros.fit_resample(X_train, y_train)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
cld = DecisionTreeClassifier()
cld.fit(X_train, y_train)
clr = LogisticRegression()
clr.fit(X_train, y_train)
cls = SVC(kernel= 'linear')
cls.fit(X_train, y_train)
clk = KNeighborsClassifier(n_neighbors=3)
clk.fit(X_train, y_train)
cln = GaussianNB()
cln.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print('no error')
joblib.dump(cld,'decision_tree_modle1.joblib')
joblib.dump(clf, 'random_forest_modle1.joblib')
joblib.dump(clr,'logistic_modle1.joblib')
joblib.dump(cls,'Svm_modle1.joblib')
joblib.dump(clk,'knn_modle1.joblib')
joblib.dump(cln,'NB_modle1.joblib')