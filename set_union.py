# farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
# wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
#
# all_animals_1 = farm_animals.union(wild_animals)
# print(all_animals_1)
#
# all_animals_2 = wild_animals.union(farm_animals)
# print(all_animals_2)
#
# all_animals_3 = wild_animals | farm_animals
# print(all_animals_3)

from prescription_data import adverse_interactions

meds_to_watch = set()

# for interaction in adverse_interactions:
#     meds_to_watch = meds_to_watch.union(interaction)
#     # meds_to_watch = meds_to_watch | interaction
#     # meds_to_watch.update(interaction)
#     # meds_to_watch |= interaction

# Not to use this method
# meds_to_watch.update(adverse_interactions[0],
#                      adverse_interactions[1],
#                      adverse_interactions[2],
#                      adverse_interactions[3],
#                      adverse_interactions[4],
#                      adverse_interactions[5],
#                      adverse_interactions[6],)

# need to use this method
meds_to_watch.update(*adverse_interactions)
# print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep='\n')
