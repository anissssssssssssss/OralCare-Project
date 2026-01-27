<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OralCare | Results</title>
    <link rel="icon" href="{{ url_for('static', filename='images/DeltaNu_Logo.png') }}" type="image/png">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/result.css') }}">
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <script src="{{ url_for('static', filename='js/popup.js') }}" defer></script>
</head>

<body>
    <div class="container">
        <h1>Assessment Results</h1>
        <p>Your results are displayed here.</p>
        <div class="results">
            <div class="result-item">
                <strong>Risk Factor Assessment:</strong>
                <p>{{ risks_level }} (Certainty Level: {{ certainty_score }})</p>
            </div>
            <div class="result-item">
                <strong>Symptom Assessment:</strong>
                <p>{{ symptom_level }} (Certainty Level: {{ symptom_certainty_score }})</p>
            </div>
        </div>
        <p class="disclaimer">Disclaimer: This assessment is provided for informational purposes only and is not intended to replace professional medical advice, diagnosis, or treatment. Please consult a qualified healthcare professional for an accurate evaluation.</p>

        <form action="/send_email" method="POST" id="emailForm">
            <label for="email">Enter your email address to receive a copy of this assessment:</label>
            <input type="email" id="email" name="email" placeholder="your-email@example.com" required>
            <button id="send" type="submit">Send My Results</button>
        </form>

        <a href="/" class="retake-link">Retake Assessment</a>
    </div>
</body>
</html>