from sklearn import datasets, linear_model
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()
#'data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'
"""    - age     age in years
      - sex
      - bmi     body mass index
      - bp      average blood pressure
      - s1      tc, total serum cholesterol
      - s2      ldl, low-density lipoproteins
      - s3      hdl, high-density lipoproteins
      - s4      tch, total cholesterol / HDL
      - s5      ltg, possibly log of serum triglycerides level
      - s6      glu, blood sugar level
"""
diabetes_X = diabetes.data[:, np.newaxis, 2]

diabetes_X_train = diabetes_X[: -30]
diabetes_X_test = diabetes_X[-30 :]

diabetes_Y_train = diabetes.target[:-30]
diabetes_Y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()

model.fit(diabetes_X_train, diabetes_Y_train)

diabetes_Y_predicted = model.predict(diabetes_X_test)

print(mean_squared_error(diabetes_Y_test, diabetes_Y_predicted))

plt.scatter(diabetes_X_test, diabetes_Y_test)

plt.plot(diabetes_X_test, diabetes_Y_predicted)

plt.show()