import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score


class DiabetesPredictor:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, 'diabetes', 'diabetes.csv')
        
        self.orig_df = pd.read_csv(csv_path)
        self.df = self.orig_df
        self.zero_not_accepted = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Insulin']

        self.setup_df()
        self.train()

    def setup_df(self):
        for column in self.zero_not_accepted:
            self.df[column] = self.df[column].replace(0, np.nan)
            mean = int(self.df[column].mean(skipna=True))
            self.df[column] = self.df[column].replace(np.nan, mean)
        
        self.X = self.df.iloc[:, 0:8]
        self.y = self.df.iloc[:, 8]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2)

        self.sc_X = StandardScaler()
        self.X_train = self.sc_X.fit_transform(self.X_train)
        self.X_test = self.sc_X.transform(self.X_test)
    
    def train(self):
        self.classifier = KNeighborsClassifier(n_neighbors=13, p=2, metric='euclidean')
        self.classifier.fit(self.X_train, self.y_train)

        self.y_pred = self.classifier.predict(self.X_test)
    
    def confusion_matrix(self):
        return confusion_matrix(self.y_test, self.y_pred)
    
    def f1_score(self):
        return np.mean(cross_val_score(self.classifier, self.X, self.y, cv=10, scoring="f1"))
    
    def accuracy_score(self):
        return np.mean(cross_val_score(self.classifier, self.X, self.y, cv=10, scoring="accuracy"))
    
    def has_diabetes(self, user_input: list) -> bool:
        # Ensure the input is a list of floats
        user_data = list(map(float, user_input))
        
        # Convert the user input into a numpy array and reshape it
        user_data = np.array(user_data).reshape(1, -1) # 1 indicates 1 row, and -1 indicates as many columns as necessary
        
        # Replace zeros with the mean values for columns that cannot have zero
        for i, column in enumerate(self.zero_not_accepted):
            if user_data[0, i] == 0:
                user_data[0, i] = self.df[column].mean(skipna=True)
        
        # Scale the user input data
        user_data = self.sc_X.transform(user_data)
        
        # Make prediction
        prediction = self.classifier.predict(user_data)
        
        if prediction[0] == 1:
            return True
        else:
            return False



