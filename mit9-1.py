vowels = ("a", "e", "i", "o", "u")
def char_counts(s):
    total_vowels = 0
    total_consonants = 0
    for i in range(0, len(s)):
        if s[i] in vowels:
            total_vowels += len(s[i])
        else:
            total_consonants += len(s[i])

    return (total_vowels, total_consonants)

print(char_counts("valparaisos"))
