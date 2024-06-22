def calculate_experience_points(level):
    for i in range(level):
        i *= 5
    return i * 2

calculate_experience_points(100)