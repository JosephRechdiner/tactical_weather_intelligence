import pandas as pd


class Data_hendler:
    def __init__(self, data: list[dict]):
        self.df = pd.DataFrame(data)
    def fiilnan(self):
        self.df.fillna()    
    def add_temperature_categor_colume(self):  
        self.df['temperature_categor'] = pd.cut(x=self.df['temperature'], bins=[-100,18,25,100], labels=['cold', 'moderate', 'hot'])
    
        
