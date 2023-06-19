from flask import Flask, render_template, request
from stockPrediction.pipeline.forecast_pipeline import ForecastPipeline
from flask_cors import CORS, cross_origin
import os
app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         user_input = request.form['input_text']

#         forcast_obj = ForecastPipeline()
#         forcast_obj.initiate_forecastes(user_input)

#         return render_template('results.html')
#     return render_template('index.html')



@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def home():

    if request.method == 'POST':

        user_input = request.form.get('number')
        forcast_obj = ForecastPipeline()
        forcast_obj.initiate_forecast(int(user_input))

        return render_template('results.html')

    return render_template('index.html')




if __name__ == '__main__':
    app.run()