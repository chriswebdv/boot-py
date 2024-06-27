vowels = ("a", "e", "i", "o", "u")
def char_counts(s):
    total_vowels = 0
    for i in range(0, len(s)):
        if s[i] in vowels:
            total_vowels += len(s[i])
    print(total_vowels)

char_counts("tanko")