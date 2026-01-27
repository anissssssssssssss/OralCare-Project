from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
from app import risk, symptoms

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

app.config['MAIL_DEBUG'] = True
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS').lower() in ['true', '1', 'yes']
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL').lower() in ['true', '1', 'yes']
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)
app.config['MAIL_DEBUG'] = True

@app.route('/')
def home():
    return render_template('index.php')

@app.route('/symptom')
def symptom():
    return render_template('symptom.php')

@app.route('/riskfactor', methods=['GET', 'POST'])
def riskfactor():
    if request.method == 'POST':
        answers = {
            'tobacco': request.form.get('tobacco', 0),
            'alcohol': request.form.get('alcohol', 0),
            'excessive_sun_exposure': request.form.get('excessive_sun_exposure', 0),
            'betel_quid': request.form.get('betel_quid', 0),
            'poor_oral_hygiene': request.form.get('poor_oral_hygiene', 0),
            'hpv_exposure': request.form.get('hpv_exposure', 0),
            'immune_compromise': request.form.get('immune_compromise', 0),
            'family_history': request.form.get('family_history', 0),
            'age_over_45': request.form.get('age_over_45', 0),
            'gender_male': request.form.get('gender_male', 0)
        }

        session['risk_level'] = risk_level
        risk_level = risk.calculate_risks(answers)
    return render_template('riskfactor.php')

@app.route('/result')
def result():
    return render_template('result.php')

@app.route('/send_email', methods=['POST'])
def send_email():
    recipient_email = request.form.get('email')

    subject = "Dental Health Assessment Result"
    body = f"""Hello,
Your dental health assessment result is as follows:

Please consult with a dental professional for further guidance.
Best regards,
OralCare Team

Disclaimer: This is an automated email. Please do not reply to this message.
"""
    try:
        msg = Message(subject, recipients=[recipient_email], body=body)
        mail.send(msg)
        return redirect(url_for('result', email_sent='success'))
    except Exception as e:
        print(f"Error sending email: {e}")
        return redirect(url_for('result', email_sent='failure'))
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)