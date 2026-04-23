# Import required libraries
import pandas as pd # for data handling
from sklearn.model_selection import train_test_split # for splitting data
from sklearn.linear_model import LogisticRegression # ML model
from sklearn.metrics import precision_score, recall_score, f1_score # evaluation metrics

# Load dataset
df = pd.read_excel('credit_score.xlsx')
df.head() # preview first 5 rows

# Understand data
df.info() # check data types, missing values, and structure

# Handle missing values
# Replace missing income with median (robust to outliers)
df['income'].fillna(df['income'].median(), inplace=True)

# Replace missing loan_amount with median
df['loan_amount'].fillna(df['loan_amount'].median(), inplace=True)

# Handle out-of-range credit scores (300 to 850)
df=df[(df['credit_score'] >= 300) & (df['credit_score'] <= 850)]

# Split features and target
# X → input features (remove target column)
X=df.drop(columns=['default_flag'])

# y → target variable (what we want to predict)
y=df['default_flag']

# 80% training, 20% testing
# random_state=42 ensures same split every time (reproducibility)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

X_train.head()

# Training Model
model=LogisticRegression()  # initialize model
model.fit(X_train,y_train) # train model on training data

# Given function
def model_predict(X_test):
    y_scores = model.predict_proba(X_test)[:, 1]
    print(y_scores)
    y_pred = (y_scores >= 0.5).astype(int)
    return y_pred, y_scores

# Make predictions
y_pred, y_scores = model_predict(X_test)

# Evaluate model
# Precision → how many predicted defaults are correct
print("Precision:", precision_score(y_test, y_pred))

# Recall → how many actual defaults we caught
print("Recall:", recall_score(y_test, y_pred))

# F1 Score → balance between precision and recall
print("F1 Score:", f1_score(y_test, y_pred))
