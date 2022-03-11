import pandas as pd

class change_dt():
    def regist_pandas(self, input_url):
        self.dt = pd.read_csv(input_url)
        return self.dt
    
    def nan_count(self):
        return self.dt.isna().sum()
    
    def dt_sort(self, input_value, input_inplce = False):
        return self.dt.sort_values(input_value, inplace=input_inplce)
    
    def dt_drop(self, input_columns = [], input_inplace = False):
        return self.dt.drop(input_columns, axis=1, inplace= input_inplace)
    
    def dt_change_c(self, input_columns):
        self.dt.columns = input_columns
        return True