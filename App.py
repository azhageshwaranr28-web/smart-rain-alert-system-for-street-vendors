import os
import pickle

import numpy as np
from flask import Flask, render_template, flash, request, session

app = Flask(__name__)
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'change-this-secret-key')


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/Home")
def Home():
    return render_template('index.html')






@app.route("/Predict")
def Predict():
    return render_template('Predict.html')



@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            preg = float(request.form['Precipitation'])
            temp_max = float(request.form['temp_max'])
            temp_min = float(request.form['temp_min'])
            wind = float(request.form['wind'])
        except ValueError:
            return "Invalid input: Please enter numeric values"

        filename = 'predict/predict.pkl'
        classifier = pickle.load(open(filename, 'rb'))

        data = np.array([[preg, temp_max, temp_min, wind]])

        my_prediction = classifier.predict(data)
        result = my_prediction[0]   # ✅ extract value

        print(result)

        if result == 0:
            pre = 'drizzle'
        elif result == 1:
            pre = 'rain'
        elif result == 2:
            pre = 'sun'
        elif result == 3:
            pre = 'snow'
        else:
            pre = 'Unknown'
        sendmsg(os.getenv('ALERT_MOBILE_NUMBER', ''), "Weather Result = " + pre)
        sendmail(os.getenv('ALERT_EMAIL', ''), "Your Weather Prediction Result is = " + pre)
        return render_template('Predict.html', pre=pre)


@app.route("/Predict1")
def Predict1():
    return render_template('Predict1.html')

@app.route("/predict1", methods=['GET', 'POST'])
def predict1():
    if request.method == 'POST':

        import requests

        url = "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true"

        response = requests.get(url)
        data = response.json()

        temp_max = data['current_weather']['temperature']
        wind = data['current_weather']['windspeed']

        print("Temperature:", temp_max)
        print("Wind Speed:", wind)


        try:
            preg = float(request.form['Precipitation'])
            #temp_max = float(request.form['temp_max'])
            temp_min = float(request.form['temp_min'])
            #wind = float(request.form['wind'])
        except ValueError:
            return "Invalid input: Please enter numeric values"

        filename = 'predict/predict.pkl'
        classifier = pickle.load(open(filename, 'rb'))

        data = np.array([[preg, temp_max, temp_min, wind]])

        my_prediction = classifier.predict(data)
        result = my_prediction[0]   # ✅ extract value

        print(result)

        if result == 0:
            pre = 'drizzle'
        elif result == 1:
            pre = 'rain'
        elif result == 2:
            pre = 'sun'
        elif result == 3:
            pre = 'snow'
        else:
            pre = 'Unknown'

        sendmsg(os.getenv('ALERT_MOBILE_NUMBER', ''), "Weather Result = " + pre)
        sendmail(os.getenv('ALERT_EMAIL', ''), "Your Weather Prediction Result is = " + pre)

        return render_template('Predict1.html', pre=pre)


@app.route("/AirQuality")
def AirQuality():
    return render_template('AirQuality.html')


@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == 'POST':

        t1 = float(request.form['t1'])
        t2 = float(request.form['t2'])
        t22 = float(request.form['t22'])
        t23 = float(request.form['t23'])
        t24 = float(request.form['t24'])
        t25 = float(request.form['t25'])
        t26 = float(request.form['t26'])
        t27 = float(request.form['t27'])
        t28 = float(request.form['t28'])

        filename = 'prediction-rfc-model.pkl'
        classifier = pickle.load(open(filename, 'rb'))

        data = np.array([[t1, t2, t22, t23, t24, t25, t26, t27, t28]])

        my_prediction = classifier.predict(data)

        result = my_prediction[0]   # important fix

        if result == 0:
            Answer = 'Good'
        elif result == 1:
            Answer = 'Moderate'
        elif result == 2:
            Answer = 'Unhealthy'
        elif result == 3:
            Answer = 'Very Unhealthy'

        sendmsg(os.getenv('ALERT_MOBILE_NUMBER', ''), "Air Result = " + Answer)
        sendmail(os.getenv('ALERT_EMAIL', ''), "Your Air Prediction Result is = " + Answer)

        return render_template('AirQuality.html', pre=Answer)






@app.route("/AirQuality1")
def AirQuality1():
    return render_template('AirQuality1.html')


@app.route("/result1", methods=['GET', 'POST'])
def result1():
    if request.method == 'POST':

        import requests

        url = "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true"

        response = requests.get(url)
        data = response.json()

        t1 = data['current_weather']['temperature']
        t22 = data['current_weather']['windspeed']

        print("Temperature:", t1)
        print("Wind Speed:", t22)

        #t1 = float(request.form['t1'])
        t2 = float(request.form['t2'])
        #t22 = float(request.form['t22'])
        t23 = float(request.form['t23'])
        t24 = float(request.form['t24'])
        t25 = float(request.form['t25'])
        t26 = float(request.form['t26'])
        t27 = float(request.form['t27'])
        t28 = float(request.form['t28'])

        filename = 'prediction-rfc-model.pkl'
        classifier = pickle.load(open(filename, 'rb'))

        data = np.array([[t1, t2, t22, t23, t24, t25, t26, t27, t28]])

        my_prediction = classifier.predict(data)

        result = my_prediction[0]   # important fix

        if result == 0:
            Answer = 'Good'
        elif result == 1:
            Answer = 'Moderate'
        elif result == 2:
            Answer = 'Unhealthy'
        elif result == 3:
            Answer = 'Very Unhealthy'

        sendmsg(os.getenv('ALERT_MOBILE_NUMBER', ''), "Air Result = " + Answer)
        sendmail(os.getenv('ALERT_EMAIL', ''), "Your Air Prediction Result is = " + Answer)

        return render_template('AirQuality.html', pre=Answer)


def sendmsg(targetno, message):
    """Send an SMS alert when SMS settings are configured in the environment."""
    import requests

    sms_api_key = os.getenv('SMS_API_KEY', '')
    sms_api_url = os.getenv('SMS_API_URL', 'https://sms.creativepoint.in/api/push.json')
    if not sms_api_key or not targetno:
        return

    requests.post(
        sms_api_url,
        params={
            'apikey': sms_api_key,
            'route': os.getenv('SMS_ROUTE', 'transsms'),
            'sender': os.getenv('SMS_SENDER', 'FSSMSS'),
            'mobileno': targetno,
            'text': 'Dear customer your msg is ' + message + ' Sent By FSMSG FSSMSS',
        },
        timeout=15,
    )



def sendmail(Mailid, message):
    """Send an email alert when SMTP settings are configured in the environment."""
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    fromaddr = os.getenv('SMTP_FROM', '')
    smtp_password = os.getenv('SMTP_PASSWORD', '')
    toaddr = Mailid
    if not fromaddr or not smtp_password or not toaddr:
        return

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Alert"

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    smtp_host = os.getenv('SMTP_HOST', 'smtp.gmail.com')
    smtp_port = int(os.getenv('SMTP_PORT', '587'))
    s = smtplib.SMTP(smtp_host, smtp_port)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, smtp_password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


if __name__ == '__main__':
    app.run(
        host=os.getenv('FLASK_HOST', '127.0.0.1'),
        port=int(os.getenv('FLASK_PORT', '5000')),
        debug=app.config['DEBUG'],
        use_reloader=app.config['DEBUG'],
    )
