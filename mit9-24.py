def filter_messages(messages):
    clean_list = []
    junk_words_count = []

    for i in messages:
        words = i.split()
        print("test1", words)
        new_list = []
        counter = 0

        for i in words:
            if i == "dang":
                counter += 1
                junk_words_count.append(counter)
                print(junk_words_count)
            else:
                new_list.append(i)
                clean_sentence = " ".join(new_list)
                clean_list.append(clean_sentence)
                print(clean_list)
        

   



list1 = ["darn it", "this dang thing won't work", "lets fight one on one"]
list2 = ["darn it", "this thing won't work", "lets fight one on one"]
filter_messages(list2)
