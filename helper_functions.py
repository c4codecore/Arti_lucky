def count_vowels_consonant_upper_lower(text):
    vowels = "aeiouAEIOU"

    vowel_count = 0
    consonant_count = 0
    uppercase_count = 0
    lowercase_count = 0

    for ch in text:
        if ch.isalpha():                     # check only alphabets
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
            
            if ch.isupper():
                uppercase_count += 1
            elif ch.islower():
                lowercase_count += 1

    print("Number of vowels:", vowel_count)
    print(f"Number of consonants:{consonant_count}")
    print("Number of uppercase letters:{}".format(uppercase_count) )
    print("Number of lowercase letters:", lowercase_count)