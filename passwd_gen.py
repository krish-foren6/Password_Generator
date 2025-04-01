import secrets
import string
import random
from argparse import ArgumentParser

# Tool ka description aur purpose add karna
parser = ArgumentParser(
    prog="Password Generator", 
    description="This is a powerful tool for generating strong, medium, or weak passwords with customizable patterns and replacements."
)

# Adding arguments for password customization
parser.add_argument("-n", "--numbers", type=int, default=0, help="Number of Digits in the password")
parser.add_argument("-l", "--lowercase", type=int, default=0, help="Number of lowercase letters in the password")
parser.add_argument("-u", "--uppercase", type=int, default=0, help="Number of uppercase letters in the password")
parser.add_argument("-s", "--special-chars", type=int, default=0, help="Number of special characters in the password")
parser.add_argument("-t", "--total-length", type=int, default=0, help="Total length of the password. If passed, it will ignore other options and generate a completely random password.")
parser.add_argument("-w", "--word", type=str, help="Custom word to use in password (e.g., your name)")
parser.add_argument("-p", "--pattern", type=str, help="Custom pattern (e.g., {word}_{special}_{digits})")  # Smart pattern 
parser.add_argument("-r", "--replace", type=str, help="Custom replacements (e.g., 'a=4,i=1,e=3,s=5')")  # Replacements for custom chars

# Arguments for the number of passwords and file output
parser.add_argument("-a", "--amount", type=int, help="Number of passwords you want to generate")
parser.add_argument("-o", "--output-file", type=str, help="Save your generated passwords to a file")
parser.add_argument("-lfs", "--leet-style", action='store_true', help="Apply leet style (e.g., a=4, s=5 or $)")

# Parsing command-line arguments
args = parser.parse_args()

# Default password count is 1 if -a is not given
if args.amount is None:
    args.amount = 1  

# Replace dictionary based on user input for custom replacements
replace_dict = {}                           # user ke diye gaye replacements ko store karna 
if args.replace:                            # it runs when user use -r flag   
    for pair in args.replace.split(","):    # it converts "a=4,i=1,e=3" to  ["a=4", "i=1", "e=3"] (separate kr rha h )
        key, value = pair.split("=")        # for e.g. "a=4" ->	key = "a", value = "4"
        replace_dict[key] = value           # it stores the key value pair (for e.g. replace_dict = {"a": "4", "i": "1", "e": "3"})  

# Leet style dictionary (default replacements for leet style)
leet_dict = {
    'a': '@', 'A': '4',
    'e': '3', 'E': '3',
    'i': '1', 'I': '1',
    'o': '0', 'O': '0',
    's': ['5', '$'],  # s ko 5 ya $ dono me se replace kiya ja sakta hai
    'S': ['5', '$'],  # Capital S ko bhi 5 ya $ dono me
    't': '7', 'T': '7'
}

# Function to apply custom and leet style replacements
def apply_replacements(text):
    # Apply custom replacements first
    for old_char, new_char in replace_dict.items():
        text = text.replace(old_char, new_char)
    
    # Apply leet style replacements if flag is set
    if args.leet_style:
        for old_char, new_chars in leet_dict.items():
            # Agar leet_dict me 2 replacements hain (like 5 or $ for s), to randomly choose ek
            if isinstance(new_chars, list):          #is instance is checking that is this list present or not
                new_char = random.choice(new_chars)  # randomly choose between 5 or $
            else:
                new_char = new_chars
            text = text.replace(old_char, new_char)
    
    return text

# Password generation loop
Passwords = []  # List to store all the generated passwords

# Loop for the number of passwords requested
for _ in range(args.amount):

    # Agar user ne total length diya to random password generate hoga
    if args.total_length:
        password = ''.join(secrets.choice(string.digits + string.ascii_letters + string.punctuation)
                           for _ in range(args.total_length))
    
    # Agar user ne pattern diya hai to uske hisaab se password generate hoga
    elif args.pattern:
        password = args.pattern  # Copy user pattern

        # Agar pattern me {word} diya hai to usse replace karo
        if "{word}" in password and args.word:
            word_replaced = apply_replacements(args.word)  # Word pe replacement lagao
            password = password.replace("{word}", word_replaced)

        # Agar pattern me {digit} diya hai to usse random digits se replace karo
        if "{digit}" in password:
            random_digits = ''.join(secrets.choice(string.digits) for _ in range(args.numbers))
            password = password.replace("{digit}", random_digits)

        # Agar pattern me {special} diya hai to special characters add karo
        if "{special}" in password:
            random_specials = ''.join(secrets.choice("@#$%&*!") for _ in range(args.special_chars))
            password = password.replace("{special}", random_specials)

        # Final replacement apply karna
        password = apply_replacements(password)

        Passwords.append(password)  # Final password list me add karo
    
    # Agar koi pattern nahi diya to normal method use hoga
    else:
        Password = []  # Temporary list to store password characters

        # Adding required numbers
        for _ in range(args.numbers):
            Password.append(secrets.choice(string.digits))

        # Adding required lowercase letters
        for _ in range(args.lowercase):
            Password.append(secrets.choice(string.ascii_lowercase))

        # Adding required uppercase letters
        for _ in range(args.uppercase):
            Password.append(secrets.choice(string.ascii_uppercase))

        # Adding required special characters
        for _ in range(args.special_chars):
            Password.append(secrets.choice(string.punctuation))

        # Shuffle the password to random order
        random.shuffle(Password)

        # Convert list to string and apply replacements
        final_password = apply_replacements(''.join(Password))

        Passwords.append(final_password)

# Saving the passwords to a file if specified
if args.output_file:
    with open(args.output_file, 'w') as f:
        f.write('\n'.join(Passwords))

# Printing the final output
print('\n'.join(Passwords))
