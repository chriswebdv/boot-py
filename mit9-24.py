def filter_messages(messages):
    clean_list = []
    junk_words_count = []

    for i in range(len(messages)):
        words = messages[i].split()
        print("test1", words)
        new_list = []
        counter = 0

        if words[i] == "dang":
            counter += 1
            print(counter)
        else:
            print("print", words[i])
            new_list.append(words[i])
            print(new_list)
        

   



list1 = ["darn it", "this dang thing won't work", "lets fight one on one"]
list2 = ["darn it", "this thing won't work", "lets fight one on one"]
filter_messages(list1)
