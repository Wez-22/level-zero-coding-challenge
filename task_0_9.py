def finding_vowels(string):
    print("Vowels: ", end="")
    for i in string:
        if i in "aeiou":
            print(i, end=", ")


finding_vowels("Umuzi")
