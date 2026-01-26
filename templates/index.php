<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OralCare | Home</title>
    <link rel="icon" href="{{ url_for('static', filename='images/oralcare.png') }}" type="image/png">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}">
</head>

<body>
    <div class="container">
        <div class="left">
            <div class="logo-title">
                <img src="{{ url_for('static', filename='images/oralcare.png') }}" alt="oralcare" class="icon">
                <h1>OralCare</h1>
            </div>

            <div class="description">
                <p>Welcome to <strong>OralCare</strong>, your personal assistant for maintaining optimal oral health. Our tool helps you assess your oral hygiene habits and provides personalized recommendations.</p>
                <p>Take our quick assessment to understand your oral health better and receive tips tailored just for you!</p>
            </div>

            <div class="description">
                <strong>Note:</strong> This tool is for informational purposes only and does not replace professional dental advice.
            </div>

            <div class="action">
                <a href="/risk factor">
                    <button class="start-btn">Start Assessment</button>
                </a>
            </div>
        </div>

        <div class="right">
            <img src="{{ url_for('static', filename='images/illustration.png') }}" alt="Illustration" class="illustration">
        </div>
    </div>
</body>
</html>