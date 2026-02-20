import csv, pandas


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# Not with pandas
# with open("./nato_phonetic_alphabet.csv", "r") as f:
#     nato_alphabet_data = csv.reader(f)
#     print(nato_alphabet_data)
#     nato_dict = {key: value for (key, value) in nato_alphabet_data if key != "letter"}
# print(nato_dict)

# With pandas
def read_csv(csv_file):
    data = pandas.read_csv(csv_file)
    csv_dict = {row.letter: row.code for (index, row) in data.iterrows() if row.letter != "letter"}
    return csv_dict


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def main():
    phonetic_dict = read_csv("./nato_phonetic_alphabet.csv")

    word = input("Enter a word: ").upper()
    output_list = [phonetic_dict[letter] for letter in word]
    print(output_list)


if __name__ == "__main__":
    main()
