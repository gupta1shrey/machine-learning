from sklearn import datasets, linear_model
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

cancer = datasets.load_breast_cancer()

cancer_x = cancer.data[:, np.newaxis, 2]

cancer_x_train = cancer_x[:-60]
cancer_x_test = cancer_x[-60 :]

cancer_y_train = cancer.target[:-60]
cancer_y_test = cancer.target[-60 :]

model = linear_model.LinearRegression()

model.fit(cancer_x_train, cancer_y_train)
cancer_y_predicted = model.predict(cancer_x_test)

print(mean_squared_error(cancer_y_test, cancer_y_predicted))

plt.scatter(cancer_x_test,cancer_y_test)

plt.plot(cancer_x_test ,cancer_y_predicted)

plt.show()