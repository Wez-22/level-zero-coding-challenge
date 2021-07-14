def common_letters(word1, word2):
    print("Common letters: ", end="")
    for i in word1:
        if i in word2:
            print(i, end=", ")


common_letters("house", "computers")
