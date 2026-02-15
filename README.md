# regression-model
**Model Overview**
The objective of this model is to predict house sale prices using multiple structural and location-based features. The model aims to capture relationships between independent variables (features) and the dependent variable (sale_price) to provide accurate price predictions.

**Problem Statement**
Given a housing dataset containing features such as bedrooms, bathrooms, square footage, lot size, location, age of the house, number of floors, and property type, the task is to predict the sale price of a house.
This is a regression problem where the target variable is continuous.

**Dataset Description**
The dataset includes the following columns:
bedrooms – Number of bedrooms
bathrooms – Number of bathrooms
square_footage – Total house area
lot_size – Land area
location – Urban / Suburban / Rural
age – Age of the property
floors – Number of floors
property_type – Type of property
sale_price – Target variable

**Data Preprocessing**
The following preprocessing steps were performed:
1.Handling Missing Values
Numerical features were filled using median values.
Categorical features were filled using the most frequent category.

2.Encoding Categorical Variables
Categorical columns were encoded using OneHot Encoding.

3.Feature Scaling
StandardScaler was applied to normalize numerical features.

4.Train-Test Split
The dataset was divided into training and testing sets using an 80:20 ratio.

5.Model Implementation
The primary model used in this project is:
Linear Regression
Additional models can be implemented for comparison, such as Ridge, Lasso, or Random Forest Regressor.

**Evaluation Metrics**
The model performance was evaluated using:
1.Mean Squared Error (MSE)
2.R² Score
These metrics measure prediction accuracy and goodness of fit.

**Requirements**
The project requires the following Python libraries:
1.pandas
2.numpy
3.scikit-learn
Ensure these libraries are installed in your Python environment before running the project.

**How to Run the Code**
1.Download or clone the project files.
2.Place the dataset file (housing_dataset.csv) in the same directory as the main script file (reg.py).
3.Open the project folder in your Python environment (such as VS Code, PyCharm, or any IDE that supports Python).
4.Open the file named reg.py.
5.Run the script using your IDE’s run option.
6.After execution, the program will:
  Load the dataset
  Perform preprocessing
  Train the regression model
  Evaluate model performance
  Display evaluation results

**Conclusion**
The regression model successfully predicts house prices based on multiple input features. The high R² score indicates strong predictive performance, and the error metrics provide insight into average prediction deviation.

