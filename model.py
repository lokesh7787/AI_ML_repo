import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

class LinearRegrisson():
    def __init__(self,learningRate = 0.01,epochs=1000):
        self.learningRate  = learningRate
        self.epochs = epochs
        self.W = None
        self.b = 0.0

    def fit(self,X,Y):
        self.sample,self.feature = X.shape
        self.W = np.random.randn(self.feature) * 0.01 # Small random initialization
        self.b = 0.0
        self.X = X
        self.Y = Y

        for i in range(self.epochs):
            if not self.updateWeight(X):
                break
            if i % 100 == 0:  # Print loss every 100 epochs
                y_pred = self.predict(X)
                loss = np.mean((Y - y_pred) ** 2)
                print(f"Epoch {i}, Loss: {loss}")
           

    def updateWeight(self,X):
        y_pred = self.predict(X)
        error = y_pred - self.Y
        dw = (2/self.sample) * np.dot(X.T,(error))
        db = (2/self.sample) * np.sum(error)
        self.W = self.W - self.learningRate * dw
        self.b = self.b - self.learningRate * db

        loss = np.mean(error ** 2)
        # Arbitrary threshold
        if loss > 1e10:
            print("Loss exploded. Stopping training.")
            return False
        return True




    def predict(self,x):
        return np.dot(x, self.W) + self.b

    
def main():
    scaler = StandardScaler()
    df = pd.read_csv('train_energy_data.csv')
    df_Test = pd.read_csv('test_energy_data.csv')
    df['Building Type'] = df['Building Type'].map({"Residential":1,"Commercial":2,"Industrial":3})
    df['Day of Week'] = df['Day of Week'].map({"Weekday":1,"Weekend":0})

    df_Test['Building Type'] = df_Test['Building Type'].map({"Residential":1,"Commercial":2,"Industrial":3})
    df_Test['Day of Week'] = df_Test['Day of Week'].map({"Weekday":1,"Weekend":0})

    X = df.iloc[:,:-1].values
    Y = df.iloc[:,-1].values
    X = scaler.fit_transform(X)
   
    X_test = df_Test.iloc[:,:-1].values
    Y_test = df_Test.iloc[:,-1].values
    X_test = scaler.transform(X_test)
    model = LinearRegrisson()

    model.fit(X,Y)

    y_pred = model.predict(X_test)
    def mse(Y_test,y_pred):
        return np.mean((Y_test - y_pred)**2)

    
    mse = mse(Y_test,y_pred)
    print("mse",mse)

    Y_pred = model.predict( X_test )
    correlection = df.corr()

    plt.figure(figsize=(10,8))

    # sns.heatmap(correlection,annot=True)

    plt.scatter( df['Square Footage'], df['Energy Consumption'], color = 'blue' )
    plt.plot( X_test, Y_pred, color = 'orange' ) 
    plt.title( 'Square Footage vs Energy Consumption' ) 
      
    plt.xlabel( 'Square Footage' ) 
      
    plt.ylabel( 'Energy Consumption' ) 
    plt.show()
if __name__ == '__main__':
    main()

