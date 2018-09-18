def countvowels():
    vowels =['a','e', 'i','o','u']
    letters = input("enter a sentence:")
    tuple(vowels)
    tuple(letters)
    dup_vowels=set(letters)
    dup = len(letters)- len(dup_vowels)
    count = ""
    for char in vowels:
        if char in letters:
             count +=str(char)
    print ((count, dup) )
countvowels()