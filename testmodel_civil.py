import pandas as pd
import numpy as np
import pickle
career = pd.read_csv('civil.data', header = None)
np.dtype('float64')

X = np.array(career.iloc[:, 0:17]) #X is skills
y = np.array(career.iloc[:, 17]) #Y is Roles

##  attribute to return the column labels of the given Dataframe
career.columns = ["Structural Analysis","Geotechnical Engineering","Transportation Engineering","Environmental Engineering",
                  "Construction Management","Concrete Technology","Steel Structures","Surveying and Leveling","Fluid Mechanics",
                  "Hydrology and Water Resources Engineering","Structural Dynamics","Earthquake Engineering",
                  "Construction Materials and Testing","Communication skills","Foundation Engineering","Troubleshooting skills",
                  "Roles"]

career.dropna(how ='all', inplace = True)
#print("career.dropna(how ='all', inplace = True)",career.dropna(how ='all', inplace = True))
career.head()
## splitting the data into training and test sets 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.3, random_state = 524)
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
scores = {}
knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)
print('X_train',X_train)
print('y_train',y_train)
y_pred = knn.predict(X_test)
print('y_pred',y_pred)
scores[5] = metrics.accuracy_score(y_test, y_pred)
print('Accuracy=',scores[5]*100)

pickle.dump(knn, open('civil.pkl','wb'))
print('test file created')

