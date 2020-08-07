from flask import Flask, render_template, request, session
from src.utils import *


app = Flask(__name__)

with open("credentials.json") as f:
    app.config['custom_vision_key'] = json.load(f)["api_key"]


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/start')
def insert():

    open_waste_slot()

    return render_template('insert.html')


@app.route('/waste/predict-type')
def predict_type():

    close_waste_slot()
    trash_picture = take_trash_picture()
    label_pred = classify_waste(trash_picture, app.config['custom_vision_key'])

    return render_template('predictions.html', label_pred=label_pred)


# User can rectify if error in prediction
@app.route('/rectify', methods=['POST'])
def rectify():

    wrong_predicted_type = request.form['type']  # Can be used to keep track of failures and improve model performances

    return render_template('type.html')


@app.route('/confirmation', methods=['POST'])
def confirmation():

    waste_type = request.form['type']

    process_waste(waste_type)
    return render_template('confirmation.html')


if __name__ == "__main__":
    app.run(debug=True)
