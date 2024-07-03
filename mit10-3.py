def count_words(sen):
    count = 0
    for i in sen:
        if i == " ":
            count += 1
    return count + 1



print(count_words("God is good all the time"))