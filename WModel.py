import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import keras
from fuzzy_layer import FuzzyLayer
from defuzzy_layer import DefuzzyLayer
from keras.models import Sequential

# load the weather data
data = pd.read_csv('Dataset/Newweather.csv')

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)





data.weather=data.weather.map({'drizzle':0,
                       'rain':1,
                       'sun':2,
                       'snow':3,
                       'fog':4
                      })

# define input and output variables
temperature = data['temp_max'].values
humidity = data['temp_min'].values
wind_speed = data['wind'].values
precipitation = data['precipitation'].values
output = data['weather'].values
print(output)

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    np.column_stack((precipitation,temperature, humidity, wind_speed)),
    output,
    test_size=0.3,
    random_state=0
)

model = Sequential()
model.add(FuzzyLayer(15, input_dim=4))
model.add(DefuzzyLayer(5))

model.compile(loss='logcosh',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(X_train, y_train,
          epochs=5000,
          verbose=1,
          batch_size=64)

model.save('predict')


