def only_print_the_vowels(string):
    print("Vowels: ",end="")
    for i in string:
        if i in "aeiou":
            print(i, end=" ")

only_print_the_vowels("Umuzi")