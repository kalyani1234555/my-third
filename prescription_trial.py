from prescription_data import *

# trial_patients = ["Denise", "Eddie", "Frank", "Georgia"]
trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    # if warfarin in prescription:
    try:
        # print(prescription)

        # prescription.discard(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"patient {patient} is not taking warfarin."
              f" please remove the patient from the trail ")
    print(patient, prescription)
