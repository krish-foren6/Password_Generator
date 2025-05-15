import argparse
import secrets
import string
import random


def print_banner():
    print("""
╔══════════════════════════════════════════════════════╗
║ 🔐 PASSCRAFT — Advanced Password Generator Tool 🔐  ║
     ✨ Craft your secure password in seconds!        ║
║      💻 Designed & Built by krish_foren6            ║
╚══════════════════════════════════════════════════════╝
    """)


def apply_replacements(text, replace_dict, leet_style):
    leet_dict = {
        'a': '@', 'A': '4', 'e': '3', 'E': '3', 'i': '1', 'I': '1',
        'o': '0', 'O': '0', 's': ['5', '$'], 'S': ['5', '$'], 't': '7', 'T': '7'
    }

    for old_char, new_char in replace_dict.items():
        text = text.replace(old_char, new_char)

    if leet_style:
        for old_char, new_chars in leet_dict.items():
            new_char = random.choice(new_chars) if isinstance(new_chars, list) else new_chars
            text = text.replace(old_char, new_char)

    return text


def check_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    types = sum([has_lower, has_upper, has_digit, has_special])

    if length >= 12 and types == 4:
        return "Strong 🔒"
    elif length >= 8 and types >= 3:
        return "Moderate ⚠️"
    else:
        return "Weak ❌"


def generate_component(charset, count):
    return [secrets.choice(charset) for _ in range(count)]


def generate_password(args):
    passwords = []

    for _ in range(args.amount):
        if args.length:
            chars = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(chars) for _ in range(args.length))
            password = apply_replacements(password, args.replace, args.leet)
        else:
            digit_part = generate_component(string.digits, args.digits)
            lower_part = generate_component(string.ascii_lowercase, args.lower)
            upper_part = generate_component(string.ascii_uppercase, args.upper)
            special_part = generate_component(string.punctuation, args.special)

            if args.pattern:
                components = {
                    'word': args.word,
                    'digit': ''.join(digit_part),
                    'lower': ''.join(lower_part),
                    'upper': ''.join(upper_part),
                    'special': ''.join(special_part),
                }

                password = args.pattern
                for key, val in components.items():
                    password = password.replace(f"{{{key}}}", val)

                password = apply_replacements(password, args.replace, args.leet)

            else:
                password_parts = digit_part + lower_part + upper_part + special_part
                if args.word:
                    password_parts.append(args.word)
                random.shuffle(password_parts)
                password = ''.join(password_parts)
                password = apply_replacements(password, args.replace, args.leet)

        passwords.append(password)
    return passwords


def save_to_file(passwords, filename):
    try:
        with open(filename, 'w') as f:
            for pw in passwords:
                f.write(pw + '\n')
        print(f"\n✅ Saved {len(passwords)} password(s) to '{filename}'")
    except Exception as e:
        print(f"❌ Error saving file: {e}")


def interactive_mode():
    print("\n--- Interactive Mode ---")
    try:
        total_length = int(input("Enter total password length (0 to skip, leave blank to customize your own): ") or 0)
        digits = int(input("How many digits? "))
        lower = int(input("How many lowercase letters? "))
        upper = int(input("How many uppercase letters? "))
        special = int(input("How many special characters? "))
        amount = int(input("How many passwords to generate? "))
        word = input("Enter a custom word to include (or leave blank): ").strip()
        pattern = input("Enter a custom pattern (use {word}, {digit},{special}) or leave blank: ").strip()
        replace_input = input("Custom replacements (e.g., a=4,i=1,s=5), leave blank if none: ").strip()
        leet = input("Apply leet style? (y/n): ").strip().lower() == 'y'

        replace_dict = {}
        if replace_input:
            for pair in replace_input.split(","):
                if "=" in pair:
                    key, value = pair.split("=")
                    replace_dict[key] = value

        class Args: pass
        args = Args()
        args.length = total_length
        args.digits = digits
        args.lower = lower
        args.upper = upper
        args.special = special
        args.amount = amount
        args.word = word
        args.pattern = pattern
        args.replace = replace_dict
        args.leet = leet

        passwords = generate_password(args)
        for pw in passwords:
            print(f"Generated Password: {pw}  | Strength: {check_strength(pw)}")

        save_choice = input("\nDo you want to save the passwords to a file? (y/n): ").strip().lower()
        if save_choice == 'y':
            filename = input("Enter file name (e.g., passwords.txt): ")
            save_to_file(passwords, filename)

    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    print_banner()
    choice = input("Choose mode: Flag Mode (f) / Interactive Mode (i): ").strip().lower()
    if choice == 'i':
        interactive_mode()
    else:
        print("🔧 Flag Mode is under construction. Use Interactive Mode for now.")


if __name__ == "__main__":
    main()
