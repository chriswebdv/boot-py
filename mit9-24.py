def filter_messages(messages):
    clean_list = []
    junk_list = []

    for i in range(len(messages)):
        str_from_list = " ".join(messages)
        if str_from_list[i]== "dang":
            junk_list.append(str_from_list[i])
            print("this", junk_list)
        else:
            clean_list.append(messages[i])
            print("this", clean_list)
            return clean_list



list1 = ["darn it", "this dang thing won't work", "lets fight one on one"]
list2 = ["darn it", "this thing won't work", "lets fight one on one"]
filter_messages(list1)
