# Regression-model
**Model Overview**
The objective of this model is to predict house sale prices using multiple structural and location-based features. The model aims to capture relationships between independent variables (features) and the dependent variable (sale_price) to provide accurate price predictions.

**Dataset Description**

The dataset includes the following features:

bedrooms – Number of bedrooms

bathrooms – Number of bathrooms

square_footage – Total built area

lot_size – Land area

location – Urban / Suburban / Rural

age – Age of the house

floors – Number of floors

property_type – House / Apartment / Condo / Villa

sale_price – Target variable

**Data Preprocessing Steps**

The following preprocessing steps were performed:

1. Handling Missing Values

Numerical columns filled using median values

Categorical columns filled using mode

2. Encoding Categorical Variables

OneHot Encoding applied to categorical features

3. Feature Scaling

StandardScaler applied to numerical features

4. Train-Test Split

80% training data

20% testing data

5. Model Used

Linear Regression

Optional comparison models:

Ridge Regression

Lasso Regression

Random Forest Regressor

6. Evaluation Metrics

The model was evaluated using:

Mean Squared Error (MSE)

R² Score

These metrics measure prediction error and the overall goodness of fit.

**Requirements**

The following Python libraries are required:

pandas

numpy

scikit-learn

Install them using a Python package manager before running the project.

**How to Run the Project**

1. Place the dataset file (house_data.csv) in the same directory as the script.

2. Ensure all required libraries are installed.

3. Open the project folder in your Python environment (VS Code, PyCharm, or similar).

4. Run the main script file:

reg.py

5. The program will:

Load and preprocess the dataset

Train the regression model

Evaluate performance

Display evaluation metrics

**Conclusion**
The regression model successfully predicts house prices based on multiple input features. The high R² score indicates strong predictive performance, and the error metrics provide insight into average prediction deviation.

