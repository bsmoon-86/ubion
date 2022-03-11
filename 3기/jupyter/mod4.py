import pandas as pd

class Change_dt_2():
    def __init__(self, input_url):
        self.url = input_url
    
    def csv_read(self, input_sort = "Country", input_inplace = True):
        self.dt = pd.read_csv(self.url) 
        self.dt.sort_values(input_sort, inplace=input_inplace)
        self.dt.reset_index(drop=True, inplace=input_inplace)
        return self.dt

    def remove_column(self, input_list = []):
        self.dt.drop(input_list, axis=1, inplace=True)
        return self.dt

    def remove_2(self, input_s_column, input_e_column):
        self.dt.drop(self.dt.loc[:,input_s_column:input_e_column], axis = 1, inplace=True)
        return self.dt
