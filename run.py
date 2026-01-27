from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

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

@app.route('/riskfactor', methods=['GET', 'POST'])
def riskfactor():
    if request.method == 'POST':
        session['tobacco'] = request.form.get('tobacco')
        session['alcohol'] = request.form.get('alcohol')
        session['sunlight'] = request.form.get('sunlight')
        session['hpv'] = request.form.get('hpv')
        session['family_history'] = request.form.get('family_history')
        session['quid_nut'] = request.form.get('quid_nut')
        session['hygiene'] = request.form.get('hygiene')
        session['immune'] = request.form.get('immune')
        session['age'] = request.form.get('age')
        session['gender'] = request.form.get('gender')
        return redirect(url_for('symptom'))
    return render_template('riskfactor.php')

@app.route('/symptom', methods=['GET', 'POST'])
def symptom():
    if request.method == 'POST':
        session['ulcers'] = request.form.get('ulcers')
        session['bleeding'] = request.form.get('bleeding')
        session['swelling'] = request.form.get('swelling')
        session['nodes'] = request.form.get('nodes')
        session['patches'] = request.form.get('patches')
        session['swallow'] = request.form.get('swallow')
        session['pain'] = request.form.get('pain')
        session['teeth'] = request.form.get('teeth')
        session['numb'] = request.form.get('numb')
        session['speak'] = request.form.get('speak')
        return redirect(url_for('result'))
    return render_template('symptom.php')

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
        sender_email = ("OralCare Team", "sofiabtrsyia@gmail.com")
        msg = Message(subject, recipients=[recipient_email], body=body, sender=sender_email)
        mail.send(msg)
        return redirect(url_for('result', email_sent='success'))
    except Exception as e:
        print(f"Error sending email: {e}")
        return redirect(url_for('result', email_sent='failure'))
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)