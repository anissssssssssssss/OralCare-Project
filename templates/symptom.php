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
        <div class="assessment-header">
            <h1>Symptom Assessment</h1>

            <p class="assessment-desc">
                    Please answer the following questions honestly. This section evaluates the presence and frequency of symptoms commonly associated with oral cancer.
                <br>
                <strong>Your answers will remain confidential and are only used for assessment purposes.</strong>
            </p>

            <div class="progress-wrapper">
                <div class="progress-text">Step 2 of 3</div>
                <div class="progress-bar">
                    <div class="progress-fill"></div>
                </div>
            </div>
        </div>

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
                        <input type="radio" name="swelling_lump" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="swelling_lump" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="swelling_lump" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="swelling_lump" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="swelling_lump" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="swelling_lump" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>   
            
            <div class="question">
                <div class="question-title">How often do you experience swelling in the lymph nodes of your neck or jaw area?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="lymph_nodes" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="lymph_nodes" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="lymph_nodes" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="lymph_nodes" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="lymph_nodes" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="lymph_nodes" value="1.0" required>
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
                        <input type="radio" name="difficulty_swallowing" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="difficulty_swallowing" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="difficulty_swallowing" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="difficulty_swallowing" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="difficulty_swallowing" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="difficulty_swallowing" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>     

            <div class="question">
                <div class="question-title">How often do you experience persistent or ongoing pain in your mouth?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="persistent_pain" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="persistent_pain" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="persistent_pain" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="persistent_pain" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="persistent_pain" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="persistent_pain" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">How often do you notice loose teeth without any injury or dental procedure?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="loose_teeth" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="loose_teeth" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="loose_teeth" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="loose_teeth" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="loose_teeth" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="loose_teeth" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">How often do you experience numbness in your mouth, lips, or face?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="numbness" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="numbness" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="numbness" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="numbness" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="numbness" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="numbness" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">How often do you experience difficulty speaking clearly?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="difficulty_speaking" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="difficulty_speaking" value="0.2" required>
                        <span>Occasionally</span>
                    </label>
                    <label>
                        <input type="radio" name="difficulty_speaking" value="0.4" required>
                        <span>Regularly</span>
                    </label>
                    <label>
                        <input type="radio" name="difficulty_speaking" value="0.6" required>
                        <span>Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="difficulty_speaking" value="0.8" required>
                        <span>Very Frequently</span>
                    </label>
                    <label>
                        <input type="radio" name="difficulty_speaking" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>            

            <div class="action">
                <a href="/riskfactor">
                    <button type="button">Back</button>
                </a>
                <a href="/result">
                    <button type="submit">Submit</button>
                </a>
            </div>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            document.querySelector('.progress-fill').style.width = '33.33%';
        });

        function updateProgressBar() {
            const radioButtons = document.querySelectorAll('input[type="radio"]');
            const checkedCount = document.querySelectorAll('input[type="radio"]:checked').length;
            const progressPercentage = (checkedCount / 10) * 33.33 + 33.33; 
            
            const progressFill = document.querySelector('.progress-fill');
            progressFill.style.width = progressPercentage + '%';
        }

        document.querySelectorAll('input[type="radio"]').forEach(radio => {
            radio.addEventListener('change', updateProgressBar);
        });
    </script>
</body>
</html>