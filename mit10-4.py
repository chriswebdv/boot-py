def sort_words(sen):
    sorted_words = sen.split()
    sorted_again = sorted(sorted_words)
    return sorted_again

print(sort_words("look at this photo"))