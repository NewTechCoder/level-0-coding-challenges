def vowels(word):
    vowel = ""
    for letter in word:
        letter = letter.lower()
        if letter in "aeiou" and letter not in vowel:
            vowel += letter
    print(f'Vowels: {", ".join(vowel)}')

if __name__ == "__main__":
    vowels("Umuzi")

