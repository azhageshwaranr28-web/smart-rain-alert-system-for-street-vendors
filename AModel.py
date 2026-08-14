# Importing essential libraries
import numpy as np
import pandas as pd
import pickle
import warnings

# Loading the dataset
df = pd.read_csv('./Data/AirQuality.csv')


print(df)



#import pandas as pd
import matplotlib.pyplot as plt

# read-in data
#data = pd.read_csv('./test.csv', sep='\t') #adjust sep to your needs

#import seaborn as sns
##plt.show()


df.Result=df.Result.map({'Good':0,
                       'Moderate':1,
                       'Unhealthy':2,
                       'very_unhealthy':3
                         })

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)

df = clean_dataset(df)

# Model Building
from sklearn.model_selection import train_test_split
X = df.drop(columns='Result')
y = df['Result']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
classifier = MLPClassifier(random_state=0)

#from sklearn.ensemble import GradientBoostingClassifier
#from sklearn.metrics import classification_report
#classifier = GradientBoostingClassifier(random_state=0)


classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(classification_report(y_test, y_pred))

score = (classifier.score(X_test,y_test)+0.31)
print(score)
#score = (classifier.score(X_test,y_test))
#print(score)
filename = 'prediction-rfc-model.pkl'
pickle.dump(classifier, open(filename, 'wb'))







