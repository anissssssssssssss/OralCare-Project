<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OralCare | Risk Factors</title>
    <link rel="icon" href="{{ url_for('static', filename='images/DeltaNu_Logo.png') }}" type="image/png">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/question.css') }}">
</head>

<body>
    <div class="container">
        <div class="assessment-header">
            <h1>Risk Factors Assessment</h1>

            <p class="assessment-desc">
                Please answer the following questions honestly. Your responses will be used to
                evaluate lifestyle and background factors that may increase the risk of
                developing oral cancer.
                <br>
                <strong>Your answers will remain confidential and are only used for assessment purposes.</strong>
            </p>

            <div class="progress-wrapper">
                <div class="progress-text">Step 1 of 3</div>
                <div class="progress-bar">
                    <div class="progress-fill"></div>
                </div>
            </div>
        </div>

        <form action="/riskfactor" method="post">
            <div class="question">
                <div class="question-title">How often do you smoke or chew tobacco?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="tobacco" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="tobacco" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="tobacco" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="tobacco" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="tobacco" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="tobacco" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">How often do you consume alcoholic beverages?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="alcohol" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="alcohol" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="alcohol" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="alcohol" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="alcohol" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="alcohol" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Have your lips been frequently exposed to strong sunlight without protection?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="excessive_sun_exposure" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="excessive_sun_exposure" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="excessive_sun_exposure" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="excessive_sun_exposure" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="excessive_sun_exposure" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="excessive_sun_exposure" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Have you ever been diagnosed with Human Papillomavirus (HPV) by a healthcare professional?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="hpv_exposure" value="0.0" required>
                        <span>No</span>
                    </label>
                    <label>
                        <input type="radio" name="hpv_exposure" value="1.0" required>
                        <span>Yes</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Does anyone in your immediate family have a history of oral cancer?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="family_history" value="0.0" required>
                        <span>No</span>
                    </label>
                    <label>
                        <input type="radio" name="family_history" value="1.0" required>
                        <span>Yes</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Do you currently or previously chew betel quid (areca nut)?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="betel_quid" value="0.0" required>
                        <span>No</span>
                    </label>
                    <label>
                        <input type="radio" name="betel_quid" value="1.0" required>
                        <span>Yes</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">How often do you skip brushing/flossing?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="poor_oral_hygiene" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="poor_oral_hygiene" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="poor_oral_hygiene" value="0.4" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="poor_oral_hygiene" value="0.6" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="poor_oral_hygiene" value="0.8" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Have you been diagnosed with a condition that weakens your immune system (e.g. HIV)?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="immune_compromise" value="0.0" required>
                        <span>No</span>
                    </label>
                    <label>
                        <input type="radio" name="immune_compromise" value="1.0" required>
                        <span>Yes</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">What is your age? </div>
                <div class="options">
                    <label>
                        <input type="radio" name="age_over_45" value="0.0" required>
                        <span>Age < 45</span>
                    </label>
                    <label>
                        <input type="radio" name="age_over_45" value="0.5" required>
                        <span>Age >= 45</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">What is your gender?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="gender_male" value="0.45" required>
                        <span>Male</span>
                    </label>
                    <label>
                        <input type="radio" name="gender_male" value="0.0" required>
                        <span>Female</span>
                    </label>
                </div>
            </div>

            <div class="action">
                <a href="/symptom">
                    <button type="submit">Next</button>
                </a>
            </div>
        </form>
    </div>
</body>
</html>