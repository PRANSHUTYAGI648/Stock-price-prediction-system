import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset
data = pd.read_csv("dataset/stock.csv")

# Features and Target
X = data[['Open', 'High', 'Low', 'Volume']]
y = data['Close']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)


# Prediction
prediction = model.predict(X_test)

# Accuracy
mse = mean_squared_error(y_test, prediction)

print("Model Trained Successfully!")
print("Mean Squared Error:", mse)

joblib.dump(model,"model.pkl")
print("model saved successfully as model.pkl")
