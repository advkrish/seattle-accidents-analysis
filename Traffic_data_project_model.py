import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

BASE = os.path.dirname(__file__)
csv_path = os.path.join(BASE, 'sea_accidents.csv')
df = pd.read_csv(csv_path, low_memory=False)
df = df.dropna(subset=['WEATHER','LIGHTCOND','ROADCOND','SEVERITYDESC','INCDTTM'])
df['INCDTTM'] = pd.to_datetime(df['INCDTTM'])
df['HOUR'] = df['INCDTTM'].dt.hour
df['ACCIDENT'] = df['SEVERITYDESC'].apply(lambda x: 1 if 'Injury' in x else 0)
features = ['WEATHER','LIGHTCOND','ROADCOND','HOUR']
X = df[features].copy()
y = df['ACCIDENT']
encoders = {}
for col in ['WEATHER','LIGHTCOND','ROADCOND']:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    encoders[col] = le
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
Parameters = pd.DataFrame([{'WEATHER':'Raining','LIGHTCOND':'Dark - Street Lights On','ROADCOND':'Wet','HOUR':22}])
for col, le in encoders.items():
    Parameters[col] = le.transform(Parameters[col].astype(str))
print("Accident likely." if model.predict(Parameters)[0] == 1 else "No accident likely.")
from sklearn.metrics import classification_report

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
print(df['ACCIDENT'].value_counts())
