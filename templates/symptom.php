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
                <div class="question-title">How often do you have mouth ulcers that do not heal after two weeks?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="ulcers" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="ulcers" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="ulcers" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="ulcers" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="ulcers" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="ulcers" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">How often do you experience bleeding in your mouth without an obvious cause?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="bleeding" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="bleeding" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="bleeding" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="bleeding" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="bleeding" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="bleeding" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">How often do you notice any swelling or lump inside your mouth?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="swelling" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="swelling" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="swelling" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="swelling" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="swelling" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="swelling" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>   
            
            <div class="question">
                <div class="question-title">How often do you experience swelling in the lymph nodes of your neck or jaw area?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="nodes" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="nodes" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="nodes" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="nodes" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="nodes" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="nodes" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>     

            <div class="question">
                <div class="question-title">How often do you notice white or red patches on the inside of your mouth?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="patches" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="patches" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="patches" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="patches" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="patches" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="patches" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>                 
            
            <div class="question">
                <div class="question-title">How often do you experience difficulty swallowing food or liquids?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="swallow" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="swallow" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="swallow" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="swallow" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="swallow" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="swallow" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>     

            <div class="question">
                <div class="question-title">How often do you experience persistent or ongoing pain in your mouth?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="pain" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="pain" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="pain" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="pain" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="pain" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="pain" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">How often do you notice loose teeth without any injury or dental procedure?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="teeth" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="teeth" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="teeth" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="teeth" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="teeth" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="teeth" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">How often do you experience numbness in your mouth, lips, or face?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="numb" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="numb" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="numb" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="numb" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="numb" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="numb" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">How often do you experience difficulty speaking clearly?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="speak" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="speak" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="speak" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="speak" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="speak" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="speak" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>            

            <div class="action">
                <a href="/result">
                    <button type="submit">Submit</button>
                </a>
            </div>
        </form>
    </div>
</body>
</html>