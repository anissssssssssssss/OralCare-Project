import clips

def calculate_risks(answers):
    env = clips.Environment()
    env.reset()

    # Define the symptoms template for oral cancer
    env.build("""
    (deftemplate oral-cancer-risks
        (slot tobacco)
        (slot alcohol)
        (slot excessive_sun_exposure)
        (slot betel_quid)
        (slot poor_oral_hygiene)
        (slot hpv_exposure)
        (slot immune_compromise)
        (slot family_history)
        (slot age_over_45)
        (slot gender_male)
    )
    """)

    # Define CF values for each symptoms
    env.build("""
    (deftemplate risks-cf-values
        (slot cf_tobacco (default 0.89))
        (slot cf_alcohol (default 0.85))
        (slot cf_excessive_sun_exposure (default 0.45))
        (slot cf_betel_quid (default 0.7))
        (slot cf_poor_oral_hygiene (default 0.5))
        (slot cf_hpv_exposure (default 0.7))
        (slot cf_immune_compromise (default 0.75))
        (slot cf_family_history (default 0.6))
        (slot cf_age_over_45 (default 0.5))
        (slot cf_gender_male (default 0.45))
    )
    """)

    # Define the fired rules template
    env.build("""(deftemplate fired-risks-rules (slot oral-cancer-risks))""")

    # Define the cancer risk level template
    env.build("""(deftemplate cancer-risk-level (slot level) (slot cf-combine))""")

    env.assert_string("(risks-cf-values)")

    # Rule 1: tobacco intake
    env.build("""
    (defrule check-tobacco
        (oral-cancer-risks (tobacco ?answer))
        ?cf <- (risks-cf-values (cf_tobacco ?cf_tobacco))
        (not (fired-risks-rules (oral-cancer-risks "tobacco")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_tobacco))
        (modify ?cf (cf_tobacco ?cf-value))
        (assert (fired-risks-rules (oral-cancer-risks "tobacco")))
    )
    """)

    # Rule 2: alcohol intake
    env.build("""
    (defrule check-alcohol
        (oral-cancer-risks (alcohol ?answer))
        ?cf <- (risks-cf-values (cf_alcohol ?cf_alcohol))
        (not (fired-risks-rules (oral-cancer-risks "alcohol")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_alcohol))
        (modify ?cf (cf_alcohol ?cf-value))
        (assert (fired-risks-rules (oral-cancer-risks "alcohol")))
    )
    """)

    # Rule 3: Excessive sun exposure
    env.build("""
    (defrule check-excessive-sun-exposure
        (oral-cancer-risks (excessive_sun_exposure ?answer))
        ?cf <- (risks-cf-values (cf_excessive_sun_exposure ?cf_excessive_sun_exposure))
        (not (fired-risks-rules (oral-cancer-risks "excessive_sun_exposure")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_excessive_sun_exposure))
        (modify ?cf (cf_excessive_sun_exposure ?cf-value))
        (assert (fired-risks-rules (oral-cancer-risks "excessive_sun_exposure")))
    )
    """)

    # Rule 4: HPV exposure
    env.build("""
    (defrule check-hpv-exposure
        (oral-cancer-risks (hpv_exposure ?answer))
        ?cf <- (risks-cf-values (cf_hpv_exposure ?cf_hpv_exposure))
        (not (fired-risks-rules (oral-cancer-risks "hpv_exposure")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_hpv_exposure))
        (modify ?cf (cf_hpv_exposure ?cf-value))
        (assert (fired-risks-rules (oral-cancer-risks "hpv_exposure")))
    )
    """)

    # Rule 5: family history
    env.build("""
    (defrule check-family-history
        (oral-cancer-risks (family_history ?answer))
        ?cf <- (risks-cf-values (cf_family_history ?cf_family_history))
        (not (fired-risks-rules (oral-cancer-risks "family_history")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_family_history))
        (modify ?cf (cf_family_history ?cf-value))
        (assert (fired-risks-rules (oral-cancer-risks "family_history")))
    )
    """)

    # Rule 6: betel quid consumption
    env.build("""
    (defrule check-betel-quid
        (oral-cancer-risks (betel_quid ?answer))
        ?cf <- (risks-cf-values (cf_betel_quid ?cf_betel_quid))
        (not (fired-risks-rules (oral-cancer-risks "betel_quid")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_betel_quid))
        (modify ?cf (cf_betel_quid ?cf-value))
        (assert (fired-risks-rules (oral-cancer-risks "betel_quid")))
    )
    """)

        # Rule 7: Poor oral hygiene
    env.build("""
    (defrule check-poor-oral-hygiene
        (oral-cancer-risks (poor_oral_hygiene ?answer))
        ?cf <- (risks-cf-values (cf_poor_oral_hygiene ?cf_poor_oral_hygiene))
        (not (fired-risks-rules (oral-cancer-risks "poor_oral_hygiene")))
        =>
        (bind ?cf-value (* (-1 (float ?answer)) ?cf_poor_oral_hygiene))
        (modify ?cf (cf_poor_oral_hygiene ?cf-value))
        (assert (fired-risks-rules (oral-cancer-risks "poor_oral_hygiene")))
    )
    """)

    # Rule 8: Immune compromise
    env.build("""
    (defrule check-immune-compromise
        (oral-cancer-risks (immune_compromise ?answer))
        ?cf <- (risks-cf-values (cf_immune_compromise ?cf_immune_compromise))
        (not (fired-risks-rules (oral-cancer-risks "immune_compromise")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_immune_compromise))
        (modify ?cf (cf_immune_compromise ?cf-value))
        (assert (fired-risks-rules (oral-cancer-risks "immune_compromise")))
    )
    """)

    # Rule 9: Age over 45
    env.build("""
    (defrule check-age-over-45
        (oral-cancer-risks (age_over_45 ?answer))
        ?cf <- (risks-cf-values (cf_age_over_45 ?cf_age_over_45))
        (not (fired-risks-rules (oral-cancer-risks "age_over_45")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_age_over_45))
        (modify ?cf (cf_age_over_45 ?cf-value))
        (assert (fired-risks-rules (oral-cancer-risks "age_over_45")))
    )
    """)
    
    # Rule 10: Gender male
    env.build("""
    (defrule check-gender-male
        (oral-cancer-risks (gender_male ?answer))
        ?cf <- (risks-cf-values (cf_gender_male ?cf_gender_male))
        (not (fired-risks-rules (oral-cancer-risks "gender_male")))
        =>
        (bind ?cf-value (* (float ?answer) ?cf_gender_male))
        (modify ?cf (cf_gender_male ?cf-value))
        (assert (fired-risks-rules (oral-cancer-risks "gender_male")))
    )
    """)

    # Combine all CF values using the certainty factor combination formula
    env.build("""
    (defrule calculate-cancer-risk
        (risks-cf-values 
            (cf_tobacco ?cf1) 
            (cf_alcohol ?cf2) 
            (cf_excessive_sun_exposure ?cf3) 
            (cf_betel_quid ?cf4) 
            (cf_poor_oral_hygiene ?cf5)
            (cf_hpv_exposure ?cf6)
            (cf_immune_compromise ?cf7)
            (cf_family_history ?cf8)
            (cf_age_over_45 ?cf9)
            (cf_gender_male ?cf10)
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
                        (assert (cancer-risk-level (cf-combine ?cf-combine-9) (level "Very High Risk - First Step Prevention Needed")))
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
                      f'(tobacco {float(answers.get("tobacco", 0))}) '
                      f'(alcohol {float(answers.get("alcohol", 0))}) '
                      f'(excessive_sun_exposure {float(answers.get("excessive_sun_exposure", 0))}) '
                      f'(betel_quid {float(answers.get("betel_quid", 0))}) '
                      f'(poor_oral_hygiene {float(answers.get("poor_oral_hygiene", 0))}) '
                      f'(hpv_exposure {float(answers.get("hpv_exposure", 0))}) '
                      f'(immune_compromise {float(answers.get("immune_compromise", 0))}) '
                      f'(family_history {float(answers.get("family_history", 0))}) '
                      f'(age_over_45 {float(answers.get("age_over_45", 0))}) '
                      f'(gender_male {float(answers.get("gender_male", 0))}))')

    env.run()

    # Extract and return the results
    for fact in env.facts():
        if fact.template.name == 'cancer-risk-level':
            risk_level = fact['level']
            certainty_score = f"{(fact['cf-combine'] * 100):.2f}%"
            return risk_level, certainty_score
    
    return "No assessment possible", "0%"