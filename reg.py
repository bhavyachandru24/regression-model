import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
df = pd.read_csv("house_data.csv")
X = df.drop("sale_price", axis=1).copy()
y = df["sale_price"]
loc = LabelEncoder()
property = LabelEncoder()
X["location"] = loc.fit_transform(X["location"])
X["property_type"] =property.fit_transform(X["property_type"])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
sc = StandardScaler()
X_train_sc = sc.fit_transform(X_train)
X_test_sc = sc.transform(X_test) 
model = LinearRegression()
model.fit(X_train_sc, y_train)
y_pred = model.predict(X_test_sc)
print("Train R2:", model.score(X_train_sc, y_train))
print("Test R2:", model.score(X_test_sc, y_test))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

