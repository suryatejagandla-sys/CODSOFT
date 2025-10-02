# Password Generator (CLI)
import random, string

def generate(length=12, use_upper=True, use_digits=True, use_punc=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_punc:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    try:
        length = int(input("Password length (e.g. 12): ") or "12")
    except:
        length = 12
    upper = input("Include uppercase? (Y/n): ").strip().lower() != 'n'
    digits = input("Include digits? (Y/n): ").strip().lower() != 'n'
    punc = input("Include punctuation? (Y/n): ").strip().lower() != 'n'
    pwd = generate(length, upper, digits, punc)
    print("Generated password:\n", pwd)

if __name__ == '__main__':
    main()
