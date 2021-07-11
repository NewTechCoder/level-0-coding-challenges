def common_letters(string_a, string_b):
    common_letter = ""
    string_a = string_a.lower()
    string_b = string_b.lower()
    for i in range(len(string_a)):
        if string_a[i] in string_b and string_a[i] not in common_letter:
            common_letter += string_a[i]
    print(f'letters: {", ".join(common_letter)}')

if __name__ == "__main__":
    common_letters("house", "Computers")
