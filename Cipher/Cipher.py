alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_word, shift_amount, direction):
    if direction == "cipher":
        ciphered = ''
        for i in original_word:
            if i in alphabet:
                index = alphabet.index(i)
                shifted_index = index + shift_amount
                if shifted_index > 25:
                    ciphered += alphabet[(shifted_index % 25) - 1]
                else:
                    ciphered += alphabet[shifted_index]
            else:
                ciphered += i
        return ciphered
    else:
        deciphered = ''
        for i in original_word:
            if i in alphabet:
                index = alphabet.index(i)
                deciphered += alphabet[index - shift_amount]
            else:
                deciphered += i
        return deciphered


cipher_and_decipher = (input("Do you want to cipher or decipher enter(cipher/decipher): ")).lower()
if cipher_and_decipher == "cipher" or cipher_and_decipher == "decipher":
    word = (input("enter the word: ")).lower()
    shift = int(input("enter the shift number(you can enter between 1 and 24): "))
    if (shift > 0) and (shift < 25):
        print(f"The {cipher_and_decipher}ed result is {caesar(word, shift, cipher_and_decipher)}")
    else:
        print("Please enter a number between 1 and 24")
else:
    print("Please enter cipher or decipher")

