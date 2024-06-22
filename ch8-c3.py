def calculate_experience_points(level):
    count = 0
    for i in range(0, level):
        count += 1
        i *= count
        return i

