import clips

ANSWERS = {
    "Never": 0.0,
    "Occasionally": 0.2,
    "Regularly": 0.4,
    "Frequently": 0.6,
    "Very Frequently": 0.8,
    "Always": 1.0,
}

def calc_oral_cancer_score(ui_answers):

    env = clips.Environment()
    env.reset()

    # Build templates
    env.build("""
    (deftemplate symptom
        (slot name)
        (slot cf))

    (deftemplate hypothesis
        (slot name)
        (slot cf))
    """)

    # Build rules
    env.build("""
    (defrule tobacco-risk
        (symptom (name tobacco_use) (cf ?c))
        ?h <- (hypothesis (name H1) (cf ?old))
        =>
        (bind ?new (+ ?old (* (* ?c 0.90) (- 1 ?old))))
        (modify ?h (cf ?new)))
    """)

    env.build("""
    (defrule tobacco-alcohol-risk
        (symptom (name tobacco_use) (cf ?c1))
        (symptom (name alcohol_use) (cf ?c2))
        ?h <- (hypothesis (name H1) (cf ?old))
        =>
        (bind ?cf-and (min ?c1 ?c2))
        (bind ?new (+ ?old (* (* ?cf-and 0.85) (- 1 ?old))))
        (modify ?h (cf ?new)))
    """)

    env.build("""
    (defrule non-healing-ulcer
        (symptom (name non_healing_ulcer) (cf ?c))
        ?h <- (hypothesis (name H2) (cf ?old))
        =>
        (bind ?new (+ ?old (* (* ?c 0.80) (- 1 ?old))))
        (modify ?h (cf ?new)))
    """)

    env.build("""
    (defrule ulcer-and-bleeding
        (symptom (name non_healing_ulcer) (cf ?c1))
        (symptom (name bleeding_mouth) (cf ?c2))
        ?h <- (hypothesis (name H2) (cf ?old))
        =>
        (bind ?cf-and (min ?c1 ?c2))
        (bind ?new (+ ?old (* (* ?cf-and 0.90) (- 1 ?old))))
        (modify ?h (cf ?new)))
    """)

    # Initialize hypotheses
    env.assert_string('(hypothesis (name H1) (cf 0.0))')
    env.assert_string('(hypothesis (name H2) (cf 0.0))')


    # Assert symptoms from UI
    for symptom, answer in ui_answers.items():
        cf = ANSWERS[answer]
        env.assert_string(
            f'(symptom (name {symptom}) (cf {cf}))'
        )

    # Run inference
    env.run()

    # Collect results
    results = {}
    for fact in env.facts():
        if fact.template.name == "hypothesis":
            results[fact["name"]] = round(fact["cf"], 2)

    return results
