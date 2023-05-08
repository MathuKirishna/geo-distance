import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from scipy.sparse import hstack


# Load the data into a pandas dataframe
data = pd.read_csv("../data/distance_added_feature_extracted_300.csv", header=0, sep=",")

feature_type=data['last_place_name_feature_type']
feature_type=list(set(feature_type))

# Split the dataset into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2)

# Extract textual features using TF-IDF
tfidf = TfidfVectorizer()
tfidf_features = tfidf.fit_transform(train_data['Locality'])

# Convert categorical variables to numerical values using one-hot encoding
onehot = OneHotEncoder(categories=[feature_type])
onehot_features = onehot.fit_transform(train_data[['last_place_name_feature_type']])

# Normalize numerical variables to have zero mean and unit variance
scaler = StandardScaler()
scaled_features = scaler.fit_transform(train_data[['source_latitude', 'source_longitude']])

# Combine the features into a single feature matrix
X_train = hstack([tfidf_features, onehot_features, pd.DataFrame(scaled_features)])

# Extract the dependent variable
y_train = train_data['distance']

# Train a linear regression model
reg = LinearRegression()
reg.fit(X_train, y_train)

# Extract the features and dependent variable from the testing set
X_test_tfidf = tfidf.transform(test_data['Locality'])
X_test_onehot = onehot.transform(test_data[['last_place_name_feature_type']])
X_test_scaled = scaler.transform(test_data[['source_latitude', 'source_longitude']])
X_test = hstack([X_test_tfidf, X_test_onehot, pd.DataFrame(X_test_scaled)])
y_test = test_data['distance']

# Evaluate the model's performance on the testing set
y_pred = reg.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Mean Absolute Error:', mae)
