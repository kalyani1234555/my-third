morning = {'Java', 'C', 'Rubby', 'Lisp', 'C#'}
afternoon = {'Python', 'C#', 'Java', 'C', 'Rubby'}

possible_courses = morning ^ afternoon  # operators can work only sets
print(possible_courses)

morning1 = ['Java', 'C', 'Rubby', 'Lisp', 'C#']
afternoon1 = ['Python', 'C#', 'Java', 'C', 'Rubby']

possible_courses1 = set(morning1).symmetric_difference(afternoon1)  # methods can work for both list and sets
print(possible_courses1)

possible_courses1 = set(afternoon1).symmetric_difference(morning1)  # methods can work for both list and sets
print(possible_courses1)
