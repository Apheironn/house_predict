import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            model_path = 'artifacts\model.pkl'
            preprocessor_path = 'artifacts\preprocessor.pkl'
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)        

class CustomData:
    def __init__(  self,
        bedrooms: int,
        bathrooms: float,
        sqft_living: int,
        sqft_lot: int,
        floors: float,
        condition: int,
        grade: int,
        sqft_above: int,
        sqft_basement: int,
        yr_built: int,
        lat: float,
        longs: float
        ):

        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.sqft_living = sqft_living
        self.sqft_lot = sqft_lot
        self.floors = floors
        self.condition = condition
        self.grade = grade
        self.sqft_above = sqft_above
        self.sqft_basement = sqft_basement
        self.yr_built = yr_built
        self.lat = lat
        self.longs = longs

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "bedrooms": [self.bedrooms],
                "bathrooms": [self.bathrooms],
                "sqft_living": [self.sqft_living],
                "sqft_lot": [self.sqft_lot],
                "floors": [self.floors],
                "condition": [self.condition],
                "grade": [self.grade],
                "sqft_above": [self.sqft_above],
                "sqft_basement":[self.sqft_basement],
                "yr_built": [self.yr_built],
                "lat": [self.lat],
                "longs": [self.longs]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)