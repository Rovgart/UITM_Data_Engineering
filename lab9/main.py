import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt

df = pd.read_csv('DataSet_for_ANN.csv')
X = df.iloc[:, 3:-1].values
y = df.iloc[:, -1].values

label_encoder = LabelEncoder()
column_transformer = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), [1])],
    remainder='passthrough'
)
X = column_transformer.fit_transform(X)
X[:, 4] = label_encoder.fit_transform(X[:, 4])

imputer = SimpleImputer(strategy='mean')
X[:, 1:3] = imputer.fit_transform(X[:, 1:3])

y = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()

def scale_columns(X_train, X_test, cols):
    X_train[:, cols] = scaler.fit_transform(X_train[:, cols])
    X_test[:, cols] = scaler.transform(X_test[:, cols])
    return X_train, X_test


X_train, X_test = scale_columns(X_train, X_test, slice(3, 4))
X_train, X_test = scale_columns(X_train, X_test, slice(5, 9))
X_train, X_test = scale_columns(X_train, X_test, slice(11, None))


X_train = X_train.astype(np.float32)
X_test = X_test.astype(np.float32)
y_train = y_train.astype(np.float32)
y_test = y_test.astype(np.float32)

model = Sequential([
    Dense(units=X_train.shape[1], activation='relu'),
    Dense(units=X_train.shape[1] // 2, activation='relu'),
    Dense(units=1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

early_stop = EarlyStopping(monitor='val_loss', patience=25, restore_best_weights=True)
history = model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=1000,
    batch_size=64,
    callbacks=[early_stop],
    verbose=1
)


pd.DataFrame(history.history).plot(figsize=(15, 5))
plt.grid(True)
plt.show()
