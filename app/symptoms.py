import clips

def calculate_symptoms(answers):
    env = clips.Environment()
    env.reset()

    # Define the symptoms template for oral cancer
    env.build("""
    (deftemplate oral-symptoms
        (slot ulcers)
        (slot bleeding)
        (slot swelling_lump)
        (slot lymph_nodes)
        (slot patches)
        (slot difficulty_swallowing)
        (slot persistent_pain)
        (slot loose_teeth)
        (slot numbness)
        (slot difficulty_speaking)
    )
    """)

    # Define CF values for each symptoms
    env.build("""
    (deftemplate symptom-cf-values
        (slot cf_ulcers (default 0.8))
        (slot cf_bleeding (default 0.8))
        (slot cf_swelling (default 0.7))
        (slot cf_lymph (default 0.7))
        (slot cf_patches (default 0.7))
        (slot cf_swallowing (default 0.6))
        (slot cf_pain (default 0.6))
        (slot cf_teeth (default 0.5))
        (slot cf_numbness (default 0.5))
        (slot cf_speaking (default 0.5))
    )
    """)

    # Define the fired rules template
    env.build("""(deftemplate fired-symptom-rules (slot symptom))""")

    # Define the cancer risk level template
    env.build("""(deftemplate cancer-risk-level (slot level) (slot cf-combine))""")

    env.assert_string("(symptom-cf-values)")

    # Rule 11: Mouth ulcers that do not heal after two weeks
    env.build("""
    (defrule check-ulcers
        (oral-symptoms (ulcers ?answer))
        ?cf <- (symptom-cf-values (cf_ulcers ?cf_ulcers))
        (not (fired-symptom-rules (symptom "ulcers")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_ulcers))
        (modify ?cf (cf_ulcers ?cf-value))
        (assert (fired-symptom-rules (symptom "ulcers")))
    )
    """)

    # Rule 12: Bleeding in mouth without obvious cause
    env.build("""
    (defrule check-bleeding
        (oral-symptoms (bleeding ?answer))
        ?cf <- (symptom-cf-values (cf_bleeding ?cf_bleeding))
        (not (fired-symptom-rules (symptom "bleeding")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_bleeding))
        (modify ?cf (cf_bleeding ?cf-value))
        (assert (fired-symptom-rules (symptom "bleeding")))
    )
    """)

    # Rule 13: Swelling or lump inside mouth
    env.build("""
    (defrule check-swelling-lump
        (oral-symptoms (swelling_lump ?answer))
        ?cf <- (symptom-cf-values (cf_swelling ?cf_swelling))
        (not (fired-symptom-rules (symptom "swelling_lump")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_swelling))
        (modify ?cf (cf_swelling ?cf-value))
        (assert (fired-symptom-rules (symptom "swelling_lump")))
    )
    """)

    # Rule 14: Swelling in lymph nodes of neck/jaw
    env.build("""
    (defrule check-lymph-nodes
        (oral-symptoms (lymph_nodes ?answer))
        ?cf <- (symptom-cf-values (cf_lymph ?cf_lymph))
        (not (fired-symptom-rules (symptom "lymph_nodes")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_lymph))
        (modify ?cf (cf_lymph ?cf-value))
        (assert (fired-symptom-rules (symptom "lymph_nodes")))
    )
    """)

    # Rule 15: White or red patches inside mouth
    env.build("""
    (defrule check-patches
        (oral-symptoms (patches ?answer))
        ?cf <- (symptom-cf-values (cf_patches ?cf_patches))
        (not (fired-symptom-rules (symptom "patches")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_patches))
        (modify ?cf (cf_patches ?cf-value))
        (assert (fired-symptom-rules (symptom "patches")))
    )
    """)

    # Rule 16: Difficulty swallowing food or liquids
    env.build("""
    (defrule check-difficulty-swallowing
        (oral-symptoms (difficulty_swallowing ?answer))
        ?cf <- (symptom-cf-values (cf_swallowing ?cf_swallowing))
        (not (fired-symptom-rules (symptom "difficulty_swallowing")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_swallowing))
        (modify ?cf (cf_swallowing ?cf-value))
        (assert (fired-symptom-rules (symptom "difficulty_swallowing")))
    )
    """)

    # Rule 17: Persistent or ongoing pain in mouth
    env.build("""
    (defrule check-persistent-pain
        (oral-symptoms (persistent_pain ?answer))
        ?cf <- (symptom-cf-values (cf_pain ?cf_pain))
        (not (fired-symptom-rules (symptom "persistent_pain")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_pain))
        (modify ?cf (cf_pain ?cf-value))
        (assert (fired-symptom-rules (symptom "persistent_pain")))
    )
    """)

    # Rule 18: Loose teeth without injury/dental procedure
    env.build("""
    (defrule check-loose-teeth
        (oral-symptoms (loose_teeth ?answer))
        ?cf <- (symptom-cf-values (cf_teeth ?cf_teeth))
        (not (fired-symptom-rules (symptom "loose_teeth")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_teeth))
        (modify ?cf (cf_teeth ?cf-value))
        (assert (fired-symptom-rules (symptom "loose_teeth")))
    )
    """)

    # Rule 19: Numbness in mouth, lips, or face
    env.build("""
    (defrule check-numbness
        (oral-symptoms (numbness ?answer))
        ?cf <- (symptom-cf-values (cf_numbness ?cf_numbness))
        (not (fired-symptom-rules (symptom "numbness")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_numbness))
        (modify ?cf (cf_numbness ?cf-value))
        (assert (fired-symptom-rules (symptom "numbness")))
    )
    """)

    # Rule 20: Difficulty speaking clearly
    env.build("""
    (defrule check-difficulty-speaking
        (oral-symptoms (difficulty_speaking ?answer))
        ?cf <- (symptom-cf-values (cf_speaking ?cf_speaking))
        (not (fired-symptom-rules (symptom "difficulty_speaking")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_speaking))
        (modify ?cf (cf_speaking ?cf-value))
        (assert (fired-symptom-rules (symptom "difficulty_speaking")))
    )
    """)

    # Combine all CF values using the certainty factor combination formula
    env.build("""
    (defrule calculate-cancer-risk
        (symptom-cf-values 
            (cf_ulcers ?cf1) 
            (cf_bleeding ?cf2) 
            (cf_swelling ?cf3) 
            (cf_lymph ?cf4) 
            (cf_patches ?cf5)
            (cf_swallowing ?cf6)
            (cf_pain ?cf7)
            (cf_teeth ?cf8)
            (cf_numbness ?cf9)
            (cf_speaking ?cf10)
        )
        =>
        (bind ?cf-combine-1 (+ ?cf1 (* ?cf2 (- 1 ?cf1))))
        (bind ?cf-combine-2 (+ ?cf-combine-1 (* ?cf3 (- 1 ?cf-combine-1))))
        (bind ?cf-combine-3 (+ ?cf-combine-2 (* ?cf4 (- 1 ?cf-combine-2))))
        (bind ?cf-combine-4 (+ ?cf-combine-3 (* ?cf5 (- 1 ?cf-combine-3))))
        (bind ?cf-combine-5 (+ ?cf-combine-4 (* ?cf6 (- 1 ?cf-combine-4))))
        (bind ?cf-combine-6 (+ ?cf-combine-5 (* ?cf7 (- 1 ?cf-combine-5))))
        (bind ?cf-combine-7 (+ ?cf-combine-6 (* ?cf8 (- 1 ?cf-combine-6))))
        (bind ?cf-combine-8 (+ ?cf-combine-7 (* ?cf9 (- 1 ?cf-combine-7))))
        (bind ?cf-combine-9 (+ ?cf-combine-8 (* ?cf10 (- 1 ?cf-combine-8))))
        
        (if (<= ?cf-combine-9 0.1) then
            (assert (cancer-risk-level (cf-combine ?cf-combine-9) (level "Very Low Risk")))
        else
            (if (<= ?cf-combine-9 0.3) then
                (assert (cancer-risk-level (cf-combine ?cf-combine-9) (level "Low Risk")))
            else
                (if (<= ?cf-combine-9 0.5) then
                    (assert (cancer-risk-level (cf-combine ?cf-combine-9) (level "Moderate Risk")))
                else
                    (if (<= ?cf-combine-9 0.7) then
                        (assert (cancer-risk-level (cf-combine ?cf-combine-9) (level "High Risk")))
                    else
                        (assert (cancer-risk-level (cf-combine ?cf-combine-9) (level "Very High Risk - Immediate Consultation Recommended")))
                    )
                )
            )
        )
    )
    """)

    # Return the result
    env.build("""
    (defrule result
        (cancer-risk-level (level ?level) (cf-combine ?cf-combine))
        =>
        (bind ?percentage (* ?cf-combine 100))
        (halt)
    )
    """)

    # Assert the user's answers
    env.assert_string(f'(oral-symptoms '
                      f'(ulcers {float(answers.get("ulcers", 0))}) '
                      f'(bleeding {float(answers.get("bleeding", 0))}) '
                      f'(swelling_lump {float(answers.get("swelling_lump", 0))}) '
                      f'(lymph_nodes {float(answers.get("lymph_nodes", 0))}) '
                      f'(patches {float(answers.get("patches", 0))}) '
                      f'(difficulty_swallowing {float(answers.get("difficulty_swallowing", 0))}) '
                      f'(persistent_pain {float(answers.get("persistent_pain", 0))}) '
                      f'(loose_teeth {float(answers.get("loose_teeth", 0))}) '
                      f'(numbness {float(answers.get("numbness", 0))}) '
                      f'(difficulty_speaking {float(answers.get("difficulty_speaking", 0))}))')

    env.run()

    # Extract and return the results
    for fact in env.facts():
        if fact.template.name == 'cancer-risk-level':
            risk_level = fact['level']
            certainty_score = f"{(fact['cf-combine'] * 100):.2f}%"
            return risk_level, certainty_score
    
    return "No assessment possible", "0%"