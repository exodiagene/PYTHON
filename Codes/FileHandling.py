while True:
    filename = input("\nEnter Filename: ")
    try:
        file = open(filename+".txt")
        wordcount = {}

        for word in file.read().split():
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
        print("Word ")
        for k, v in wordcount.items():
            print(k, '{}'.format(":\t"), v)
    except:
        print("INVALID FILENAME")

    if input("Do you want to Continue: ") != "y".casefold():
        break
