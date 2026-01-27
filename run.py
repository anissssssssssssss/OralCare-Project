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

@app.route('/riskfactor', methods=['GET', 'POST'])
def riskfactor():
    if request.method == 'POST':
        answers = {
            'tobacco': request.form.get('tobacco'),
            'alcohol': request.form.get('alcohol'),
            'excessive_sun_exposure': request.form.get('excessive_sun_exposure'),
            'hpv_exposure': request.form.get('hpv_exposure'),
            'family_history': request.form.get('family_history'),
            'betel_quid': request.form.get('betel_quid'),
            'poor_oral_hygiene': request.form.get('poor_oral_hygiene'),
            'immune_compromise': request.form.get('immune_compromise'),
            'age_over_45': request.form.get('age_over_45'),
            'gender_male': request.form.get('gender_male')
        }
        session['answers'] = answers
        return redirect(url_for('symptom'))
    return render_template('riskfactor.php')

@app.route('/symptom', methods=['GET', 'POST'])
def symptom():
    if request.method == 'POST':
        answers = {
            'ulcers': request.form.get('ulcers'),
            'bleeding': request.form.get('bleeding'),
            'swelling_lump': request.form.get('swelling_lump'),
            'lymph_nodes': request.form.get('lymph_nodes'),
            'patches': request.form.get('patches'),
            'difficulty_swallowing': request.form.get('difficulty_swallowing'),
            'persistent_pain': request.form.get('persistent_pain'),
            'loose_teeth': request.form.get('loose_teeth'),
            'numbness': request.form.get('numbness'),
            'difficulty_speaking': request.form.get('difficulty_speaking')
        }

        session['answers'] = {
            **session.get('answers', {}),
            **answers
        }

        return redirect(url_for('result'))
    return render_template('symptom.php')

@app.route('/result')
def result():
    answers = session.get('answers')
    if not answers:
        return redirect(url_for('riskfactor'))
    
    cancer_riskfactor_level, risk_certainty_score = risk.calculate_risks(answers)
    symptom_level, symptom_certainty_score = symptoms.calculate_symptoms(answers)
    
    session['risks_level'] = cancer_riskfactor_level
    session['certainty_score'] = risk_certainty_score
    session['symptom_level'] = symptom_level
    session['symptom_certainty_score'] = symptom_certainty_score

    return render_template('result.php', risks_level=cancer_riskfactor_level, certainty_score=risk_certainty_score, 
                           symptom_level=symptom_level, symptom_certainty_score=symptom_certainty_score)

@app.route('/send_email', methods=['POST'])
def send_email():
    recipient_email = request.form.get('email')

    # Get the assessment results from session
    risks_level = session.get('risks_level', 'Not Available')
    certainty_score = session.get('certainty_score', 'Not Available')
    symptom_level = session.get('symptom_level', 'Not Available')
    symptom_certainty_score = session.get('symptom_certainty_score', 'Not Available')

    subject = "Dental Health Assessment Result"
    body = f"""Hello,

Your dental health assessment result is as follows:

Risk Factor Assessment: {risks_level} (Certainty Level: {certainty_score})
Symptom Assessment: {symptom_level} (Certainty Level: {symptom_certainty_score})

Please consult with a dental professional for further guidance and accurate evaluation.

Best regards,
OralCare Team

Disclaimer: This is an automated email. Please do not reply to this message. This assessment is provided for informational purposes only and is not intended to replace professional medical advice, diagnosis, or treatment.
"""
    try:
        print(f"Attempting to send email to: {recipient_email}")
        print(f"Mail server: {app.config.get('MAIL_SERVER')}")
        print(f"Mail port: {app.config.get('MAIL_PORT')}")
        print(f"Mail username: {app.config.get('MAIL_USERNAME')}")
        print(f"Mail use TLS: {app.config.get('MAIL_USE_TLS')}")
        
        msg = Message(subject, recipients=[recipient_email], body=body)
        mail.send(msg)
        print("Email sent successfully!")
        return redirect(url_for('result', email_sent='success'))
    except Exception as e:
        print(f"Error sending email: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return redirect(url_for('result', email_sent='failure'))
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)