import pandas as pd
import numpy as np
import pickle
career = pd.read_csv('ece.data', header = None)
np.dtype('float64')

X = np.array(career.iloc[:, 0:17]) #X is skills
print(X)
y = np.array(career.iloc[:, 17]) #Y is Roles
print("hi")
print(y) 

##  attribute to return the column labels of the given Dataframe
career.columns = ["Analog Communication Systems", "Digital Communication Systems", 
                  "Information Theory", "Communication Networks", "Modulation Techniques",
                  "Programming Skills", "Project Management", "Wireless Sensor Networks", 
                  "Communication Protocols", "Multimedia Communication","Data Compression Techniques","Business Analysis"
                  ,"Business Analysis","Communication skills","Digital Modulation and Coding","Troubleshooting skills",
                  "Internet of Things (IoT)","Roles"]

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

pickle.dump(knn, open('ece.pkl','wb'))
print('test file created')

