import pandas as pd
from sklearn.preprocessing import LabelEncoder 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV, KFold
import joblib

def main():
    data = pd.read_csv('../data/cleaned_data/clean_data.csv')
    label_encoder = LabelEncoder()
    data['sectorName'] = label_encoder.fit_transform(data['sectorName'])
    data['stateDescription']= label_encoder.fit_transform(data['stateDescription'])
    data.drop(['customers','revenue','sales'],axis=1,inplace= True)

    X = data.drop(['price'],axis=1)
    y=data['price']
    #train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # param_grid = {
    #     'n_estimators': [50, 100, 150, 200, 250]  # Adjust this range as needed
    # }
    # rf = RandomForestRegressor(random_state=42)
    # cv = KFold(n_splits=5, shuffle=True, random_state=42)  # 5-fold cross-validation
    # grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=cv, scoring='neg_mean_squared_error', n_jobs=-1)
    # grid_search.fit(X, y)

    # best_n_estimators = grid_search.best_params_['n_estimators']

    best_rf = RandomForestRegressor(n_estimators=10,max_depth=10)
    best_rf.fit(X_train, y_train)
    save_model(best_rf,"../data/model/main.joblib")

    y_pred = best_rf.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    # print("Best number of estimators:", best_n_estimators)
    print("Mean Squared Error (MSE):", mse)

def save_model(model, path):
    joblib.dump(model, path)

def load_model(path):
    model = joblib.load("./data/model/main.joblib")
    return model

def prediction(X):
    model = joblib.load("../data/model/main.joblib")
    preds = model.predict(X)
    print(preds)
    return preds[0]

if __name__ == "__main__":
    main()
    # prediction(pd.DataFrame({"year":[2021],"month":[10],"stateDescription":[42],"sectorName":[2]}))