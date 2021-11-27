
from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


app = Flask(__name__)
api = Api(app)

url_data="https://raw.githubusercontent.com/EderReisS/Python_Machine_Learning/main/input_Files/Credit.csv"
df_credit = pd.read_csv(url_data)

class data_helper():
    
    @staticmethod
    def agg_quantitative(data: pd.DataFrame, var: str = 'credit_amount') -> pd.DataFrame:
        quali_var = 'job'
        quanti_var = var
                
        df_agg =data.groupby(by=quali_var).agg(
            {quanti_var:['mean','sum','std','median','count']
            }
        ).round(2)
        
        return df_agg
    
    @staticmethod
    def graph_plot(data: pd.DataFrame, var: str = 'credit_amount') -> None:
        graph = plt.figure(figsize=(15, 10))
        sns.boxplot(data = data, x = 'job', y = var, hue = 'class')
        plt.savefig('graph.jpeg')


class credit_purpose(Resource):
    def get(self, purpose_):
        purpose_filter = df_credit['purpose'] == purpose_
        df_filtered = df_credit[purpose_filter]
        
        #persistir como csv e json a partir 
        name_agg = 'credit_amount'
        df_agg = data_helper.agg_quantitative(data = df_filtered, var = name_agg ) 
        df_agg.to_json(f'{name_agg}.json', orient='columns')
        df_agg.to_csv(f'{name_agg}.csv')
        
        #salvar o gráfico
        data_helper.graph_plot(data = df_filtered)
        
        #retorno como API
        return df_filtered.to_json(orient='columns')
    
class purposes(Resource):
    def get(self):
        return df_credit['purpose'].unique().tolist()
    

api.add_resource(credit_purpose, '/<string:purpose_>')
api.add_resource(purposes, '/')

if __name__ == '__main__':
    app.run(debug=True)
