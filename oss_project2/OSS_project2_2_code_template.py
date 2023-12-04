import pandas as pd
import sklearn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def sort_dataset(dataset_df):
	#TODO: Implement this function
	return dataset_df.sort_values(by=['year'])
def split_dataset(dataset_df):	
	#TODO: Implement this function
	return train_test_split(dataset_df, dataset_df['salary'] * 0.001, test_size = 0.1016, shuffle=False)
def extract_numerical_cols(dataset_df):
	#TODO: Implement this function
	return dataset_df[['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly', 'war']]
def train_predict_decision_tree(X_train, Y_train, X_test):
	#TODO: Implement this function
	dt = DecisionTreeClassifier()
	dt.fit(X_train, Y_train.astype('int'))
	
	return dt.predict(X_test)
def train_predict_random_forest(X_train, Y_train, X_test):
	#TODO: Implement this function
	rf = RandomForestClassifier()
	rf.fit(X_train, Y_train.astype('int'))
	
	return rf.predict(X_test)
def train_predict_svm(X_train, Y_train, X_test):
	#TODO: Implement this function
	svm_pipe = make_pipeline(StandardScaler(), SVC())
	svm_pipe.fit(X_train, Y_train.astype('int'))
	
	return svm_pipe.predict(X_test)
def calculate_RMSE(labels, predictions):
	#TODO: Implement this function
	mse = mean_squared_error(labels, predictions)
	rmse = np.sqrt(mse)
	
	return rmse
if __name__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
	
	sorted_df = sort_dataset(data_df)	
	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)
	
	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)
	
	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))	
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))	
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))
