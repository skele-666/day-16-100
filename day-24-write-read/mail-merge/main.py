# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def main():
    # Get list of invited names
    with open("./Input/Names/invited_names.txt", "r") as f:
        invited_names = [line.strip() for line in f]

        # OR
        # raw_lines = f.readlines()
        # invited_names = []
        # for name in raw_lines:
        #     invited_names.append(name.strip())

    print(invited_names)

    # Open and save contents of starting letter
    with open("./Input/Letters/starting_letter.txt", "r") as f:
        starting_letter = f.read()

    print(starting_letter)

    # Loop through names in list and write letters
    for name in invited_names:
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as f:
            new_letter = starting_letter.replace("[name]", name)
            f.write(new_letter)


if __name__ == "__main__":
    main()
