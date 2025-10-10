% Medical Diagnosis Program

% Facts
symptom(fever).
symptom(cough).
symptom(headache).
symptom(running_nose).
symptom(sore_throat).
symptom(body_pain).

% Rules
disease(flu) :- symptom(fever), symptom(cough), symptom(body_pain).
disease(cold) :- symptom(running_nose), symptom(sore_throat).
disease(migraine) :- symptom(headache), \+ symptom(fever).

% Query example
diagnose(Disease) :- disease(Disease),
    write('You may be suffering from '), write(Disease), write('.'), nl.
