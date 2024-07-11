def find_grades(grades, students):
    new_list = []
    for elem in students:
        grade = grades[elem]
        new_list.append(grade)
    return new_list

d = {"Ana": "B", "Matt": "C", "John": "B", "Katy": "A"}

print(find_grades(d, ["Matt", "Katy"]))

        
