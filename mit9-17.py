def get_champion_slices(champions):
    champ1 = champions[3:]
    champ2 = champions[:-2]
    champ3 = champions[::2]

    return champ1, champ2, champ3

names = ["Spencer", "Bill", "Matthew", "Brandon", "Tony"]

print(get_champion_slices(names))