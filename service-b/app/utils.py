import pandas as pd
import os
import requests 
import models

URL = os.getenv('SERVICE_C_URL')


class Data_hendler:
    def __init__(self, data: models.Weather_information_list):
        self.valid(data=data)
        self.df = pd.DataFrame(data.data)
        self.fiilnan()
        self.add_temperature_category_colume()
        self.add_wind_category()
        
    def fiilnan(self):
        self.df.fillna(self.df)    

    def add_temperature_category_colume(self): 
        self.df['temperature_categor'] = pd.cut(x=self.df['temperature'], bins=[-100,18,25,100], labels=['cold', 'moderate', 'hot'])

    def add_wind_category(self):
        self.df['wind_category'] = pd.cut(x=self.df['wind_speed'], bins=[0,10,1000], labels=['calm', 'windy'])   

    def valid(self, data: list):
        try:
            for i in data:
                models.Weather_information(i) 
        except TypeError as e:
            return str(e)            

    def return_data_dict(self):
        return self.df.to_dict('records') 


class Send_data:
    def __init__(self):
      self.url = URL 

    def send_data(self, data): 
        data_obj = models.Weather_information_list(data=data)
        result = requests.post(url=self.url, json=data_obj.model_dump(mode='json'))
        return result.json()
        



   
