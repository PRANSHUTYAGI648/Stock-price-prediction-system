# Stock-price-prediction-system

📈 Stock Price Prediction — Basic Knowledge
1. What is Stock Price Prediction?

Stock Price Prediction is a Machine Learning project that predicts the future closing price of a stock using historical stock market data.

In your project, we use these features:

Open – price at which the stock started trading
High – highest price during the trading period
Low – lowest price during the trading period
Volume – number of shares traded
Close – closing price, which is the value we want to predict
2. Which Machine Learning Algorithm did you use?

You used Linear Regression.

Simple English explanation:

Linear Regression is a supervised machine learning algorithm used to predict a continuous numerical value. In this project, it learns the relationship between Open, High, Low, and Volume and predicts the Close price.

3. How does your project work?

The basic workflow is:

Historical Dataset → Data Preprocessing → Train/Test Split → Linear Regression → Model Training → Prediction → Web Application

For your project:

stock.csv
   ↓
Load Dataset
   ↓
Select Features
(Open, High, Low, Volume)
   ↓
Target
(Close)
   ↓
Train/Test Split
   ↓
Linear Regression Model
   ↓
Train Model
   ↓
Save model.pkl
   ↓
Flask Web App
   ↓
Enter Stock Values
   ↓
Predict Closing Price
4. What is model.pkl?

model.pkl is the saved trained machine learning model.

Instead of training the model every time the website runs, we save the trained model using joblib.

Then Flask loads the saved model and uses it for prediction.

5. What is Flask?

Flask is a lightweight Python web framework.

In your project, Flask connects:

HTML frontend ↔ Python Machine Learning model

For example:

User enters:
Open = 150
High = 155
Low = 148
Volume = 1000000


        ↓


Flask


        ↓


model.pkl


        ↓


Predicted Close Price
🧠 Important Interview Questions
Q1. What is the objective of your project?

The objective of my project is to predict the closing price of a stock using historical stock market data and machine learning.

Q2. Why did you use Linear Regression?

I used Linear Regression because the target value, which is the closing price, is a continuous numerical value. It is also simple and easy to understand for a basic prediction model.

Q3. What are your input features?

My input features are Open Price, High Price, Low Price, and Volume.

Q4. What is the target variable?

The target variable is the Close Price because my model is trained to predict the closing price.

Q5. What is the difference between training and testing data?

Training data is used to teach the machine learning model, while testing data is used to evaluate how well the trained model performs on unseen data.

Q6. What is train_test_split?

train_test_split divides the dataset into training and testing parts. In my project, I used 80% data for training and 20% for testing.

Q7. What is MSE?

MSE = Mean Squared Error

MSE is an evaluation metric used to measure the difference between actual values and predicted values. A lower MSE generally means better prediction performance.

Your project produced:

MSE ≈ 920.08

📂 Your GitHub Project Structure

Your project can be explained like this:

STOCK-PRICE-PREDICTION/
│
├── dataset/
│   └── stock.csv
│
├── templates/
│   └── index.html
│
├── app.py
├── model.py
├── model.pkl
└── requirements.txt
Files ka role:
File	Purpose
stock.csv	Historical stock data
model.py	Machine Learning model training
model.pkl	Saved trained model
app.py	Flask backend
index.html	User interface
requirements.txt	Required Python libraries
