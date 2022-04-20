import pandas as pd
import numpy as np 
from catboost import CatBoostRegressor

def run(test_path, model_path):
  test = pd.read_csv(test_path)
  features = test.drop(["Модуль упругости при растяжении, ГПа"], axis=1)
  target = test["Модуль упругости при растяжении, ГПа"]

  model = CatBoostRegressor()
  model.load_model(model_path)
  pred = model.predict(features)
  print("RMSE на тестовой выборке для первого целевого признака: ", np.sqrt(((target-pred)**2).mean()))
  print("MAPE на тестовой выборке для первого целевого признака: ", np.abs((target-pred)/target).mean()*100, "%")