import clips

(deftemplate user-input
   (slot tobacco)
   (slot alcohol)
   (slot excessive_sun_exposure)
   (slot hpv_exposure)
   (slot family_history)
   (slot betel_quid)
   (slot poor_oral_hygiene)
   (slot immune_compromise)
   (slot age_over_45)
   (slot gender)
)

(deftemplate cf-value
   (slot hypothesis)
   (slot value)
)
CF[12, E] = CF_user × CF_expert.
(defrule rule-name
   (symptom-input (slot-name ?u))
=>
   (bind ?cf (* ?u EXPERT_CF))
   (assert (cf-value (hypothesis H1) (rule rule-name) (value ?cf)))
)
(defrule r1-tobacco
   (user-input (tobacco ?u&:(> ?u 0)))
=>
   (assert (cf-value (hypothesis H1) (value (* ?u 0.90))))
)

(defrule r2-alcohol
   (user-input (alcohol ?u&:(> ?u 0)))
=>
   (assert (cf-value (hypothesis H1) (value (* ?u 0.85))))
)

(defrule r3-sun-exposure
   (user-input (excessive_sun_exposure ?u&:(> ?u 0)))
=>
   (assert (cf-value (hypothesis H1) (value (* ?u 0.45))))
)

(defrule r4-betel-quid
   (user-input (betel_quid ?u&:(> ?u 0)))
=>
   (assert (cf-value (hypothesis H1) (value (* ?u 0.70))))
)

(defrule r5-poor-hygiene
   (user-input (poor_oral_hygiene ?u&:(> ?u 0)))
=>
   (assert (cf-value (hypothesis H1) (value (* ?u 0.50))))
)

(defrule r6-hpv
   (user-input (hpv_exposure ?u&:(> ?u 0)))
=>
   (assert (cf-value (hypothesis H1) (value (* ?u 0.70))))
)

(defrule r7-immune
   (user-input (immune_compromise ?u&:(> ?u 0)))
=>
   (assert (cf-value (hypothesis H1) (value (* ?u 0.75))))
)

(defrule r8-family-history
   (user-input (family_history ?u&:(> ?u 0)))
=>
   (assert (cf-value (hypothesis H1) (value (* ?u 0.60))))
)

(defrule r9-age
   (user-input (age_over_45 ?u&:(> ?u 0)))
=>
   (assert (cf-value (hypothesis H1) (value (* ?u 0.65))))
)

(defrule r10-gender
   (user-input (gender ?u&:(> ?u 0)))
=>
   (assert (cf-value (hypothesis H1) (value (* ?u 0.55))))
)

(defrule r11-tobacco-alcohol
   (user-input (tobacco ?u1&:(> ?u1 0))
               (alcohol ?u2&:(> ?u2 0)))
=>
   (bind ?u (min ?u1 ?u2))
   (assert (cf-value (hypothesis H1) (value (* ?u 0.90))))
)

(defrule combine-cf-h1
   ?c1 <- (cf-value (hypothesis H1) (value ?v1))
   ?c2 <- (cf-value (hypothesis H1) (value ?v2&:(> ?v2 ?v1)))
=>
   (bind ?newcf (+ ?v1 (* ?v2 (- 1 ?v1))))
   (retract ?c1 ?c2)
   (assert (cf-value (hypothesis H1) (value ?newcf)))
)
