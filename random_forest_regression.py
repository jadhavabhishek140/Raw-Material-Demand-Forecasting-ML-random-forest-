

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt  
from sklearn.ensemble import RandomForestRegressor
# %matplotlib inline

#!git clone https://github.com/Nitesh167/raw-materials-forecasting.git

#cd raw-materials-forecasting/

df=pd.read_csv('dataset_value2.csv')
df.columns=['Year',"no_of_cars","steel","plastics","iron","rubber","aluminium","glass","copper"]
df.head(10)

#delete column 
del df["Year"]

np.random.seed(33)
msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]

"""# **STEEL**"""

train_x = np.asanyarray(train[['no_of_cars']])
train_y = np.asanyarray(train[['steel']])
from sklearn.ensemble import RandomForestRegressor
model_steel = RandomForestRegressor()
model_steel.fit (train_x, train_y)
# The coefficients
pickle.dump(model_steel, open('steel_model.pkl', 'wb'))
steel_model = pickle.load(open('steel_model.pkl', 'rb'))

"""# **PLASTICS**"""

from sklearn import linear_model
model_plastics =RandomForestRegressor()
train_x = np.asanyarray(train[['no_of_cars']])
train_y_plastics = np.asanyarray(train[['plastics']])
model_plastics.fit (train_x, train_y_plastics)
pickle.dump(model_plastics, open('plastics_model.pkl', 'wb'))
plastics_model = pickle.load(open('plastics_model.pkl', 'rb'))


"""# **IRON**"""

from sklearn import linear_model
model_iron = RandomForestRegressor()
train_x = np.asanyarray(train[['no_of_cars']])
train_y_iron = np.asanyarray(train[['iron']])
model_iron.fit (train_x, train_y_iron)
pickle.dump(model_iron, open('iron_model.pkl', 'wb'))
iron_model = pickle.load(open('iron_model.pkl', 'rb'))

# **RUBBER**"""

from sklearn import linear_model
model_rubber = RandomForestRegressor()
train_x = np.asanyarray(train[['no_of_cars']])
train_y_rubber = np.asanyarray(train[['rubber']])
model_rubber.fit (train_x, train_y_rubber)
pickle.dump(model_rubber, open('rubber_model.pkl', 'wb'))
rubber_model = pickle.load(open('rubber_model.pkl', 'rb'))

"""# **ALUMINIUM**"""

from sklearn import linear_model
model_aluminium = RandomForestRegressor()
train_x = np.asanyarray(train[['no_of_cars']])
train_y_aluminium = np.asanyarray(train[['aluminium']])
model_aluminium.fit (train_x, train_y_aluminium)

pickle.dump(model_aluminium, open('aluminium_model.pkl', 'wb'))
aluminium_model = pickle.load(open('aluminium_model.pkl', 'rb'))

"""# **GLASS**"""

from sklearn import linear_model
model_glass = RandomForestRegressor()
train_x = np.asanyarray(train[['no_of_cars']])
train_y_glass = np.asanyarray(train[['glass']])
model_glass.fit (train_x, train_y_glass)
pickle.dump(model_glass, open('glass_model.pkl', 'wb'))
glass_model = pickle.load(open('glass_model.pkl', 'rb'))

"""# **COPPER**"""

from sklearn import linear_model
model_copper = RandomForestRegressor()
train_x = np.asanyarray(train[['no_of_cars']])

train_y_copper = np.asanyarray(train[['copper']])
model_copper.fit (train_x, train_y_copper.ravel())

pickle.dump(model_copper, open('copper_model.pkl', 'wb'))
copper_model = pickle.load(open('copper_model.pkl', 'rb'))




