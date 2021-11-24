
from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd


app = Flask(__name__)
api = Api(app)

url_data="https://raw.githubusercontent.com/EderReisS/Python_Machine_Learning/main/input_Files/Credit.csv"
df_credit = pd.read_csv(url_data)

class credit_purpose(Resource):
    def get(self, purpose_):
        purpose_filter= df_credit['purpose']== purpose_
        credit_purpose = df_credit[purpose_filter]
        print(credit_purpose.to_json(orient='columns'))
        return credit_purpose.to_json(orient='columns')
    
class purposes(Resource):
    def get(self):
        return df_credit['purpose'].unique().tolist()
    

api.add_resource(credit_purpose, '/<string:purpose_>')
api.add_resource(purposes, '/')

if __name__ == '__main__':
    app.run(debug=True)
