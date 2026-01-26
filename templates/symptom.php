<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OralCare | Symptoms</title>
    <link rel="icon" href="{{ url_for('static', filename='images/DeltaNu_Logo.png') }}" type="image/png">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/question.css') }}">
</head>

<body>
    <div class="container">
        <form action="/symptom" method="post">
            <div class="question">
                <div class="question-title">Q1</div>
                <div class="options">
                    <label>
                        <input type="radio" name="Q1" value="0.0" required>
                        <span>Option 1</span>
                    </label>
                </div>
            </div>

            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>