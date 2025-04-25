from prescription_data import patients
trial_patient = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

while trial_patient:
    patient = trial_patient.pop()
    print(patient, end= " : ")
    prescription = patients[patient]
    print(prescription)
